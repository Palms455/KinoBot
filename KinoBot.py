import telebot
from message import msg, msg1
from new_token import token
import cityopen


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Мираж', 'Кинопорт', 'Салават').row('Что посмотреть')


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_message(message):
	bot.send_message(message.chat.id, msg, reply_markup=keyboard1)



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'мираж':
        bot.send_message(message.chat.id, 'Сеансы в кинокомплексе "Мираж"')
        bot.send_message(message.chat.id, data('https://cityopen.ru/afisha/kinoteatr-mirazh-sinema/'),  reply_markup=keyboard1)
    elif message.text.lower() == 'кинопорт':
        movie_list = cityopen.data('https://cityopen.ru/afisha/kinotsentr-kinoport/')
        bot.send_message(message.chat.id, f'Сеансы в кинокомплексе "Кинопорт" на {movie_list[0]}')
        for movie in movie_list[1]:
            bot.send_message(message.chat.id, movie)
            bot.send_message(message.chat.id, ' '.join(movie_list[1][movie]), reply_markup=keyboard1)
    elif message.text.lower() == 'салават':
        bot.send_message(message.chat.id, 'Сеансы в кинокомплексе "Салават"')
        bot.send_message(message.chat.id, data('https://cityopen.ru/afisha/kinoteatr-salavat/'),  reply_markup=keyboard1)
    elif message.text.lower() == 'что посмотреть':
    	bot.send_message(message.chat.id, 'Расписание сеансов во всех кинокомплексах',  reply_markup=keyboard1)
    else:
        bot.send_sticker(message.chat.id, msg1)
bot.polling()

