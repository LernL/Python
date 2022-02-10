#5250766987:AAG_AFUmbHY9Gf8PNYSGIdvrg2-v-fGm1bc
import telebot
from telebot import types

bot = telebot.TeleBot("5250766987:AAG_AFUmbHY9Gf8PNYSGIdvrg2-v-fGm1bc", parse_mode=None)

name=""
surname=""
age=0

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, f"Hello,{message.from_user.first_name} {message.from_user.last_name}. I'm your personal bot.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	#bot.reply_to(message, message.text)
    if message.text=="Hello" or message.text=="hello":
        bot.reply_to(message, "Hi!")
    elif message.text == '/reg':
        # bot.reply_to(message,f"Name: {message.from_user.first_name}" )
        # bot.reply_to(message, f"Surname: {message.from_user.last_name}")
        # bot.reply_to(message, f"Is it correct")
        bot.send_message(message.from_user.id,"Hello,let is get acquainted\n What's your name?")
        bot.register_next_step_handler(message,register_name)
    else:
        bot.reply_to(message, "Invalid value")
def register_name(message):
    bot.send_message(message.from_user.id,"What's your surname?")
    global name
    name=message.text
    bot.register_next_step_handler(message, register_surname)
    # bot.reply_to(message,"What is your name?:")
def register_surname(message):
    bot.send_message(message.from_user.id,"How old are you?")
    global surname
    surname=message.text
    bot.register_next_step_handler(message, register_age)
def register_age(message):
    # while True:
    global age
    #     if age==0:
    #         age=int(message.text)
    #         break
    #     else:
    #         bot.send_message(message.from_user.id, "Write in numbers")
    while age==0:
        try:
            age = int(message.text)
            #bot.send_message(message.from_user.id, age)
        except Exception:
            bot.send_message(message.from_user.id, "Write numbers")
    a=f"Тебе {age}, тебя зовут {name} {surname}. It's true?"
    #bot.send_message(message.from_user.id, a)
    keyboard = types.InlineKeyboardMarkup()
    keyboard_yes = types.InlineKeyboardButton(text="Yes",callback_data='yes')
    #keyboard.add(keyboard_yes)
    keyboard_no = types.InlineKeyboardButton(text="No",callback_data="no")
    keyboard.add(keyboard_no,keyboard_yes)
    bot.send_message(message.from_user.id, text=a, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def check(call):
    if call.data=='yes':
        bot.send_message(call.message.chat.id, "Okay, I'm writed this information")
    else:
        bot.send_message(call.message.chat.id, "Try again")
        bot.register_next_step_handler(call.message, register_name)
bot.infinity_polling()
