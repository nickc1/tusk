import os
import json
import requests

# class SlackMessage:
#     def __init__(self):
#         self.message = dict(blocks=[])

#     def add_markdown_block(self, text):

#         block = dict(type="section", text=dict(type="mrkdwn", text=text))
#         self.message["blocks"].append(block)

#     def add_success_block(self, path, start_time, end_time):
#         elapsed = end_time - start_time

#         msg = f"""
#         :heavy_check_mark: SUCCESSFUL RUN {path}
#         *Start Time*: {start_time}
#         *End Time*: {end_time}
#         *Run Time*: {elapsed}
#         """

#         self.add_markdown_block(msg)

#     def add_error_block(self, path, start_time, end_time):
#         elapsed = end_time - start_time

#         msg = f"""
#         :x: *ERROR IN {path}*
#         *Start Time*: {start_time}
#         *End time*: {end_time}
#         *Run Time*: {elapsed}
#         """

#         self.add_markdown_block(msg)


class Slack:
    def __init__(self, url=None):
        self.message = dict(blocks=[])

        if url is None:
            url = os.environ.get("TUSK_SLACK_URL")
        self.url = url

    def add_markdown_block(self, text):

        block = dict(type="section", text=dict(type="mrkdwn", text=text))
        self.message["blocks"].append(block)

    def add_success_block(self, path, start_time, end_time):
        elapsed = end_time - start_time

        msg = f"""
        :heavy_check_mark: *SUCCESSFUL RUN:* {path}
        *Start Time*: {start_time}
        *End Time*: {end_time}
        *Run Time*: {elapsed}
        """

        self.add_markdown_block(msg)

    def add_error_block(self, path, start_time, end_time):
        elapsed = end_time - start_time

        msg = f"""
        :x: *ERROR IN {path}*
        *Start Time*: {start_time}
        *End time*: {end_time}
        *Run Time*: {elapsed}
        """

        self.add_markdown_block(msg)

    def make_post(self):
        headers = {"Content-type": "application/json"}
        msg = json.dumps(self.message)
        resp = requests.post(self.url, data=msg, headers=headers)
        return resp
