import runpy
from datetime import datetime
import traceback
import typer

app = typer.Typer()


@app.command()
def something(path: str):

    start = datetime.now()
    typer.echo(f"TUSK: Starting at {start} run of: \n{path}\n")

    try:
        runpy.run_path(path)
        print("It ran")

    except Exception:

        error = traceback.format_exc()
        typer.echo(f"ERROR IN: \n {error}")

        # send message
        subject = "ERROR - {}".format(path.split("/")[-1])
        Slack(subject, start_time, error_time)

    end = datetime.now()
    typer.echo(f"TUSK: Finished at {end}")
