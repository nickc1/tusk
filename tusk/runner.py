import runpy
from datetime import datetime
import traceback
from .slack import Slack
import papermill


class Runner:
    def __init__(self, path, path_out=None, parameters=None):
        self.path = path
        self.path_out = None
        self.parameters = None
        self.parse_extension()

    def parse_extension(self):
        ext = self.path.split(".")[-1]
        if ext == "ipynb":
            self.extension = "notebook"
        else:
            self.extension = "script"

    def run(self):

        start_time = datetime.now()
        print(f"TUSK: Starting at {start_time} run of: \n{self.path}\n")

        try:
            if self.extension == "notebook":
                papermill.execute_notebook(
                    self.path, self.path_out, parameters=self.parameters
                )
            else:
                runpy.run_path(self.path)

        except Exception:

            error = traceback.format_exc()
            print(f"ERROR IN: \n {self.path}")

            # send message
            end_time = datetime.now()

            S = Slack()
            S.add_error_block(self.path, error, start_time, end_time)
            S.make_post()

        end = datetime.now()
        print(f"TUSK: Finished at {end}")
