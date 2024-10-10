import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Replace with your actual bot token
bot_token = '7601061325:AAGlclgJOe1t4oP63T5JBla3IpvCqYX8hkA'

# Initialize the bot using ApplicationBuilder
app = ApplicationBuilder().token(bot_token).build()

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create the message
    message = (
        "Hi there!\n"
        "This is a new bot made for sharing files that includes lessons and exams for English students.\n"
        "I hope you enjoy <3"
    )
    
    # Create a button
    keyboard = [
        [InlineKeyboardButton("Developer account", url="https://www.facebook.com/profile.php?id=100074209436216")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the message with the button
    await update.message.reply_text(message, reply_markup=reply_markup)

# Function to handle the /sendpdf command
async def send_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("Received /sendpdf command.")
    
    # Path to the folder containing the PDF files
    folder_path = r'C:\Users\Administrator\Pictures\botis'
    
    # Get a list of PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    if not pdf_files:
        await update.message.reply_text("No PDF files found.")
        return

    chat_id = update.effective_chat.id

    # Send each PDF file
    for pdf_file in pdf_files:
        file_path = os.path.join(folder_path, pdf_file)
        try:
            await context.bot.send_document(chat_id=chat_id, document=open(file_path, 'rb'))
            logging.info(f"Sent PDF: {pdf_file}")
        except Exception as e:
            logging.error(f"Error sending PDF {pdf_file}: {e}")
    
    await update.message.reply_text(f"Sent {len(pdf_files)} PDF files.")

# Add command handlers for /start and /sendpdf
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('sendpdf', send_pdf))

# Start the bot
app.run_polling()
