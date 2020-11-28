from tusk.slack import SlackMessage, Slack


def test_slack():
    text = (
        "This is a mrkdwn section block :ghost: *this is bold*,"
        "and ~this is crossed out~, and <https://google.com|this is a link>"
    )
    SM = SlackMessage()
    SM.add_markdown_block(text)

    slack = Slack()
    slack.make_post(SM.message)
