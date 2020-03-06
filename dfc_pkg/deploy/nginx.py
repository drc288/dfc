#!/usr/bin/python3
from deploy.modules.verify_path import verify_path
from deploy.modules.compress import compress
from deploy.modules.create_connection import create_connection
from deploy.modules.upload_files import upload_files
from deploy.controllers.config_gunicorn import create_service_gunicorn
from deploy.nginx_server.setup_nginx import install_nginx, component
import os
import typer

app = typer.Typer()
path_project = os.getenv("DFC_PATH")


@app.command()
def nginx_project(ip: str = typer.Option(...), path_key: str = typer.Option(...),
                  user_ssh: str = typer.Option(...), port: int = typer.Option(...)):
    """
    create a app server, connect to host an deploy the services in nginx server
    :param ip: host to connect
    :param path_key: ssh key
    :param user_ssh: user to connect
    :param port: the number of the port to run gunicorn
    :return: deploy server
    """
    os.chdir(os.path.dirname(__file__))
    if path_project is None:
        verify_path(os.getcwd())
        zip_file = compress(os.getcwd())
        server = create_connection(user_ssh, ip, path_key)
        install_nginx(server, user_ssh, ip)
        upload_files(server, os.getcwd(), zip_file)
        component(server, os.getcwd(), zip_file, user_ssh)
        create_service_gunicorn(server, os.getcwd(), user_ssh, port, os.getcwd())
    else:
        verify_path(path_project)
        zip_file = compress(path_project)
        server = create_connection(user_ssh, ip, path_key)
        install_nginx(server, user_ssh, ip)
        upload_files(server, path_project, zip_file)
        component(server, path_project, zip_file, user_ssh)
        create_service_gunicorn(server, path_project, user_ssh, os.getcwd())


if __name__ == "__main__":
    app()
