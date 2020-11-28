# tusk

tusk makes it easy to:
- run python scripts and notebooks
- get notifications on failure
- log important statistics

To run a python script that sends a slack message on error:

```bash
tusk myscript.py --slack
```

Similary to run a python notebook:

```bash
tusk my-notebook.ipynb --slack
```

## Use Cases

tusk aims to bridge the gap between unmonitored or loosely monitored cron jobs and more robust solutions such as airflow or prefect. We wanted to make a tool that works out of the box without much configuration or setup.

## Installation

```bash
pip install tusk-runner
```

## Slack

To have errors or successful runs send notifications to slack, you must first set up a slack webhook and then set the `TUSK_SLACK_URL` environmental variable.
