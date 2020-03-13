#!/usr/bin/python3
from colored import fg, stylize, attr
import paramiko
import socket
import typer


def install_mysql(server):
    """
    This function connect a external server and install mysql
    :param server: server to connect
    :return: void
    """
    try:
        typer.echo(stylize('Starting with the installation of mysql', fg('blue')))
        server.run('sudo apt-get install mysql-server -y > /dev/null')
        typer.echo(stylize('Mysql has been installed', fg('green'), attr('bold')))
    except socket.error as err:
        typer.echo(stylize(f'Unable to connect, error: {err}', fg("red")))
    except paramiko.ssh_exception.AuthenticationException as err:
        typer.echo(stylize(f'SSH Error: {err}', fg("red")))
