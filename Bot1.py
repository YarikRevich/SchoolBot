import telebot
import datetime
from telebot import types 

bot = telebot.TeleBot("1030049622:AAHkF1VMYj8kB0WFGu6iogFs7L6XkrwON9M")
#Реакція на команду /start

@bot.message_handler(commands=["start"])



def welcome(message):
	with open("people.txt","a") as file:
			file.write("\n""{0.first_name}".format(message.from_user, bot.get_me()) + "-" + "{0.id}".format(message.from_user, bot.get_me())+ " " + "натиснув(ла) start" + " " + "о" + " " + datetime.datetime.fromtimestamp(int(message.date)).strftime("%Y-%m-%d %H:%M:%S"))


	#Створення клавіатури

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	thing1 = types.KeyboardButton("/login")
	thing2 = types.KeyboardButton("/info")
	thing3 = types.KeyboardButton("/review")
	
	markup.add(thing1, thing2, thing3)

	#Надсилання повідомлення як реакції на команду /start

	bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nХочеш отримати Д/З за минулий день?\nТоді натисніть кнопку\n/login\nДля того щоб подивитися інформацію про бота натисніть кнопку\n/info\nДля того щоб залишити відгук натисніть\n/review".format(message.from_user, bot.get_me()),	
		parse_mode="html", reply_markup=markup)

#Реакція на команду "info"

@bot.message_handler(commands=["info"])

def info(message):
	with open("people.txt","a") as file:
			file.write("\n""{0.first_name}".format(message.from_user, bot.get_me()) + "-" + "{0.id}".format(message.from_user, bot.get_me())+ " " + "натиснув(ла) info")

	bot.send_message(message.chat.id, "Цей бот був створений для надсилання домашнього завдання дітям 9-А класу школи ЗК МГА\nБот був створений учнем 9-А класу Світлицьким Ярославом")



#Реакція на команду "/login"

@bot.message_handler(commands=["login"])

#Перевірка наявності id користувача у базі данних

def UserID(message):
	with open("people.txt","a") as file:
			file.write("\n""{0.first_name}".format(message.from_user, bot.get_me()) + "-" + "{0.id}".format(message.from_user, bot.get_me())+ " " + "натиснув(ла) login")

	bot.send_message(message.chat.id, "{0.id}".format(message.from_user, bot.get_me()))

	#Якщо id користувача є у базі данних тоді бот надійшле повідомлення з домашнім завданням,а якщо ні тоді бот надішле відповідне повідомлення

	m = "{0.id}".format(message.from_user, bot.get_me())
	f = open("Log.txt", "r")
	l = f.read()			 	
	if m in l:
		bot.send_message(message.chat.id, "Вітаю ти можеш забрати свою домашку!".format(message.from_user,bot.get_me()),parse_mode= "html")
		with open("work.txt", 'r') as file:
				 w = file.read()
		bot.send_message(message.chat.id, w, parse_mode = "html")
		bot.send_message(message.chat.id, "Для того,щоб знову подивитися домашнє завдання можеш натиснути \n/login")

	else:
		bot.send_message(message.chat.id,"Ти не був відсутній")

 #Реакція бота на команду "review"

@bot.message_handler(commands=["review"])

 #Утворення інлайн клавіатури

def review(message):
	with open("people.txt","a") as file:
			file.write("\n""{0.first_name}".format(message.from_user, bot.get_me()) + "-" + "{0.id}".format(message.from_user, bot.get_me())+ " " + "натиснув(ла) review")

	markup = types.InlineKeyboardMarkup(row_width=5)
	stuff1 = types.InlineKeyboardButton("5", callback_data="5")
	stuff2 = types.InlineKeyboardButton("4", callback_data="4")
	stuff3 = types.InlineKeyboardButton("3", callback_data="3")
	stuff4 = types.InlineKeyboardButton("2", callback_data="2")
	stuff5 = types.InlineKeyboardButton("1", callback_data="1")
	stuff6 = types.InlineKeyboardButton("Написати власний відгук", callback_data="Написати власний відгук")
	
	markup.add(stuff1, stuff2, stuff3, stuff4, stuff5, stuff6)

	bot.send_message(message.chat.id,"Можете поставити оцінку нашому боту,по 5-ти бальній шкалі,або написати власний відгук", reply_markup=markup)


  #Реакції на натискання кнопок в інлайн клавіатурі

@bot.callback_query_handler(func=lambda call: True)

def call_back(call):
	if call.message:

		#Реакція на натискання кнопки "5"

		if call.data == "5":
			bot.send_message(call.message.chat.id, "Дякую,ми будемо покращувати роботу бота")
			bot.send_message(call.message.chat.id, "Для отримання домашнього завдання натисніть кнопку\n/login\nДля того щоб подивитися інформацію про бота натисніть\n/info")
			with open("review.txt", "a") as file:
				h = file.write("\n""{0.first_name}".format(call.from_user,bot.get_me())+ ":" + "5")
		
		#Реакція на натискання кнопки "4"

		if call.data == "4":
			bot.send_message(call.message.chat.id, "Дякую,ми будемо покращувати роботу бота")
			bot.send_message(call.message.chat.id, "Для отримання домашнього завдання натисніть кнопку\n/login\nДля того щоб подивитися інформацію про бота натисніть\n/info")
			with open("review.txt", "a") as file:
				h = file.write("\n""{0.first_name}".format(call.from_user,bot.get_me())+ ":" + "4")

		#Реакція на натискання кнопки "3"
 
		if call.data == "3":
			bot.send_message(call.message.chat.id, "Дякую,ми будемо покращувати роботу бота")
			bot.send_message(call.message.chat.id, "Для отримання домашнього завдання натисніть кнопку\n/login\nДля того щоб подивитися інформацію про бота натисніть\n/info")
			with open("review.txt", "a") as file:
				h = file.write("\n""{0.first_name}".format(call.from_user,bot.get_me())+ ":" + "3")

		#Реакція на натискання кнопки "2"

		if call.data == "2":
			bot.send_message(call.message.chat.id, "Дякую,ми будемо покращувати роботу бота")
			bot.send_message(call.message.chat.id, "Для отримання домашнього завдання натисніть кнопку\n/login\nДля того щоб подивитися інформацію про бота натисніть\n/info")
			with open("review.txt", "a") as file:
				h = file.write("\n""{0.first_name}".format(call.from_user,bot.get_me())+ ":" + "2")

		#Реакція на натискання кнопки "1"

		if call.data == "1":
			bot.send_message(call.message.chat.id, "Дякую,ми будемо покращувати роботу бота")
			bot.send_message(call.message.chat.id, "Для отримання домашнього завдання натисніть кнопку\n/login\nДля того щоб подивитися інформацію про бота натисніть\n/info")
			with open("review.txt", "a") as file:
				h = file.write("\n""{0.first_name}".format(call.from_user,bot.get_me())+ ":" + "1")

		#Реакція на натискання кнопки "Написати власний відгук"

		if call.data == "Написати власний відгук":
			msg = bot.send_message(call.message.chat.id, "Напишіть ваші враження від користування нашим ботом!")
			bot.register_next_step_handler(msg,answer)


#Запис відгуку користувача записується у файл.Далі бот перевіряє файл,якщо відгук є у файлі,то бот виводить відповідне повідомлення 

def answer(message):

	with open("review.txt", "a") as file:
			h = file.write("\n""{0.first_name}".format(message.from_user,bot.get_me())+ ":" + message.text)
	with open("review.txt", "r") as file:
			r = file.read()
	if message.text in r:
		bot.send_message(message.chat.id, "Дякую,ваш відгук записано")
		bot.send_message(message.chat.id, "Для отримання домашнього завдання натисніть кнопку\n/login\nДля того щоб подивитися інформацію про бота натисніть\n/info")





bot.polling(none_stop = True)