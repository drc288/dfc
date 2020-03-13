#!/usr/bin/python3
from deploy.mysql_server.verify_mysql import verify_mysql
from colored import stylize, fg, attr
import paramiko
import socket
import typer


def setup_project(server, path: str, zip_file: str, user: str):
    """
    This function configure the nginx server with the project
    :param server: Connection of the server
    :param path: Original path project folder
    :param zip_file: The zip file
    :param user: user
    :return: void
    """
    try:
        path_split = path.split("/")
        remove_path = path_split[1]
        path_project = path_split[len(path_split) - 1] + "/dev"
        # Create the folder /data/ descompress the zip file in /data/
        server.run(f"sudo mkdir -p /data/")
        server.run(f"sudo tar -xzf /tmp/{zip_file} -C /data/")
        # Move the path project to /data/
        server.run(f"sudo mv /data{path} /data/")
        # Remove trash files in /data/DESS_FILE and the tmp
        server.run(f"sudo rm -rf /data/{remove_path}/ /tmp/{zip_file}")
        # Change the user and group owner of /data/
        server.run(f"sudo chown -R {user}. /data")
        server.run("sudo apt-get install python3-pip -y > /dev/null")
        server.run("sudo pip3 install -U pip > /dev/null")
        if verify_mysql(path):
            typer.echo(stylize("Mysql modules were found", fg("blue")))
            server.run("sudo dpkg --configure -a > /dev/null")
            server.run("sudo apt-get install libmysqlclient-dev -y > /dev/null")
            server.run("sudo apt-get install libmariadbclient-dev -y > /dev/null")
            typer.echo(stylize("Modules mysql are installed", fg("green"), attr("bold")))
        server.run(f"sudo pip3 install  -r /data/{path_project}/requirements.txt > /dev/null")
        typer.echo(stylize("Modules are installed", fg("green"), attr("bold")))
        typer.echo(stylize("NGINX configured", fg("green"), attr("bold")))
    except socket.error:
        typer.echo(stylize("An error has occurred in the configuration NGINX", fg("red")))
