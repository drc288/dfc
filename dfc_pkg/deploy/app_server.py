#!/usr/bin/python3
import os
import typer
app = typer.Typer()

path_proyect = os.getenv("DFC_PATH")

@app.command()
def app_server(ip: str = typer.Option(...)):
    if path_proyect is None:
        typer.echo("Checking the current path project")
        os.chdir(os.path.dirname(__file__))
        path_web = os.getcwd() + "/web"
        path_api = os.getcwd() + "/api"
        requirements = os.getcwd() + "/requirements.txt"

        if os.path.isdir(path_web) is False:
            typer.echo(f"You need to create the directory web in the path: {os.getcwd()}")
            exit(0)
        if os.path.isdir(path_api) is False:
            typer.echo(f"You need to create the directory api in the path: {os.getcwd()}")
            exit(0)
        if os.path.isfile(requirements) is False:
            typer.echo("You need the requirements file to install all the dependencies in the web server")
    else:
        path_web = path_proyect + "/web"
        path_api = path_proyect + "/api"
        requirements = path_proyect + "/requirements.txt"

        if os.path.isdir(path_web) is False:
            typer.echo(f"You need to create the directory web in the path: {os.getcwd()}")
            exit(0)
        if os.path.isdir(path_api) is False:
            typer.echo(f"You need to create the directory api in the path: {os.getcwd()}")
            exit(0)
        if os.path.isfile(requirements) is False:
            typer.echo("You need the requirements file to install all the dependencies in the web server")


if __name__ == "__main__":
    app()