#!/usr/bin/python3
from commands.modules.verify_path import verify_path
from commands.modules.compress import compress
from commands.modules.create_connection import create_connection
from commands.modules.upload_files import upload_files
from commands.controllers.config_gunicorn import create_service_gunicorn
from commands.controllers.config_nginx import config_nginx
from commands.nginx_server.setup_project import setup_project
import os
import typer

app = typer.Typer()
path_project = os.getenv("DFC_PATH")


@app.command()
def project(ip: str = typer.Option(...), key_ssh: str = typer.Option(...),
            user_ssh: str = typer.Option(...)):
    """
    Deploys an application under the NAFA architecture, this deployment contains the configuration of the app,
    the execution and the recreation of the gunicorn as a daemon, if you have a project in other path,
    specify it as follows: export DFC_PATH.
    """
    dfc_path = os.path.dirname(__file__)
    pwd_directory = os.getcwd()
    if path_project is None:
        verify_path(pwd_directory)
        zip_file = compress(os.getcwd())
        server = create_connection(user_ssh, ip, key_ssh)
        upload_files(server, pwd_directory, zip_file)
        create_service_gunicorn(server, pwd_directory, user_ssh, dfc_path)
        setup_project(server, pwd_directory, zip_file, user_ssh)
        config_nginx(server, pwd_directory, dfc_path)
    else:
        verify_path(path_project)
        zip_file = compress(path_project)
        server = create_connection(user_ssh, ip, path_key)
        upload_files(server, path_project, zip_file)
        create_service_gunicorn(server, path_project, user_ssh, dfc_path)
        setup_project(server, path_project, zip_file, user_ssh)
        config_nginx(server, path_project, dfc_path)


if __name__ == "__main__":
    app()
