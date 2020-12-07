import runpy
from datetime import datetime
import traceback
import typer
from .slack import Slack

app = typer.Typer()


@app.command()
def something(path: str):

    start_time = datetime.now()
    typer.echo(f"TUSK: Starting at {start_time} run of: \n{path}\n")

    try:
        runpy.run_path(path)
        print("It ran")

    except Exception:

        error = traceback.format_exc()
        typer.echo(f"ERROR IN: \n {error}")

        # send message
        end_time = datetime.now()
        S = Slack()
        S.add_error_block(path, start_time, end_time)
        S.make_post()

    end = datetime.now()
    typer.echo(f"TUSK: Finished at {end}")
