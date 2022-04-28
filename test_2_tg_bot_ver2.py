import telebot
import requests
import time

def inn_valid(inn):

    inn_9 = inn[:-1]
    number = [2,4,10,3,5,9,4,6,8]

    kontr = 0
    try:
        for k, i in enumerate(inn_9):
            kontr += (int(i) * number[k])

        kontr_0 = kontr
        #print(kontr_0)

        kontr = int(kontr/11)
        kontr = kontr * 11
        #print(kontr)

        kontr_num = kontr_0 - kontr
        #print(kontr_num)
        #print(inn[-1:])

        if int(inn[-1:]) == kontr_num:
            return 'valid'
        else:
            return 'no_valid'

    except:
        return 'no_valid'

token = '73442*********************xA-5sz8'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Вас привествует робот валидности ИНН")
    bot.send_message(message.chat.id, "Введите ИНН компании:")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, f'Вы ввели ИНН: {message.text}')
    inn = message.text
    vl = inn_valid(inn)

    if vl == 'valid':
        bot.send_message(message.from_user.id, 'ИНН валиден 👍🏼')

    else:
        bot.send_message(message.from_user.id, 'ИНН не валиден 🤷\nПроверьте правильность ввода. Вожможно контрагент мошенник((')

bot.infinity_polling()
