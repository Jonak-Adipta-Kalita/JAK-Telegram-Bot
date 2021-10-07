import datetime
from telegram import InlineKeyboardMarkup, bot
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton


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
    /hacktoberfest -> Check out about Hacktoberfest
"""
    )


def time(update, context):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    update.message.reply_text(f"The Current Time is: {current_time}")


def hacktoberfest(update, context):
    update.message.reply_text(
        """
        Hacktoberfest encourages participation in the open source community, which grows bigger every year. Complete the 2021 challenge and earn a limited edition
        T-shirt. And also this bot is included in Hacktoberfest repo. For more information check the url below.
        """,
        reply_markup=urlKeyboard(),
    )


def urlKeyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "Hacktoberfest", url="https://hacktoberfest.digitalocean.com/"
            )
        ],
        [
            InlineKeyboardButton(
                "Bot Repository",
                url="https://github.com/Jonak-Adipta-Kalita/JAK-Telegram-Bot",
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
