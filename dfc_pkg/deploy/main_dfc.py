#!/usr/bin/python3
from deploy.modules.verify_path import verify_path
from deploy.modules.compress import compress
from deploy.modules.create_connection import create_connection
from deploy.modules.upload_files import upload_files
from deploy.controllers.config_gunicorn import create_service_gunicorn
from deploy.controllers.config_nginx import config_nginx
from deploy.nginx_server.setup_nginx import install_nginx, component
from deploy.mysql_server.setup_mysql import install_mysql
import os
import typer

app = typer.Typer()
path_project = os.getenv("DFC_PATH")


@app.command()
def run_nginx(ip: str = typer.Option(...), path_key: str = typer.Option(...),
              user_ssh: str = typer.Option(...)):
    """
    This command install a basic configuration for nginx daemon in remote server
    """
    server = create_connection(user_ssh, ip, path_key)
    install_nginx(server)


@app.command()
def run_mysql(ip: str = typer.Option(...), path_key: str = typer.Option(...),
              user_ssh: str = typer.Option(...)):
    """
    This command install a basic mysql server
    """
    server = create_connection(user_ssh, ip, path_key)
    install_mysql(server)

@app.command()
def deploy_project(ip: str = typer.Option(...), path_key: str = typer.Option(...),
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
        server = create_connection(user_ssh, ip, path_key)
        upload_files(server, pwd_directory, zip_file)
        create_service_gunicorn(server, pwd_directory, user_ssh, dfc_path)
        component(server, pwd_directory, zip_file, user_ssh)
        config_nginx(server, pwd_directory, dfc_path)
    else:
        verify_path(path_project)
        zip_file = compress(path_project)
        server = create_connection(user_ssh, ip, path_key)
        upload_files(server, path_project, zip_file)
        create_service_gunicorn(server, path_project, user_ssh, os.getcwd())
        component(server, path_project, zip_file, user_ssh)
        config_nginx(server, path_project, os.getcwd())


if __name__ == "__main__":
    app()
