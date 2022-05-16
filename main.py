from logging import error
import telegram.ext as telegram_bot
import src.functions as funcs
import credentials

print("Starting...")

updater = telegram_bot.Updater(credentials.TOKEN, use_context=True)

updater.dispatcher.add_handler(telegram_bot.CommandHandler("start", funcs.start))
updater.dispatcher.add_handler(telegram_bot.CommandHandler("help", funcs.help_me))
updater.dispatcher.add_handler(telegram_bot.CommandHandler("time", funcs.time))
updater.dispatcher.add_handler(
    telegram_bot.CommandHandler("hacktoberfest", funcs.hacktoberfest)
)

updater.dispatcher.add_error_handler(error)
updater.start_polling()
updater.idle()

print("Exiting...")
