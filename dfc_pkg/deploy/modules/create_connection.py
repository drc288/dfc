#!/usr/bin/python3
from fabric import Connection


def create_connection(user: str, ip: str, key: str):
    """
    This function create the connection with a server
    :param user: user of the server
    :param ip: address of the server
    :param key: key to connect
    :return: the session
    """
    return Connection(host=ip,
                      user=user,
                      connect_timeout=5,
                      connect_kwargs={
                          "key_filename": key,
                      }, )
