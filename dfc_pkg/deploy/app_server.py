#!/usr/bin/python3
from datetime import datetime
from invoke import run as local
import os
import typer



app = typer.Typer()
time = "%Y-%m-%dT%H-%M"
path_proyect = os.getenv("DFC_PATH")


def verify_path(path: str):
    """
    This function verify the project folder
    :param path: path to verify the project
    :return: void
    """
    path_web = path + "/web"
    path_api = path + "/api"
    path_test = path + "/tests"
    path_models = path + "/models"
    requirements = path + "/requirements.txt"

    if os.path.isdir(path_web) is False:
        typer.echo(f"You need to create the directory web in: {path}")
        exit(0)
    if os.path.isdir(path_api) is False:
        typer.echo(f"You need to create the directory api in: {path}")
        exit(0)
    if os.path.isdir(path_models) is False:
        typer.echo(f"You need to create the directory models in: {path}")
        exit(0)
    if os.path.isdir(path_test) is False:
        typer.echo(f"You need to create the directory test in: {path}")
        exit(0)
    if os.path.isfile(requirements) is False:
        typer.echo("You need the requirements file to install all the dependencies in the web server")
        exit(0)


def compress(path: str):
    my_date = datetime.now().strftime(time)
    split_path = path.split("/")
    version_path = path + "/versions"
    name = split_path[len(split_path) - 1]
    zip_file = my_date + "-" + name + ".tgz"
    local(f'mkdir -p {version_path}')
    local(f'tar -zcvf {version_path}/{zip_file} {path}')


@app.command()
def app_server(ip: str, path_key: str, user_ssh: str):
    if path_proyect is None:
        os.chdir(os.path.dirname(__file__))
        verify_path(os.getcwd())
    else:
        verify_path(path_proyect)
        compress(path_proyect)



if __name__ == "__main__":
    app()
