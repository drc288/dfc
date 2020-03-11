#!/usr/bin/python3
from deploy.controllers.make_file import render_template, make_file
from colored import stylize, fg, attr
import typer
import socket


def config_nginx(server, path: str, main_path: str):
    """
    This function configure the nginx file, and edit the default route
    :param server: Server to run command
    :param path: path of the project
    """
    path_split = path.split("/")
    name_path = path_split[len(path_split) - 1]
    params = { "{<debug_name>}": name_path }
    new_file = render_template(main_path + "/templates/default", params)
    make_file("/tmp/default", new_file)
    try:
        server.put("/tmp/default", "/tmp/")
        server.run("sudo chown root. /tmp/default && sudo chmod 644 /tmp/default")
        server.run("sudo rm -rf /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default")
        server.run("sudo mv /tmp/default /etc/nginx/sites-available/")
        server.run("sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled")
        server.run("sudo service nginx restart")
        typer.echo(stylize("Server are Run", fg("green"), attr("bold")))
    except socket.error:
        print("error")
