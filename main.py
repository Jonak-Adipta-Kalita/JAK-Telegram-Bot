import telegram.ext as telegram_bot
import src.functions as funcs
import credentials

updater = telegram_bot.Updater(credentials.TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram_bot.CommandHandler("start", funcs.start))
disp.add_handler(telegram_bot.CommandHandler("help", funcs.help_me))
disp.add_handler(telegram_bot.CommandHandler("time", funcs.time))

updater.start_polling()
updater.idle()

print("Exiting...\n")
