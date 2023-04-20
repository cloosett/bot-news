import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5950055024:AAH_KPgRUciCiLcHsv_m2zSoyPaY5OeV0CU')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Щоб отримати останні новини, напишіть команду /news")

@bot.message_handler(commands=['news'])
def get_news(message):
    url = 'https://www.unian.ua/war'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    news = soup.find_all('div', class_='list-thumbs__item')
    for n in news:
        bot.send_message(message.chat.id, n.text)
    bot.send_message(message.chat.id, 'Це найсвіжіші новини, за останні пару годин.')

bot.polling(none_stop=True)
