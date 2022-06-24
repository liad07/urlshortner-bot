from telegram.ext import *
import resposnses as Res

print("Bot started")
def start_command(update, context):
    update.message.reply_text('enter link')
def handle_message(update, context):
    text = str(update.message.text).lower()
    resposnses = Res.sample_res(text)
    update.message.reply_text(resposnses)

def main():
    updater = Updater("5478152172:AAGtty4JGhmzVKAr8b534o__0l7UWBF6F7k", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()


main()