import os

SYSTEM_MANAGER_ADDR = (
    "http://"
    + os.environ.get("SYSTEM_MANAGER_URL")
    + ":"
    + str(os.environ.get("SYSTEM_MANAGER_PORT"))
)
