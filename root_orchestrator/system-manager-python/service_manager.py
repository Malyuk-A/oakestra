import threading

import mongodb_client

instance_ip_lock = threading.Lock()
subnetip_ip_lock = threading.Lock()


def new_job_rr_address(job_data):
    """
    This method is called at deploy time. Given the deployment descriptor check if a custom valid RR ip has been assigned
    by the user and returns that to the service. Otherwise a new RR address will be returned.
    @return: string, a new address
    @raise: exception if an invalid RR address has been provided by the user
    """
    address = job_data.get('RR_ip')
    job_name = job_data['app_name'] + "." + job_data['app_ns'] + "." + job_data['service_name'] + "." + job_data[
        'service_ns']

    if address is not None:
        address_arr = str(address).split(".")
        if len(address_arr) == 4:
            if address_arr[0] != "172" or address_arr[1] != "30":
                raise Exception("RR ip address must be in the form 172.30.x.y")
            job = mongodb_client.mongo_find_job_by_ip(address)
            if job is not None:
                if job['job_name'] != job_name:
                    raise Exception("RR ip address already used by another service")
            return address
        else:
            raise Exception("Invalid RR_ip address length")
    return new_instance_ip()


def new_instance_ip():
    """
    Function used to assign a new instance IP address for a Service that is going to be deployed.
    An instance address is a static address bounded with a single replica of a service
    @return: string,
        A new address from the address pool. This address is now removed from the pool of available addresses
    """
    with instance_ip_lock:
        addr = mongodb_client.mongo_get_service_address_from_cache()

        while addr is None:
            addr = mongodb_client.mongo_get_next_service_ip()
            next_addr = _increase_service_address(addr)
            mongodb_client.mongo_update_next_service_ip(next_addr)
            job = mongodb_client.mongo_find_job_by_ip(addr)
            if job is not None:
                addr = None

        return _addr_stringify(addr)


def clear_instance_ip(addr):
    """
    Function used to give back an Instance address to the pool of available addresses
    @param addr: string,
        the address that is going to be added back to the pool
    """
    addr = _addr_destringify(addr)

    # Check if address is in the correct rage
    assert addr[1] == 30
    assert 0 <= addr[2] < 256
    assert 0 <= addr[3] < 256

    with instance_ip_lock:
        next_addr = mongodb_client.mongo_get_next_service_ip()

        # Ensure that the give address is actually before the next address from the pool
        assert int(str(addr[2]) + str(addr[3])) < int(str(next_addr[2]) + str(next_addr[3]))

        mongodb_client.mongo_free_service_address_to_cache(addr)


def new_subnetwork_addr():
    """
    Function used to generate a new subnetwork address for any worker node
    @return: string,
        A new address from the address pool. This address is now removed from the pool of available addresses
    """
    with subnetip_ip_lock:
        addr = mongodb_client.mongo_get_subnet_address_from_cache()

        if addr is None:
            addr = mongodb_client.mongo_get_next_subnet_ip()
            next_addr = _increase_subnetwork_address(addr)
            mongodb_client.mongo_update_next_subnet_ip(next_addr)

        return _addr_stringify(addr)


def clear_subnetwork_ip(addr):
    """
    Function used to give back a subnetwork address to the pool of available addresses
    @param addr: string,
        the address that is going to be added back to the pool
    """
    addr = _addr_destringify(addr)

    # Check if address is in the correct rage
    assert 17 < addr[1] < 30
    assert 0 <= addr[2] < 256
    assert addr[3] in [0, 64, 128]

    with subnetip_ip_lock:
        next_addr = mongodb_client.mongo_get_next_subnet_ip()

        # Ensure that the give address is actually before the next address from the pool
        assert int(str(addr[1]) + str(addr[2]) + str(addr[3])) < int(
            str(next_addr[1]) + str(next_addr[2]) + str(next_addr[3]))

        mongodb_client.mongo_free_subnet_address_to_cache(addr)


def service_resolution(name):
    job = mongodb_client.mongo_find_job_by_name(name)
    if job is not None:
        return job['instance_list']
    return []


def service_resolution_ip(ip):
    job = mongodb_client.mongo_find_job_by_ip(ip)
    if job is not None:
        return job['instance_list']
    return []


def _increase_service_address(addr):
    new2 = addr[2]
    new3 = (addr[3] + 1) % 254
    if new3 == 0:
        new2 = (addr[2] + 1) % 254
        if new2 == 0:
            raise RuntimeError("Exhausted Address Space")
    return [addr[0], addr[1], new2, new3]


def _increase_subnetwork_address(addr):
    new1 = addr[1]
    new2 = addr[2]
    new3 = addr[3]
    new3 = (new3 + 64) % 256
    if new3 == 0:
        new2 = (new2 + 1) % 256
    if new2 == 0 and new2 != addr[2]:
        new1 = (new1 + 1) % 30
        if new1 == 0:
            raise RuntimeError("Exhausted Address Space")
    return [addr[0], new1, new2, new3]


def _addr_stringify(addr):
    res = ""
    for n in addr:
        res = res + str(n) + "."
    return res[0:len(res) - 1]


def _addr_destringify(addrstr):
    addr = []
    for num in addrstr.split("."):
        addr.append(int(num))
    return addr
