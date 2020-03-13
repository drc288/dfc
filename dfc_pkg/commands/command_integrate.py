#!/usr/bin/python3
from commands.modules.create_connection import create_connection
from commands.mysql_server.integrate_mysql import integrate_mysql
import typer


app = typer.Typer()


@app.command()
def mysql_flaskcli(
        ip: str = typer.Option(...),
        key_ssh: str = typer.Option(...),
        user_ssh: str = typer.Option(...),
        name_project: str = typer.Option(...)
):
    cn = create_connection(user_ssh, ip, key_ssh)
    integrate_mysql(cn, name_project)


if __name__ == "__main__":
    app()