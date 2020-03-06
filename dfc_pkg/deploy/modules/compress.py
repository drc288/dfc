#!/usr/bin/python3
from datetime import datetime
from invoke import run as local
from colored import stylize, fg, attr
import typer

time = "%Y-%m-%dT%H-%M"


def compress(path: str):
    """
    Create a compress file of the project
    :param path: path of the project
    :return: the name of the zip file
    """
    my_date = datetime.now().strftime(time)
    split_path = path.split("/")
    version_path = path + "/versions"
    name = split_path[len(split_path) - 1]
    zip_file = my_date + "-" + name + ".tgz"
    try:
        local(f'mkdir -p {version_path}')
        local(f'tar -zcf {version_path + "/" + zip_file} --absolute-names {path} > /dev/null')
    except:
        pass
    finally:
        typer.echo(stylize(f"File created: {zip_file}", fg("green"), attr("bold")))
    return zip_file