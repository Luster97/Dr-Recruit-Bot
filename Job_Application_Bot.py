import logging
import os
import spacy
nlp = spacy.load("en_core_web_sm")
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
from handlers.nlp_handlers import analyze_job_description, analyze_resume

load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("7508331357:AAHXPrO1dqwJPXz3-rrmd_JPzSYLqd24J1Q")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! 👋\nI'm your Job Application Assistant Bot.\n\n"
        "Send me a job description or resume text and I’ll help analyze it for you!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send help message."""
    await update.message.reply_text("Send me:\n- A job description to analyze keywords.\n"
                                    "- A resume snippet to compare against a job description.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming text."""
    text = update.message.text

    if "responsibilities" in text.lower() or "qualifications" in text.lower():
        result = analyze_job_description(text)
    else:
        result = analyze_resume(text)

    await update.message.reply_text(result)

def main() -> None:
    """Start the bot."""
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    application.run_polling()

if __name__ == "__main__":
    main()
