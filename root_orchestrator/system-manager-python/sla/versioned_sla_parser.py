import json

from sla.sla_versions import sla_validator_by_version


class SLAFormatError(BaseException):
    message = "The given SLA was not formatted correctly"


# if the file was sent with curl it is enough to use only file.read
# if it was uploaded with a post request we have to use also json.loads


def parse_sla_json(sla):
    print("A#" * 10)

    json_data = sla

    if not isinstance(sla, dict):
        json_data = json.loads(sla)

    print("B#" * 10)
    version = json_data["sla_version"]
    validator = sla_validator_by_version[version]

    print("C#" * 10)

    if validator(json_data):
        print("D1#" * 10)
        return json_data
    else:
        raise SLAFormatError
