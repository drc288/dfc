#!/usr/bin/python3
from commands.modules.create_connection import create_connection
from commands.nginx_server.install_nginx import install_nginx
from commands.mysql_server.setup_mysql import install_mysql
import typer

app = typer.Typer()


@app.command()
def nginx(
    ip: str = typer.Option(...),
    key_ssh: str = typer.Option(...),
    user_ssh: str = typer.Option(...),
):
    """
    This command install a nginx server
    """
    cn = create_connection(user_ssh, ip, key_ssh)
    install_nginx(cn)


@app.command()
def mysql(
    ip: str = typer.Option(...),
    key_ssh: str = typer.Option(...),
    user_ssh: str = typer.Option(...),
):
    """
    This command install mysql server
    """
    cn = create_connection(user_ssh, ip, key_ssh)
    install_mysql(cn)


if __name__ == "__main__":
    app()
