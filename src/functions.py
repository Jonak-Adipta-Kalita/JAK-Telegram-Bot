import datetime, telegram
import src.keyboard_buttons as keyboard_buttons


def start(update: telegram.Update, context):
    update.message.reply_text(
        "Made by JAK aka Jonak Adipta Kalita\n/help -> See Full Commands List"
    )


def help_me(update: telegram.Update, context):
    update.message.reply_text(
        "Full Commands List:\n\n/start -> Start the Bot\n/help -> See full List of Commands\n/time -> See the Current Time\n/hacktoberfest -> Check out about Hacktoberfest"
    )


def time(update: telegram.Update, context):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    update.message.reply_text(f"The Current Time is: {current_time}")


def hacktoberfest(update, context):
    update.message.reply_text(
        "Hacktoberfest encourages participation in the open source community, which grows bigger every year. Complete the 2021 challenge and earn a limited edition T-shirt.\nAnd also this bot is included in Hacktoberfest eligibal Repositories. For more information check the urls below.",
        reply_markup=keyboard_buttons.hacktoberfest(),
    )
