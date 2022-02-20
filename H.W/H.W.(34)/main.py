#5250766987:AAG_AFUmbHY9Gf8PNYSGIdvrg2-v-fGm1bc
import telebot

bot = telebot.TeleBot("5250766987:AAG_AFUmbHY9Gf8PNYSGIdvrg2-v-fGm1bc", parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f"Hello,{message.from_user.first_name} {message.from_user.last_name}. I'm your personal bot.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	#bot.reply_to(message, message.text)
    if message.text=="Hello" or message.text=="hello":
        bot.reply_to(message, "Hi!")
    elif message.text == "How are you?":
        bot.reply_to(message, "I'm fine, thanks!:)")
    elif message.text == "/help":
        bot.reply_to(message, f"You can write:\n'Hello' or 'hello'\n'How are you?'\n '/help'")
    else:
        bot.reply_to(message, "Invalid value")
bot.infinity_polling()