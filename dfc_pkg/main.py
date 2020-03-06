#!/usr/bin/python3
"""
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Command line interpreter for Deploy Flask CLI (DFC)  #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    :deploy:
        Create the deploy for NGINX server v0.1
"""
import typer
import deploy.nginx as nginx

app = typer.Typer()

app.add_typer(nginx.app, name="deploy")

if __name__ == "__main__":
    app()