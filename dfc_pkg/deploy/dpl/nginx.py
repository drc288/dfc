#!/usr/bin/python3
from colored import  stylize, fg, attr
import socket
import typer


def install_nginx(server, user: str, ip: str):
    """
    This function install NGINX server
    :param ip: Ip address
    :param user: User to connect
    :param server: the connection
    :return: void
    """
    try:
        server.run("sudo apt-get update -y > /dev/null")
        typer.echo(stylize("Server updated", fg("green"), attr("bold")))
        server.run("sudo apt-get install nginx -y > /dev/null")
        typer.echo(stylize("NGINX installed", fg("green"), attr("bold")))
    except socket.error:
        typer.echo(stylize(f'Unable to connect to {user}@{ip}', fg("red")))
        exit(0)


def upload_files(path: str, server, zip_file: str):
    """
    This function upload the file tar to the external server
    :param path: path of the file
    :param server: conection to the server
    :param zip_file: name of the file
    :return: void
    """
    try:
        server.put(path + "/versions/" + zip_file, "/tmp/")
        typer.echo(stylize("File upload", fg("green"), attr("bold")))
    except socket.error:
        typer.echo(stylize("An error has occurred in the upload of the file", fg("red")))