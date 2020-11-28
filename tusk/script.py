import runpy
from datetime import datetime
import traceback


class Runner:
    def __init__(self, path, out_path=None):
        self.path = path
        self.out_path = None
        self.parse_extension()

    def parse_extension(self, path):
        ext = path.split(".")[-1]
        if ext == "ipynb":
            self.extension = "notebook"
        else:
            self.extension = "script"

    def run_script(self):

        try:
            runpy.run_path(path)

        except Exception:

            error = traceback.format_exc()
            return error

    def run_notebook(self, parameters):
        """Execute notebook.
        Args:
            parameters (dict): parameters to be injected into notebook
        """

        try:
            papermill.execute_notebook(
                "path/to/input.ipynb", "path/to/output.ipynb", parameters=parameters
            )
        except Exception:
            error = traceback.format_exc()
            return error
