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
    path_api = path + "/api"
    path_test = path + "/tests"
    path_models = path + "/models"
    requirements = path + "/requirements.txt"

    if os.path.isdir(path_web) is False:
        typer.echo(stylize(f"You need to create the directory web in: {path}", fg("reed")))
        exit(0)
    if os.path.isdir(path_api) is False:
        typer.echo(stylize(f"You need to create the directory api in: {path}", fg("reed")))
        exit(0)
    if os.path.isdir(path_models) is False:
        typer.echo(stylize(f"You need to create the directory models in: {path}", fg("red")))
        exit(0)
    if os.path.isdir(path_test) is False:
        typer.echo(stylize(f"You need to create the directory test in: {path}", fg("red")))
        exit(0)
    if os.path.isfile(requirements) is False:
        typer.echo(
            stylize("You need the requirements file to install all the dependencies in the web server", fg("red")))
        exit(0)