import telebot
import sqlite3
from telebot import types


bot = telebot.TeleBot('bot')

@bot.message_handler(commands=['start'])

def start(message):
    conn = sqlite3.connect('baza.sql')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, id_name char(50), first_name varchar('
        '50), last_name varchar(50), bezopas integer, komfort integer, clear integer)')
    conn.commit()
    cur.close()
    conn.close()
    global result_full
    result_full=[message.from_user.id, message.from_user.first_name, message.from_user.last_name]

    kp = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Опрос", callback_data='btn1')
    kp.row(btn1)
    bot.send_message(message.chat.id,
                     f"Приветствую! {message.from_user.first_name} {message.from_user.last_name}. Выберите действие.",
                     reply_markup=kp)

    #bot.register_next_step_handler(message, on_click)

@bot.callback_query_handler(func=lambda call: call.data=='btn1')
def check_one(call: types.CallbackQuery):
    #bot.register_next_step_handler(call.message, take)
#def take(call: types.CallbackQuery):
    markup2 = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('1', callback_data='odin_b')
    btn_2 = types.InlineKeyboardButton('2', callback_data='dva_b')
    btn_3 = types.InlineKeyboardButton('3', callback_data='tri_b')
    btn_4 = types.InlineKeyboardButton('4', callback_data='che_b')
    btn_5 = types.InlineKeyboardButton('5', callback_data='pyti_b')
    markup2.row(btn_1, btn_2, btn_3, btn_4, btn_5)
    bot.send_message(call.message.chat.id, ' Оцените ', reply_markup=markup2)
    #bot.register_next_step_handler(call, callback_message)
#@bot.callback_query_handler(func=lambda call: True)
#def check_callback_data(call):
#    if call.data == "btn1":
#        return check_one(message=call)


#def check_one(message):
#    markup2 = types.InlineKeyboardMarkup()
#    btn_1 = types.InlineKeyboardButton('1', callback_data='odin')
#    btn_2 = types.InlineKeyboardButton('2', callback_data='dva')
#    btn_3 = types.InlineKeyboardButton('3', callback_data='tri')
#    btn_4 = types.InlineKeyboardButton('4', callback_data='che')
#    btn_5 = types.InlineKeyboardButton('5', callback_data='pyti')
#    markup2.row(btn_1, btn_2, btn_3, btn_4, btn_5)
#    bot.send_message(callback.message.chat.id, ' Оцените ', reply_markup=markup2)
    # bot.register_next_step_handler(message, callback_message)


@bot.callback_query_handler(func=lambda callback: callback.data == 'odin_b' or callback.data == 'dva_b' or callback.data == 'tri_b' or callback.data == 'che_b' or callback.data == 'pyti_b')

def callback_message_b(callback):

    #result_b=[callback.message.chat.first_name]
    if callback.data == 'odin_b':
        bot.send_message(callback.message.chat.id, f'1 {callback.message.chat.first_name}')
        #t = callback.message.chat.first_name
        #print(callback.from_user.first_name)
        result_full.append(1)
        #conn = sqlite3.connect('baza.sql')
        #cur = conn.cursor()
        #cur.execute("INSERT INTO users(name, pass) VALUES (?, ?);", ('rtrgf', 'sdhshj'))
        #conn.commit()
        #cur.close()
        #conn.close()
        #one_bezopas()
    elif callback.data == 'dva_b':
            bot.send_message(callback.message.chat.id, f'2 {callback.message.chat.first_name}')
        # t = callback.message.chat.first_name
        #print(callback.from_user.first_name)
            result_full.append(2)
    elif callback.data == 'tri_b':
            result_full.append(3)
    elif callback.data == 'che_b':
            result_full.append(4)
    elif callback.data == 'pyti_b':
            result_full.append(5)
    markup2 = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('1', callback_data='odin_k')
    btn_2 = types.InlineKeyboardButton('2', callback_data='dva_k')
    btn_3 = types.InlineKeyboardButton('3', callback_data='tri_k')
    btn_4 = types.InlineKeyboardButton('4', callback_data='che_k')
    btn_5 = types.InlineKeyboardButton('5', callback_data='pyti_k')
    markup2.row(btn_1, btn_2, btn_3, btn_4, btn_5)
    bot.send_message(callback.message.chat.id, ' Оцените по пятибалльной шкале комфорт ', reply_markup=markup2)
# bot.register_next_step_handler(message, callback_message)

#d3ef one_bezopas():
#    conn = sqlite3.connect('baza.sql')
#    cur = conn.cursor()
#    cur.execute(f"INSERT INTO users(name) VALUES (1)")
#    conn.commit()
#    cur.close()
#    conn.close()
@bot.callback_query_handler(func=lambda callback: callback.data == 'odin_k' or callback.data == 'dva_k' or callback.data == 'tri_k' or callback.data == 'che_k' or callback.data == 'pyti_k')

def callback_message_k(callback):

    if callback.data == 'odin_k':
        bot.send_message(callback.message.chat.id, f'1 {callback.message.chat.first_name}')
        result_full.append(1)
    elif callback.data == 'dva_k':
            bot.send_message(callback.message.chat.id, f'2 {callback.message.chat.first_name}')
            result_full.append(2)
    elif callback.data == 'tri_k':
            result_full.append(3)
    elif callback.data == 'che_k':
            result_full.append(4)
    elif callback.data == 'pyti_k':
            result_full.append(5)
    markup2 = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('1', callback_data='odin_c')
    btn_2 = types.InlineKeyboardButton('2', callback_data='dva_c')
    btn_3 = types.InlineKeyboardButton('3', callback_data='tri_c')
    btn_4 = types.InlineKeyboardButton('4', callback_data='che_c')
    btn_5 = types.InlineKeyboardButton('5', callback_data='pyti_c')
    markup2.row(btn_1, btn_2, btn_3, btn_4, btn_5)
    bot.send_message(callback.message.chat.id, ' Оцените по пятибалльной шкале чистоты ', reply_markup=markup2)

# @bot.message_handler(commands=['cr'])
# def get_calendar(message):
#   now = datetime.datetime.now() #Текущая дата
#  chat_id = message.chat.id
# date = (now.year,now.month)
# current_shown_dates[chat_id] = date #Сохраним текущую дату в словарь
# markup = create_calendar(now.year,now.month)
# bot.send_message(message.chat.id, "Пожалйста, выберите дату", reply_markup=markup)
@bot.callback_query_handler(func=lambda callback: callback.data == 'odin_c' or callback.data == 'dva_c' or callback.data == 'tri_c' or callback.data == 'che_c' or callback.data == 'pyti_c')

def callback_message_k(callback):

    if callback.data == 'odin_c':
        bot.send_message(callback.message.chat.id, f'1 {callback.message.chat.first_name}')
        result_full.append(1)
    elif callback.data == 'dva_c':
            bot.send_message(callback.message.chat.id, f'2 {callback.message.chat.first_name}')
            result_full.append(2)
    elif callback.data == 'tri_c':
            result_full.append(3)
    elif callback.data == 'che_c':
            result_full.append(4)
    elif callback.data == 'pyti_c':
            result_full.append(5)
    bot.send_message(callback.message.chat.id, 'Спасибо за ответы! Хорошего дня! \nК возврату главного меню /start')
    conn = sqlite3.connect('baza.sql')
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO    users (id_name, first_name, last_name, bezopas, komfort, clear) VALUES (?, ?, ?, ?, ?, ?)',
        result_full)
    conn.commit()
    cur.close()
    conn.close()
    #bot.register_next_step_handler(resultat)
@bot.message_handler(content_types=['text'])
def one(message):

    markup2 = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('1', callback_data='one')
    btn_2 = types.InlineKeyboardButton('2', callback_data='one')
    btn_3 = types.InlineKeyboardButton('3', callback_data='one')
    btn_4 = types.InlineKeyboardButton('4', callback_data='one')
    btn_5 = types.InlineKeyboardButton('5', callback_data='one')
    markup2.row(btn_1, btn_2, btn_3, btn_4, btn_5)
    bot.reply_to(message, 'Привет ', reply_markup=markup2)
    print(result_full)
def resultat():
    conn = sqlite3.connect('baza.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users(id_name, first_name, last_name, bezopas< komfort, clear) VALUES (?, ?, ?, ?, ?, ?);", (result_full[0], result_full[1], result_full[2], result_full[3], result_full[4]), result_full[5])
    conn.commit()
    cur.close()
    conn.close()
# @bot.message_handler(content_types=['text'])
# def get_text_messag(messags):
# bot.send_message(messags.from_user.id, 'ЗРТТР')


# А дальше всё работает

bot.polling(none_stop=True, interval=0)



