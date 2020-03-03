#!/usr/bin/python3
import typer
import deploy.app_server as app_server

app = typer.Typer()

app.add_typer(app_server.app, name="deploy")

if __name__ == "__main__":
    app()