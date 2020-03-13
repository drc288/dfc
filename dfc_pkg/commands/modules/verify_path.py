#!/usr/bin/python3
from colored import stylize, fg
import typer
import os


def verify_path(path: str):
    """
    This function verify the project folder
    :param path: path to verify the project
    :return: void
    """
    path_web = path + "/web"
    web_app = path + "/web/app.py"
    path_dev = path + "/dev"
    path_api = path + "/api"
    path_models = path + "/models"
    requirements = path + "/dev/requirements.txt"
    dev_mysql = path + "/dev/setup_mysql_dev.sql"


    if os.path.isdir(path_web) is False:
        typer.echo(stylize(f"You need to create the directory web in: {path}", fg("red")))
        exit(0)
    if os.path.isdir(path_api) is False:
        typer.echo(stylize(f"You need to create the directory api in: {path}", fg("red")))
        exit(0)
    if os.path.isdir(path_models) is False:
        typer.echo(stylize(f"You need to create the directory models in: {path}", fg("red")))
        exit(0)
    if os.path.isdir(path_dev) is False:
        typer.echo(stylize(f"You need to create the directory dev in : {path}", fg("red")))
        exit(0)
    if os.path.isfile(requirements) is False:
        typer.echo(
            stylize("You need the requirements file to install all the dependencies in the web server", fg("red")))
        exit(0)
    if os.path.isfile(dev_mysql) is False:
        typer.echo(stylize(f'You need the setup_mysql_dev.sql in: {path + "/dev"}', fg("red")))
        typer.echo(stylize('Example:', fg("blue")))
        typer.echo(stylize('CREATE DATABASE, CREATE USER, GRANT PERMISSIONS', fg("blue")))
        exit(0)
    if os.path.isfile(web_app) is False:
        typer.echo(stylize("You need the app.py file in /web", fg("red")))
        exit(0)
