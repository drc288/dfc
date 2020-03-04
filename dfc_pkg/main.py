#!/usr/bin/python3
import typer
import deploy.nginx_project as nginx_project

app = typer.Typer()

app.add_typer(nginx_project.app, name="deploy")

if __name__ == "__main__":
    app()