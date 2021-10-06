from logging import error
import telegram.ext as telegram_bot
import src.functions as funcs
import credentials

updater = telegram_bot.Updater(credentials.TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram_bot.CommandHandler("start", funcs.start))
disp.add_handler(telegram_bot.CommandHandler("help", funcs.help_me))
disp.add_handler(telegram_bot.CommandHandler("time", funcs.time))
disp.add_handler(
    telegram_bot.CommandHandler("abouthacktoberfest", funcs.abouthacktoberfest)
)
updater.dispatcher.add_error_handler(error)
updater.start_polling()
updater.idle()

print("Exiting...\n")
