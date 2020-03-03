#!/usr/bin/python3
from datetime import datetime
from invoke import run as local
from fabric import Connection
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
        print(version_path)
        local(f'mkdir -p {version_path}')
        local(f'tar -zcf {version_path + "/" + zip_file} {path}')
    except:
        pass
    finally:
        typer.echo(f"File created: {zip_file}")

    return zip_file


def create_connection(user: str, ip: str, key: str):
    """
    This function create the connection with a server
    :param user: user of the seerver
    :param ip: address of the server
    :param key: key to connect
    :return: the session
    """
    cn = Connection(host=ip,
                    user=user,
                    connect_kwargs={
                        "key_filename": key,
                    },)
    return cn


def install_nginx(server):
    """
    This function install nginx server
    :param server: the connection
    :return: void
    """
    server.run("sudo apt-get update -y > /dev/null")
    typer.echo("Server updated")
    server.run("sudo apt-get install nginx -y > /dev/null")
    typer.echo("Nginx installed")


def upload_files(path: str, server, zip_file: str):
    server.put(path + "/versions/" + zip_file, "/tmp/")
    typer.echo("File upload")


@app.command()
def app_server(ip: str = typer.Option(...), path_key: str = typer.Option(...),
               user_ssh: str = typer.Option(...)):
    """
    create a app server, connect to host an deploy the services in nginx server
    :param ip: host to connect
    :param path_key: ssh key
    :param user_ssh: user to connect
    :return: deploy server
    """
    if path_proyect is None:
        os.chdir(os.path.dirname(__file__))
        verify_path(os.getcwd())
        zip_file = compress(os.getcwd())
        server = create_connection(user_ssh, ip, path_key)
        install_nginx(server)
    else:
        verify_path(path_proyect)
        zip_file = compress(path_proyect)
        server = create_connection(user_ssh, ip, path_key)
        install_nginx(server)
        upload_files(path_proyect, server, zip_file)




if __name__ == "__main__":
    app()
