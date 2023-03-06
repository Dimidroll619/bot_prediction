from datetime import datetime
import random
import prediction_database
import telebot
from telebot import types
from geopy import distance
token = "6113739504:AAFv4m6YVXeiLAxSN5NykRPuSNrhRlX5YYw"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.chat.first_name #Ім`я
    user = message.chat.id

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text = "Передбачення на день \U00002728")
    btn2 = types.KeyboardButton(text = "Випадкове передбачення\U0001F31F")
    btn3 = types.KeyboardButton(text = "Таймер\U000023F3")
    btn4 = types.KeyboardButton(text = "Відстань\U0001F4CF", request_location = True)
    btn5 = types.KeyboardButton(text = "Help\U0001F198")
    btn6 = types.KeyboardButton(text = "Цитата дня \U0001F4D3")
    
    keyboard.add(btn1, btn2, btn6, btn3, btn4, btn5)

    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBQ6RfR8r9OHxVZxEIik6XXRVYh5StpQACBAcAAkb7rARD2NYo4qk9gxsE")
    bot.send_message(message.chat.id, "І знову привіт, " + first_name + "! \nПро мій новий функціонал можна дізнатись у вкладці HELP", reply_markup=keyboard)
    bot.send_message(603699998, user)


@bot.message_handler(func=lambda message: message.text == "Передбачення на день \U00002728")
def day_prediction(message):
    now = datetime.now().strftime("%d.%m.%Y")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHhd9j2EPnJQST6s5VgAABNOdglR-GYHIAAgsAA_cXgSv-y3as0uIoSS0E")
    bot.send_message(message.chat.id, prediction_database.listd[now])

@bot.message_handler(func=lambda message: message.text == "Цитата дня \U0001F4D3")
def day_prediction(message):
    now = datetime.now().strftime("%d.%m.%Y")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEICM5kBnRlVOHJe8GHUe28JC8axqKgtwACVQADr8ZRGmTn_PAl6RC_LgQ")
    bot.send_message(message.chat.id, prediction_database.listq[now])

@bot.message_handler(func=lambda message: message.text == "Випадкове передбачення\U0001F31F")
def rand_prediction(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHheVj2EQ_EoxWA0dnPUgpa_4a3kVAbgACAwAD9xeBKzrS2wLjKk6XLQQ")
    bot.send_message(message.chat.id, random.choice(prediction_database.listr))


@bot.message_handler(func=lambda message: message.text == "Таймер\U000023F3")
def timer(message):
    date1 = datetime(2023, 4, 15)
    date2 = datetime.now()
    t = (date1 - date2).total_seconds()
    h = t//3600
    m = (t%3600)//60
    s = (t%3600)%60
    timer = "%d:%d:%d"%(h,m,s)
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvFdf7ymAmuyuQ2U0Y_yz9zAzhKInGwACDQADr8ZRGj7pvDy3DEgWHgQ")
    bot.send_message(message.chat.id, timer)


@bot.message_handler(func = lambda message: True, content_types = ["location"])
def location(message) :
    nestle = (49.80953396504598, 24.04561312739838)
    lon = message.location.longitude
    lat = message.location.latitude
    place = (lat, lon)
    distance1 = distance.great_circle(place, nestle).kilometers
    bot.send_message(message.chat.id, "Відстань до львіського офісу складає:"+ str(round(distance1, 2)) + " кілометрів.")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvdRf818dGfnlvYLCwfPcSPUaOo8-igACgQMAAm2wQgOxqAABZxcolQABHgQ")
    print(str(place))

@bot.message_handler(func=lambda message: message.text == "Help\U0001F198")
def help(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHhe1j2EWM8soc94yvIiI2y-8XqD0yMgAC-QYAAkb7rAQF5n-88vDa9S0E")
    bot.send_message(message.chat.id, "Наразі добавилась цитата дня, та передбачення продовжені до кінця року", parse_mode="HTML")


bot.polling()
