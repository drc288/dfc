#!/usr/bin/python3
from deploy.controllers.make_file import render_template, make_file
from colored import stylize, fg, attr
import typer
import socket


def create_service_gunicorn(server, path: str, user: str, main_path: str):
    """
    This function create the gunicorn as a service
    :param server: The connection with the remote server
    :param path: path of the project
    :param user: user of the service
    :param main_path: the main path of the DFC
    :return: void
    """
    path_split = path.split("/")
    name_path = path_split[len(path_split) - 1]
    command_gunicorn = "gunicorn --bind unix:gunicorn.sock web.app:app"
    params = {
        "{<name>}": user,
        "{<name_project>}": name_path,
        "{<gunicorn_command>}": command_gunicorn
    }
    new_file = render_template(main_path + "/templates/gunicorn.service", params)
    make_file("/tmp/gunicorn.service", new_file)
    try:
        server.put("/tmp/gunicorn.service", "/tmp/")
        server.run("sudo chown root. /tmp/gunicorn.service && sudo chmod 777 /tmp/gunicorn.service")
        server.run("sudo mv /tmp/gunicorn.service /etc/systemd/system/")
        server.run("sudo systemctl daemon-reload")
        server.run("sudo systemctl start gunicorn.service")
        typer.echo(stylize("Service gunicorn are installed", fg("green"), attr("bold")))
    except socket.error:
        print("error")
