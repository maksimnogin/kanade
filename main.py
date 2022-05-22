# ---------------------------------------------------------------------------
import telebot

from telebot import types

# ---------------------------------------------------------------------------
from telebot.types import InlineKeyboardButton

bot = telebot.TeleBot('5220353983:AAGCEhUsqgilJRoa1IrgRN1mZR-8xTIhzFk')


@bot.message_handler(commands=['start'])
# ---------------------------------------------------------------------------

def welcome(message):

    # клавиатура (Создание кнопок и приветствие)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    item1 = types.KeyboardButton("🎸 Найти реп-точку 🎸")
    item2 = types.KeyboardButton("📃 Обо мне 📃")
    item3 = types.KeyboardButton("📱 Контакты 📱")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Привет, {0.first_name}!🎉\nНегде репетировать?\nЯ - <b>{1.first_name}</b>, помогу тебе найти реп-точку!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
# ---------------------------------------------------------------------------

def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎸 Найти реп-точку 🎸':

            # клавиатура (Создание кнопок под текстом)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Таганрог", callback_data='1')
            item2 = types.InlineKeyboardButton("Ростов-на-Дону", callback_data='2')


            markup.add(item1, item2,)

            bot.send_message(message.chat.id, 'В каком городе требуется найти? 🌆', reply_markup=markup)

        # elif message.text == ' '
        elif message.text == "📃 Обо мне 📃":
            bot.send_message(message.chat.id,
                             "<b> Вас неожиданно выгнали с точки? Я покажу вам, где можно порепетировать в Таганроге или Ростове-на-Дону.\n"
                             "На данный момент - это все, что я умею..но обещаю исправиться:) </b>",
                             parse_mode='html')

        elif message.text == "📱 Контакты 📱":
            bot.send_message(message.chat.id,
                             'Бот был создан @maksrolinh\nВконтакте:https://vk.com/dyingforfame\nТелефон:+7(952) 568-56-97',
                             parse_mode='html')


        else:
            bot.send_message(message.chat.id, 'Если у вас остались какие-то вопросы, напишите, пожалуйста сюда --> @maksrolinh')


# ---------------------------------------------------------------------------
points = { '1': [{'point': '1', 'address': 'Заводская, 20/3', 'contact': 'Номер телефона: +7 (988) 556-71-14','title':'Олимп'},
                 {'point': '2', 'address': 'Петровская ул.91', 'contact': 'Номер телефона: +7 (938) 109-77-66','title':'WЭLСOM'},
                 {'point': '3', 'address': 'Комсомольский пер.58а', 'contact': 'Номер телефона: +7 (908)187-55-75','title':'Репа'}],

           '2': [{'point': '1', 'address': 'Тургеневская 16', 'contact': 'Номер телефона: 7 (988) 993-39-05','title':'Бас-бочка'},
                 {'point': '2', 'address': 'Гвардейский пер., 61а', 'contact': 'Номер телефона:  +7 (928) 960-68-56','title':',База'},
                 {'point': '3', 'address': 'Станиславского 87', 'contact': 'Номер телефона:  +7 (928) 616-64-06','title':'Локки'},
                 {'point': '4', 'address': 'Гвардейский пер.61А', 'contact': 'Номер телефона: +7 (928) 960-68-56','title':'Joker'},
                 {'point': '5', 'address': 'Соборный пер., д. 24', 'contact': 'Номер телефона: +7 (951) 500-48-09','title':'ПЕТРОFF Music'},
                 {'point': '6', 'address': 'Привокзальная, 4', 'contact': 'Номер телефона: +7 (928) 146-61-33','title':'Sacra-studio'},
                 {'point': '7', 'address': 'Мечникова 112/1', 'contact': 'Номер телефона: +7 (904) 448-87-27','title':'Tamata Sound Studio'},
                 {'point': '8', 'address': 'Текучева ул.183', 'contact': 'Номер телефона: +7 (919) 888-03-74','title':'REPEATiT'}
                 ]}
# ---------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:

            # клавиатура (Работа с кнопками под текстом)
            if call.data == '1':
                markup = types.InlineKeyboardMarkup(row_width=3)
                for point in points[str(call.data)]:
                    markup.add(InlineKeyboardButton(f'Точка {point["point"]}', callback_data=f'point_1_{point["point"]}'))
                # item1 = types.KeyboardButton("Найти реп-точку")
                bot.send_message(call.message.chat.id, 'Доступные точки', reply_markup=markup)

            elif call.data == '2':
                markup = types.InlineKeyboardMarkup(row_width=3)
                for point in points[str(call.data)]:
                    markup.add(InlineKeyboardButton(f'Точка {point["point"]}', callback_data=f'point_2_{point["point"]}'))
                #item1 = types.KeyboardButton("Найти реп-точку")
                bot.send_message(call.message.chat.id, 'Доступные точки',reply_markup = markup)
            elif 'point' in call.data:
                print(call.data)

                id = call.data.split('_')[2]
                for point in points[call.data.split('_')[1]]:
                    if point['point'] == id:
                        bot.send_message(call.message.chat.id,
                                         f'Название:<u>{point["title"]}</u>\nАдрес: {point["address"]}\nКонтактная информация:\n<b>{point["contact"]}</b>', parse_mode='html')
 # ---------------------------------------------------------------------------
            # удаление inline кнопок
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="  ",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Пишите, всегда помогу!")

    except Exception as e:
        print(repr(e))


# ---------------------------------------------------------------------------


# Старт
bot.polling(none_stop=True)

# ---------------------------------------------------------------------------