import click
from .runner import Runner

@click.command()
@click.argument("path")
@click.option("--path_out", help="Where to save output.")
@click.option(
    "--parameters",
    "-p",
    nargs=2,
    multiple=True,
    help="Parameters to pass to the parameters cell.",
)
def tusk(path, path_out, parameters):
    """Simple program that greets NAME for a total of COUNT times."""

    click.echo(f"path: {path}")
    click.echo(f"path_out: {path_out}")
    click.echo(f"parameters: {parameters}")
    if not len(parameters):
        parameters = None
    R = Runner(path, path_out=path_out, parameters=parameters)
    R.run()


# from typing import List, Optional, Tuple
# import typer
# 

# app = typer.Typer()


# @app.command()
# def run(
#     ctx: typer.Context,
#     path: str,
#     path_out: str = None,
#     user: Optional[List[str]] = typer.Argument(None, nargs=2),
# ):

#     if not user:
#         typer.echo("No provided users")
#         raise typer.Abort()
#     for u in user:
#         typer.echo(f"Processing user: {u}")

#     R = Runner(path, path_out=path_out)
#     R.run()
