import datetime
from tusk.slack import Slack


def test_slack():
    text = (
        "This is a mrkdwn section block :ghost: *this is bold*,"
        "and ~this is crossed out~, and <https://google.com|this is a link>"
    )
    S = Slack()
    S.add_markdown_block(text)
    S.make_post()

    path = "my/path/to/myscript.py"
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(minutes=3, seconds=22)

    S = Slack()
    S.add_error_block(path, start_time, end_time)
    S.make_post()

    S = Slack()
    S.add_success_block(path, start_time, end_time)
    S.make_post()
