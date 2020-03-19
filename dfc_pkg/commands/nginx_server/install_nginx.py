#!/usr/bin/python3
from colored import stylize, fg, attr
import paramiko
import socket
import typer


def install_nginx(server):
    """
    This function install NGINX server
    :param ip: Ip address
    :param user: User to connect
    :param server: the connection
    :return: void
    """
    try:
        # Updating the server
        typer.echo(stylize("The server is being updated", fg("blue")))
        server.run('sudo sed -i "s/^mesg n$/tty -s && mesg n/g" /root/.profile')
        server.run("sudo apt-get install dialog apt-utils -y > /dev/null 3> /dev/null")
        server.run("sudo apt-get update -y > /dev/null")
        typer.echo(stylize("Server updated", fg("green"), attr("bold")))
        # Init to install nginx server
        typer.echo(stylize("Installing nginx server", fg("blue")))
        server.run("sudo apt-get install nginx -y > /dev/null 3> /dev/null")
        # Verify the path for mysql dependencies
        typer.echo(stylize("Installing pip3 for python3", fg("blue")))
        server.run("sudo apt-get install python3-pip -y > /dev/null")
        server.run("sudo pip3 install -U pip > /dev/null")
        typer.echo(stylize("NGINX and PIP are installed ", fg("green"), attr("bold")))
    except socket.error:
        typer.echo(stylize(f"Unable to connect", fg("red")))
        exit(0)
    except paramiko.ssh_exception.AuthenticationException:
        typer.echo(stylize(f"SSH Error, verify the kay path", fg("red")))
        exit(0)
