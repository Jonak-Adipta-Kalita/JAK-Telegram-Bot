import telegram.ext as telegram_bot
import credentials

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

    /start -> Start the Bot
    /help  -> See full List of Cammands
"""
    )


updater = telegram_bot.Updater(credentials.TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram_bot.CommandHandler("start", start))
disp.add_handler(telegram_bot.CommandHandler("help", help_me))

updater.start_polling()
updater.idle()
