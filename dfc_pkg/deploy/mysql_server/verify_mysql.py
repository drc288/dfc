#!/usr/bin/python3


def verify_mysql(path: str):
    """
    verify_mysql: Verify if the requirements file have the service mysql
    :param path: the path of the file
    :return:
    """
    vp = False
    requirements = path + "/dev/requirements.txt"
    with open(requirements, "r") as f:
        file = f.read()
        if "mysql" in file:
            vp = True

    return vp
