#!/usr/bin/python3
"""
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Command line interpreter for Deploy Flask CLI (DFC)  #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    :deploy:
        Create the deploy for NGINX server v0.1
"""
import commands.command_deploy as deploy
import commands.command_build as build
import commands.command_integrate as integrate
import typer

app = typer.Typer()

app.add_typer(deploy.app, name="deploy")
app.add_typer(build.app, name="build")
# app.add_typer(integrate.app, name="integrate")


if __name__ == "__main__":
    app()
