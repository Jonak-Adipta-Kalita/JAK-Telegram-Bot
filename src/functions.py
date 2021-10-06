import datetime
import webbrowser


def start(update, context):
    update.message.reply_text(
        r"""
    Made by JAK aka Jonak Adipta Kalita

    /help -> See Full Commands List
"""
    )


def help_me(update, context):
    update.message.reply_text(
        r"""
    Full Commands List:

    /start -> Start the Bot
    /help -> See full List of Commands
    /time -> See the Current Time
    /repo -> Go to this Bot's repository
    /hacktoberfest -> See information about Hacktoberfest
"""
    )


def time(update, context):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    update.message.reply_text(f"The Current Time is: {current_time}")


def hacktoberfest(update, context):
    webbrowser.open("https://hacktoberfest.digitalocean.com/")
    update.message.reply_text(
        r"""
    Hacktoberfest encourages participation in the open source community, which grows bigger every year. Complete the 2021 challenge and earn a limited edition T-Shirt.
And also this bot is included in Hacktoberfest Repositories!!

/repo -> Go to this Bot's Repository
"""
    )


def repo(update, context):
    webbrowser.open("https://github.com/Jonak-Adipta-Kalita/JAK-Telegram-Bot")
    update.message.reply_text("Opening Bot's repository.")
