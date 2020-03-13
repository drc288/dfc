#!/usr/bin/python3
from colored import stylize, fg, attr
import typer


def integrate_mysql(server, name_project: str):
    path_project = "/data/" + name_project
    path_verify = ["dev", "web", "models", "api"]
    verify = None

    typer.echo(stylize("Initialized the mysql integration with the project", fg("blue")))
    try:
        verify = server.run(f"ls {path_project}", hide=True)
    except :
        pass

    if verify is None:
        typer.echo(stylize(f"The path: {path_project} not exists", fg("red")))
    else:
        for path in path_verify:
            if path in verify.stdout:
                continue
            else:
                typer.echo(stylize(f"You need the path: {path}", fg("red")))
                exit(0)
        server.run(f"cat {path_project}/dev/setup_mysql_dev.sql | sudo mysql")
        typer.echo(stylize("Integration complete", fg("green")))
