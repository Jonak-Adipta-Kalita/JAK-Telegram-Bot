import webbrowser, datetime


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
    /help -> See full List of Cammands
    /website -> Open JAK's Website
    /api -> Open JAK's API's Website
    /discord_bot -> Open JAK's Discord Bot Invite Link
    /time -> See the Current Time
"""
    )


def website(update, context):
    update.message.reply_text("Opening JAK's Website!!")
    webbrowser.open("https://jonakadiptakalita.herokuapp.com/")


def api(update, context):
    update.message.reply_text("Opening JAK's API's Website!!")
    webbrowser.open("https://jak-api-dot-com.herokuapp.com/")


def discord_bot(update, context):
    update.message.reply_text("Opening JAK's Discord Bot Invite Link!!")
    webbrowser.open(
        "https://discord.com/oauth2/authorize?client_id=756402881913028689&scope=bot"
    )


def time(update, context):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    update.message.reply_text(f"The Current Time is: {current_time}")
