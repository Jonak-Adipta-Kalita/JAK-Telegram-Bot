import telegram.ext as telegram_bot
import credentials, functions

updater = telegram_bot.Updater(credentials.TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram_bot.CommandHandler("start", functions.start))
disp.add_handler(telegram_bot.CommandHandler("help", functions.help_me))
disp.add_handler(telegram_bot.CommandHandler("time", functions.time))

updater.start_polling()
updater.idle()
