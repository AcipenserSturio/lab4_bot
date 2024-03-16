from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)

class Bot():
    def __init__(self, token: str):
        self.app = ApplicationBuilder().token(token).write_timeout(30).build()
        self.app.add_handler(CommandHandler("infer", infer))

async def infer(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
    message = await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = update.message.text,
    )


