from telegram import InlineKeyboardMarkup
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton


def hacktoberfest():
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
