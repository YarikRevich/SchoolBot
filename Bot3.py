import telebot

from telebot import types 

bot = telebot.TeleBot("1044027580:AAG7DJy4lSpwA_wU7SMIqzgl0RayAAQRx6w")

@bot.message_handler(commands=["start"])


def welcome(message):	

	bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nМожеш скидувати д/з\nЯкщо хочеш подивитися інформація про бота напиши команду /info".format(message.from_user, bot.get_me()),
	parse_mode = "html")	
		
@bot.message_handler(commands=["info"])

def info(message):
	bot.send_message(message.chat.id, "Цей бот був створений для підтримки роботи бота @ddomashaa_bot,спеціально створеного для класу 9-А школи ЗК МГА\nБот був створений учнем 9-А класу Світлицьким Ярославом")


@bot.message_handler(content_types=["text"])


def mess(message):
	with open("work.txt", "w") as file:
		 	file.write(message.text)
	with open("work.txt", "r") as file:
			l = file.read()
	if message.text in l:
		bot.send_message(message.chat.id, "Дякую,домашнє завдання записане")

bot.polling(none_stop = True)

