import telebot
from SimpleQIWI import *

TELEGRAM_TOKEN = '1947890605:AAHfVuQ1FUD1DkR7YE0VPkbj5ZyEnGyLOmQ' 					   # Создайте своего бота в @BotFather, скопируйте и вставьте токен
bot = telebot.TeleBot(TELEGRAM_TOKEN)


token = "agsgayy272vzbaj111"         						   # Создайте и вставьте свой токен https://qiwi.com/api
phone = '+7123123111'							   # Свой номер киви
api = QApi(token=token, phone=phone)

# КОД ВНИЗУ РЕДАКТИРОВАТЬ НЕ ЖЕЛАТЕЛЬНО

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, '⚙️ Выберите Действие:\n\n💰 Проверить баланс: /balance')

@bot.message_handler(commands=['balance'])
def balance(message):
	text_balance = '💰 Твой баланс: '+str(api.balance)
	bot.send_message(message.chat.id, text_balance)


bot.polling(none_stop=True)

# Если есть вопросы, или есть предложения - пишите в телеграмм @Rellex, t.me/rellex
