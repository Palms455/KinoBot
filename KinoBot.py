import telebot
from message import msg, msg1
from new_token import token
import cityopen


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Мираж', 'Кинопорт', 'Салават')


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_message(message):
	bot.send_message(message.chat.id, msg, reply_markup=keyboard1)



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'мираж':
        url = 'https://cityopen.ru/afisha/kinoteatr-mirazh-sinema/'
        x = 13
        state = 'Кинопорт'
    elif message.text.lower() == 'кинопорт':
        url = 'https://cityopen.ru/afisha/kinotsentr-kinoport/'
        x = 15
        state = 'Кинопорт'
    elif message.text.lower() == 'салават':
        url = 'https://cityopen.ru/afisha/kinoteatr-salavat/'
        x = 5
        state = 'Салават'
    else:
        message.text.lower() == 'что посмотреть'
        bot.send_message(message.chat.id, 'Расписание сеансов во всех кинокомплексах',  reply_markup=keyboard1)
        url = 'https://cityopen.ru/afisha/kinoteatr-mirazh-sinema/'
        x = 13
        state = 'Кинопорт'

    movie_list = cityopen.data(url, x)
    bot.send_message(message.chat.id, f'Сеансы в кинокомплексе "{state}" на {movie_list[0]}')
    for movie in movie_list[1]:
        bot.send_message(message.chat.id, movie)
        bot.send_message(message.chat.id, ' '.join(movie_list[1][movie]), reply_markup=keyboard1)
   
bot.polling()

