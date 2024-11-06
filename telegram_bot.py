from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Define a function to respond to the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Create an inline button for joining
    keyboard = [
        [InlineKeyboardButton("Join our community", callback_data="join_link")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the /start message with the button
    await update.message.reply_text(
        "Hello! I’m your new Telegram bot. How can I help you today?",
        reply_markup=reply_markup
    )

# Define a function to handle the button press
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the button press

    # Check if the callback data is "join_link"
    if query.data == "join_link":
        join_link = "https://t.me/DiwaliRewardsBot?start=5668614247"  # Replace with your actual join link
        await query.edit_message_text(
            text=f"Join our community here: {join_link}"
        )

def main():
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    application = Application.builder().token("7492642687:AAFmhu5QkubmUf5OsuQmhmbLxiP6qiILqXk").build()

    # Register the start command handler
    application.add_handler(CommandHandler("start", start))

    # Register the button press handler
    application.add_handler(CallbackQueryHandler(button))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
