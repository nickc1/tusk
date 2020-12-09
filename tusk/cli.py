import runpy
from datetime import datetime
import traceback
import typer
from .runner import Runner

app = typer.Typer()


@app.command(context_settings={"allow_extra_args": True})
def run(ctx: typer.Context, path: str, path_out: str = None):

    for extra_arg in ctx.args:
        typer.echo(f"Got extra arg: {extra_arg}")

    R = Runner(path, path_out=path_out)
    R.run()

    # start_time = datetime.now()
    # typer.echo(f"TUSK: Starting at {start_time} run of: \n{path}\n")

    # try:
    #     runpy.run_path(path)

    # except Exception:

    #     error = traceback.format_exc()
    #     typer.echo(f"ERROR IN: \n {error}")

    #     # send message
    #     end_time = datetime.now()
    #     S = Slack()
    #     S.add_error_block(path, start_time, end_time)
    #     S.make_post()

    # end = datetime.now()
    # typer.echo(f"TUSK: Finished at {end}")
