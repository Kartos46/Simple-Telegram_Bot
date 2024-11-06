from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Define a function to respond to the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I’m your new Telegram bot. How can I help you today?")

# Define a function to respond to the /join command
async def join(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    join_link = "YOUR_JOIN_LINK_HERE"  # Replace with your actual join link
    await update.message.reply_text(f"Join our community here: {join_link}")

def main():
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    application = Application.builder().token("YOUR_TOKEN_HERE").build()

    # Register the start command handler
    application.add_handler(CommandHandler("start", start))

    # Register the join command handler
    application.add_handler(CommandHandler("join", join))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
