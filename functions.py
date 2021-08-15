import webbrowser


def start(update, context):
    update.message.reply_text(
        r"""
    Made by JAK

    /help -> See Full Commands List
"""
    )


def help_me(update, context):
    update.message.reply_text(
        r"""
    Full Commands List:

    /start   -> Start the Bot
    /help    -> See full List of Cammands
    /website -> Open JAK's Website
    /api     -> Open JAK's API's Website
"""
    )


def website(update, context):
    update.message.reply_text("Opening JAK's Website!!")
    webbrowser.open("https://jonakadiptakalita.herokuapp.com/")


def api(update, context):
    update.message.reply_text("Opening JAK's API's Website!!")
    webbrowser.open("https://jak-api-dot-com.herokuapp.com/")
