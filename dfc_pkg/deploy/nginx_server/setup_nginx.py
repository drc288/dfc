#!/usr/bin/python3
from colored import stylize, fg, attr
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
        # To remove the error =  debconf: unable to initialize frontend: Dialog
        server.run("sudo sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile")
        server.run("sudo apt-get update -y > /dev/null")
        typer.echo(stylize("Server updated", fg("green"), attr("bold")))
        server.run("sudo apt-get install nginx -y > /dev/null")
        server.run("sudo apt-get install python3-pip -y > /dev/null")
        server.run("sudo pip3 install -U pip")
        typer.echo(stylize("NGINX and PIP are installed ", fg("green"), attr("bold")))
    except socket.error:
        typer.echo(stylize(f'Unable to connect to {user}@{ip}', fg("red")))
        exit(0)


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


def config_nginx(server, path: str, zip_file: str, user: str):
    """
    This function configure the nginx server with the project
    :param server: Connection of the server
    :param path: Original path project folder
    :param zip_file: The zip file
    :return: void
    """
    try:
        path_split = path.split("/")
        remove_path = path_split[1]
        path_project = path_split[len(path_split) - 1]
        # Create the folder /data/ descompress the zip file in /data/
        server.run(f"sudo mkdir -p /data/")
        server.run(f"sudo tar -xzf /tmp/{zip_file} -C /data/")
        # Move the path project to /data/
        server.run(f"sudo mv /data{path} /data/")
        # Remove trash files in /data/DESS_FILE and the tmp
        server.run(f"sudo rm -rf /data/{remove_path}/ /tmp/{zip_file}")
        # Change the user and group owner of /data/
        server.run(f"sudo chown -R {user}. /data")
        server.run(f"sudo pip install  -r /data/{path_project}/requirements.txt > /dev/null")
        typer.echo(stylize("Modules are installed", fg("green"), attr("bold")))
        typer.echo(stylize("NGINX configured", fg("green"), attr("bold")))
    except socket.error:
        typer.echo(stylize("An error has occurred in the configuration NGINX", fg("red")))


def run_gunicorn(server, path: str, port: int):
    path_split = path.split("/")
    name_path = path_split[len(path_split) - 1]
    try:
        server.run(f"cd /data/{name_path} && gunicorn -b 0.0.0.0:{port} web.app:app &> /dev/null &", hide=True)
        typer.echo(stylize(f"Server are excecuted in the port: {port}", fg("green"), attr("bold")))
    except socket.error:
        typer.echo(stylize("An error has occurred in the configuration GUNICORN", fg("red")))
