import telebot

# Your bot token from BotFather
TOKEN = '7828202547:AAE3ceQOGolsRek0mHg0ZgO_i5zR1jv8DIw'

# Create the bot object
bot = telebot.TeleBot(TOKEN)

# When someone sends /start, reply with welcome message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به قرعه‌کشی خوش آمدی 🎉 برای خرید اعتبار یا شرکت در قرعه‌کشی دکمه‌های پایین رو بزن!")

# Start the bot
bot.polling()
