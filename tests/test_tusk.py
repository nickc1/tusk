import os

from tusk import __version__
from tusk import Runner


def test_version():
    assert __version__ == "0.1.0"


def test_runner_pass():
    f = os.path.join(os.path.dirname(__file__), "test_tusk", "script_pass.py")
    # f = "test_scripts/script_pass.py"
    R = Runner(f)
    R.run()


def test_runner_fail():
    # f = "test_scripts/script_fail.py"
    f = os.path.join(os.path.dirname(__file__), "test_tusk", "script_fail.py")
    R = Runner(f)
    R.run()
