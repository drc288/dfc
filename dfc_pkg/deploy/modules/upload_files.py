#!/usr/bin/python3
from colored import stylize, fg, attr
import socket
import typer

def upload_files(server, path: str, zip_file: str):
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