import telebot

from telebot import types 

bot = telebot.TeleBot("1039871774:AAF1Rx_3hxo805E_KI4-NpIobsosNTOq_1A")

    #Реакція на команду "start"
@bot.message_handler(commands=["start"])
	     
def wel(message):
	
	#Створення клавіатури 

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	thing3 = types.KeyboardButton("/write")
	thing4 = types.KeyboardButton("/info")
		
	markup.add(thing3,thing4)

	#Бот надсилає повідомлення при створенні клавіатури

	bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nДля того щоб записати відсутніх\n натисніть кнопку\n/write".format(message.from_user, bot.get_me()),	
		parse_mode="html", reply_markup=markup)
	bot.send_message(message.chat.id, "✅Правила роботи з ботом:\n1️⃣Запис відсутніх здійснюється за допомогою натискання кнопок з прізвищами відсутніх\n2️⃣Перед натискання кнопок з відсутніми для їхнього запису у базу данних треба натиснути на кнопку /clean \nУдачного запису😊 ".format(message.from_user, bot.get_me()),parse_mode="html")



    #Реакція на команду "info"

@bot.message_handler(commands=["info"])

def info(message):
		bot.send_message(message.chat.id, "Цей бот був створений для підтримки роботи бота @ddomashaa_bot,спеціально створеного для класу 9-А школи ЗК МГА\nБот був створений учнем 9-А класу Світлицьким Ярославом")


    #Реакція на команду "write"

@bot.message_handler(commands=["write"])

    #Створення клавіатури

def mess(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	clean = types.KeyboardButton("/clean")
	surname1 = types.KeyboardButton("Акулініна")
	surname2 = types.KeyboardButton("Болжоларська")
	surname3 = types.KeyboardButton("Бохова")
	surname4 = types.KeyboardButton("Величко")
	surname5 = types.KeyboardButton("Вітценко")
	surname6 = types.KeyboardButton("Верміяш")
	surname7 = types.KeyboardButton("Василенко")
	surname8 = types.KeyboardButton("Гуцол")
	surname9 = types.KeyboardButton("Єфремова")
	surname10 = types.KeyboardButton("Зубов")
	surname11 = types.KeyboardButton("Ілларіонов")
	surname12 = types.KeyboardButton("Івахно")
	surname13 = types.KeyboardButton("Карталова")
	surname14 = types.KeyboardButton("Кайдаш")
	surname15 = types.KeyboardButton("Козакова")
	surname16 = types.KeyboardButton("Коробов")
	surname17 = types.KeyboardButton("Кошовець")
	surname18 = types.KeyboardButton("Коплік")
	surname19 = types.KeyboardButton("Кадігроб")
	surname20 = types.KeyboardButton("Мунтян")
	surname21 = types.KeyboardButton("Міхайленко")
	surname22 = types.KeyboardButton("Маргелов")
	surname23 = types.KeyboardButton("Пуцько")
	surname24 = types.KeyboardButton("Слива")
	surname25 = types.KeyboardButton("Савчук")
	surname26 = types.KeyboardButton("Самонін")
	surname27 = types.KeyboardButton("Світлицький")
	surname28 = types.KeyboardButton("Скорікова")
	surname29 = types.KeyboardButton("Труфанов")
	surname30 = types.KeyboardButton("Уткіна")
	surname31 = types.KeyboardButton("Шевченко")
	surname32 = types.KeyboardButton("Шустер")
	surname33 = types.KeyboardButton("Яковенко")


	markup.add(clean,surname1,surname2,surname3,surname4,surname5,surname6,surname7,surname8,surname9,surname10,surname11,surname12,surname13,surname14,surname15,surname16,surname17,surname18,surname19,surname20,surname21,surname22,surname23,surname24,surname25,surname26,surname27,surname28,surname29,surname30,surname31,surname32,surname33)

    #Бот надсилає повідомлення після створення клавіатури

	bot.send_message(message.chat.id, "{0.first_name},можеш вибрати відсутніх".format(message.from_user, bot.get_me()),parse_mode = "html",reply_markup=markup)

        #Реакції на натискання кнопок клавіатури

@bot.message_handler(content_types=['text'])
def mass(message):
	if message.text == ("/clean"):
		with open("Log.txt", "w") as file:
				file.write(" ")
		bot.send_message(message.chat.id, "База данних очищена,можете записувати відсутніх")

        #Реакція на натискання кнопки "Акулініна"

	if message.text == ("Акулініна"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Акулініна" + ":" + "780259389")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Болжоларська"


	if message.text == ("Болжоларська"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Болжоларська" + ":" + "741005234")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Бохова"

	if message.text == ("Бохова"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Бохова" + ":" +"860113568")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")


		#Реакція на натискання кнопки "Величко"

	if message.text == ("Величко"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Величко" + ":" + "544781298")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")


        #Реакція на натискання кнопки "Вітценко"
 
	if message.text == ("Вітценко"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Вітценко" + ":" + "900079974")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Верміяш"

	if message.text == ("Верміяш"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Верміяш" + ":" + "699436866")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Василенко"

	if message.text == ("Василенко"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Василенко" + ":" + "576160165")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

		#Реакція на натискання кнопки "Гуцол"
	if message.text == ("Гуцол"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Гуцол" + ":" + "710495288")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Зубов"

	if message.text == ("Зубов"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Зубов" + ":" + "489929608")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

         #Реакція на натискання кнопки "Ілларіонов"

	if message.text == ("Ілларіонов"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Ілларіонов" + ":" + "589316748")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

         #Реакція на натискання кнопки "Івахно"

	if message.text == ("Івахно"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Івахно" + ":" + "-")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Ця людина поки не зареєстрована у базі данних")

         #Реакція на натискання кнопки "Карталова"  

	if message.text == ("Карталова"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Карталова" + ":" + "483562090")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

         #Реакція на натискання кнопки "Козакова"

	if message.text == ("Козакова"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Козакова" + ":" + "650758107")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Коробов"

	if message.text == ("Коробов"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Коробов" + ":" + "-")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Ця людина поки не зареєстрована у базі данних")

        #Реакція на натискання кнопки "Кошовець"

	if message.text == ("Кошовець"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Кошовець" + ":" + "451640706")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Кадігроб"

	if message.text == ("Кадігроб"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Кадігроб" + ":" + "752699013")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Мунтян"

	if message.text == ("Мунтян"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Мунтян" + ":" + "833607700")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакця на натискання кнопки "Міхайленко"

	if message.text == ("Міхайленко"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Міхайленко" + ":" + "-") 
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Ця людина поки не зареєстрована у базі данних")
	
        #Реакція на натискання кнопки "Маргелов"

	if message.text == ("Маргелов"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Маргелов" + ":" + "793890709")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Пуцько"

	if message.text == ("Пуцько"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Пуцько" + ":" + "514767955")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Слива"

	if message.text == ("Слива"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Слива" + ":" + "782320937")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

		#Реакція на натискання кнопки "Савчук"

	if message.text == ("Савчук"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Савчук" + ":" + "636369899")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")


		#Реакція на натискання кнопки "Самонін"

	if message.text == ("Самонін"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Самонін" + ":" + "822418660")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Скорікова"

	if message.text == ("Скорікова"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Скорікова" + ":" + "-")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Цієї людина поки немає в базі данних")
	
        #Реакція на натискання кнопки "Світлицький"

	if message.text == ("Світлицький"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Світлицький" + ":" + "Власник бота")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Труфанов"

	if message.text == ("Труфанов"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Труфанов" + ":" + "-")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Цієї людина поки немає в базі данних")
	
        #Реакція на натискання кнопки "Уткіна"
          

	if message.text == ("Уткіна"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Уткіна" + ":" + "-")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Цієї людина поки немає в базі данних")
	
        
        #Реакція на натискання кнопки "Шевченко"

	if message.text == ("Шевченко"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Шевченко" + ":" + "691650372")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

        #Реакція на натискання кнопки "Яковенко"

	if message.text == ("Яковенко"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Яковенко" + ":" + "462432739")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")


        #Реакція  на натискання кнопки "Єфремова"

	if message.text == ("Єфремова"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Єфремова" + ":" + "604138063")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")

		#Реакція на натискання кнопки "Кайдаш"

	if message.text == ("Кайдаш"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Кайдаш" + ":" + "272097553")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")


        #Реакція на натискання кнопки "Коплік"

	if message.text == ("Коплік"):
		with open("Log.txt", "a") as file:
				file.write("\n" + "Коплік" + ":" + "669457493")
		with open("Log.txt", "r") as file:
				x = file.read()
		if message.text in x:
			bot.send_message(message.chat.id, "Дякую,прізвище записане")


bot.polling(none_stop = True)

