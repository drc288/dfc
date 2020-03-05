#!/usr/bin/python3
from deploy.dpl.verify_path import verify_path
from deploy.dpl.compress import compress
from deploy.dpl.create_connection import create_connection
from deploy.dpl.nginx import install_nginx, upload_files, config_nginx, run_gunicorn
import os
import typer

app = typer.Typer()
path_proyect = os.getenv("DFC_PATH")


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
    if path_proyect is None:
        os.chdir(os.path.dirname(__file__))
        verify_path(os.getcwd())
        zip_file = compress(os.getcwd())
        server = create_connection(user_ssh, ip, path_key)
        install_nginx(server, user_ssh, ip)
        upload_files(os.getcwd(), server, zip_file)
    else:
        verify_path(path_proyect)
        zip_file = compress(path_proyect)
        server = create_connection(user_ssh, ip, path_key)
        install_nginx(server, user_ssh, ip)
        upload_files(server, path_proyect, zip_file)
        config_nginx(server, path_proyect, zip_file, user_ssh)
        run_gunicorn(server, path_proyect, port)



if __name__ == "__main__":
    app()
