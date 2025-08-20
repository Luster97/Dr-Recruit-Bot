from telegram.ext import Application, MessageHandler, filters

async def handler(update, context):
    await update.message.reply_text("You said: '{}'".format(update.message.text))


def main():
    application = Application.builder().token('"7508331357:AAHXPrO1dqwJPXz3-rrmd_JPzSYLqd24J1Q"').build()
    application.add_handler(MessageHandler(filters.TEXT, handler))
    application.run_polling()


if __name__ == '__main__':
    main()