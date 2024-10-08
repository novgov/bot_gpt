#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import shelve

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    user_id = user.id
    user_name = user.full_name
    pandora = shelve.open("pandora")
    if str(user_id) not in pandora.keys():
        user_data = {
            "user_name": user_name,
            "subs": "Free",
            "tokens": 0
        }
        pandora[str(user_id)] = user_data
    await update.message.reply_text(f"Добро пожаловать в GPT бота! {pandora[str(user_id)]["user_name"]}")
    pandora.close()

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = str(user.id)
    pandora = shelve.open("pandora")
    subscription_type = pandora[str(user_id)]["subs"]
    tokens = pandora[str(user_id)]['tokens']
    name = pandora[str(user_id)]['user_name']
    profile_text = (
        f"Это ваш профиль. 🫠\n"
        f"Имя: {name}.\n"
        f"ID: {user_id}\n"
        f"Подписка: {subscription_type}\n\n"
        f"Лимиты: {tokens} token"
    )
    await update.message.reply_text(profile_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "Для покупи токенов /store \n"
        "Для просмотра информации о вашем аккаунте /profile \n"
        "Для смены модели GPT /mode \n"
    )
    await update.message.reply_text(help_text)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    """Echo the user message."""
    await update.message.reply_text(int(message) + 2)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7914691283:AAEf7gVCqyonBrUHCo57b9sUEpBxD4eFXWE").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("profile", profile))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()


