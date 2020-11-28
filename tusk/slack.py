import os
import json
import requests

error_msg = """
:x: *ERROR IN {PATH}*
*Start Time*: {START_TIME}
*End time*: {END_TIME}
*Run Time*: {ELAPSED} seconds
"""

success_msg = """
:heavy_check_mark: SUCCESSFUL RUN {PATH}
*Start Time*: {START_TIME}
*End Time*: {END_TIME}
*Run Time*: {ELAPSED} seconds
"""


class SlackMessage:
    def __init__(self):
        self.message = dict(blocks=[])

    def add_markdown_block(self, text):

        block = dict(type="section", text=dict(type="mrkdwn", text=text))
        self.message["blocks"].append(block)

    def add_success_block(self, path, start_time, end_time):
        elapsed = end_time - start_time
        msg = succuss_msg.format(
            PATH=path, START_TIME=start_time, END_TIME=end_time, ELAPSED=elapsed
        )
        self.add_markdown_block(msg)

    def add_error_block(self, path, start_time, end_time):
        elapsed = end_time - start_time
        msg = error_msg.format(
            PATH=path, START_TIME=start_time, END_TIME=end_time, ELAPSED=elapsed
        )
        self.add_markdown_block(msg)


class Slack:
    def __init__(self, url=None):

        if url is None:
            url = os.environ.get("TUSK_SLACK_URL")
        self.url = url

    def make_post(self, message):
        headers = {"Content-type: application/json"}
        message = json.dumps(message)
        resp = requests.post(self.url, data=message)
        return resp
