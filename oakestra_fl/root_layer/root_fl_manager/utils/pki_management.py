import ipaddress
import pathlib
from datetime import datetime, timedelta

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

SSL_PATH = pathlib.Path("/etc/ssl")
CA_KEY_PATH = SSL_PATH / "ca_key.pem"
CA_CERT_PATH = SSL_PATH / "ca_cert.pem"

REGULAR_KEY_PATH = SSL_PATH / "key.pem"
REGULAR_CERT_PATH = SSL_PATH / "cert.pem"


def create_private_key(path_to_store_new_key: pathlib.Path) -> None:
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )
    with open(str(path_to_store_new_key), "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )


def create_cert(is_ca: bool, cert_name: str) -> None:

    with open(CA_KEY_PATH, "rb") as f:
        ca_private_key = serialization.load_pem_private_key(
            f.read(), password=None, backend=default_backend()
        )

    if not is_ca:
        with open(REGULAR_KEY_PATH, "rb") as f:
            regular_private_key = serialization.load_pem_private_key(
                f.read(), password=None, backend=default_backend()
            )

        with open(CA_CERT_PATH, "rb") as f:
            ca_certificate = x509.load_pem_x509_certificate(f.read(), default_backend())

    subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, cert_name)])
    if is_ca:
        issuer = subject

    builder = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer if is_ca else ca_certificate.subject)
        .public_key((ca_private_key if is_ca else regular_private_key).public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.utcnow())
        .not_valid_after(datetime.utcnow() + timedelta(days=365))
        .add_extension(
            x509.BasicConstraints(ca=is_ca, path_length=None),
            critical=True,
        )
        .add_extension(
            x509.KeyUsage(
                digital_signature=True,
                key_cert_sign=is_ca,
                crl_sign=is_ca,
                content_commitment=False,
                key_encipherment=False,
                data_encipherment=False,
                encipher_only=False,
                decipher_only=False,
                key_agreement=False,
            ),
            critical=True,
        )
        .add_extension(
            x509.SubjectAlternativeName(
                [
                    x509.IPAddress(ipaddress.ip_address("192.168.178.44")),
                    # x509.IPAddress(ipaddress.ip_address("192.168.1.2")),
                    # Add more SAN entries as needed
                    # x509.DNSName("www.example.com"),
                ]
            ),
            critical=False,
        )
    )

    new_certificate = builder.sign(
        private_key=ca_private_key, algorithm=hashes.SHA256(), backend=default_backend()
    )
    with open(CA_CERT_PATH if is_ca else REGULAR_CERT_PATH, "wb") as f:
        f.write(new_certificate.public_bytes(serialization.Encoding.PEM))


def handle_pki():
    create_private_key(CA_KEY_PATH)
    create_cert(is_ca=True, cert_name="Oakestra Root FL Manager CA Certificate")

    create_private_key(REGULAR_KEY_PATH)
    create_cert(is_ca=False, cert_name="Oakestra Root FL Manager Regular Certificate")
