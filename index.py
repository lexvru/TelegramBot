import telebot
import sqlite3
from telebot import types


bot = telebot.TeleBot('6585664820:AAEzz9yRAMFRkSZaevw347WUNBnxmYoQv')


@bot.message_handler(commands=['start'])

def start(message):
    conn = sqlite3.connect('baza.sql')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    kp = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Опрос", callback_data='btn1')
    kp.row(btn1)
    bot.send_message(message.chat.id,
                     f"Приветствую! {message.from_user.first_name} {message.from_user.last_name}. Выберите действие.",
                     reply_markup=kp)
    #bot.register_next_step_handler(message, on_click)
def name():
    s = message.from_user.first_name
    return s
@bot.callback_query_handler(func=lambda call: call.data=='btn1')
def check_one(call: types.CallbackQuery):
    #bot.register_next_step_handler(call.message, take)
#def take(call: types.CallbackQuery):
    markup2 = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('1', callback_data='odin')
    btn_2 = types.InlineKeyboardButton('2', callback_data='dva')
    btn_3 = types.InlineKeyboardButton('3', callback_data='tri')
    btn_4 = types.InlineKeyboardButton('4', callback_data='che')
    btn_5 = types.InlineKeyboardButton('5', callback_data='pyti')
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


@bot.callback_query_handler(func=lambda callback: callback.data == 'odin')

def callback_message(callback):
    if callback.data == 'odin':
        bot.send_message(callback.message.chat.id, f'1 {callback.message.chat.first_name}')
        #t = callback.message.chat.first_name
        t=name(message)

        conn = sqlite3.connect('baza.sql')
        cur = conn.cursor()
        cur.execute("INSERT INTO users(name, pass) VALUES (?, ?);", ('rtrgf', t))
        conn.commit()
        cur.close()
        conn.close()
        one_bezopas()


def one_bezopas():
    conn = sqlite3.connect('baza.sql')
    cur = conn.cursor()
    cur.execute(f"INSERT INTO users(name) VALUES (1)")
    conn.commit()
    cur.close()
    conn.close()


# @bot.message_handler(commands=['cr'])
# def get_calendar(message):
#   now = datetime.datetime.now() #Текущая дата
#  chat_id = message.chat.id
# date = (now.year,now.month)
# current_shown_dates[chat_id] = date #Сохраним текущую дату в словарь
# markup = create_calendar(now.year,now.month)
# bot.send_message(message.chat.id, "Пожалйста, выберите дату", reply_markup=markup)

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


# @bot.message_handler(content_types=['text'])
# def get_text_messag(messags):
# bot.send_message(messags.from_user.id, 'ЗРТТР')


# А дальше всё работает

bot.polling(none_stop=True, interval=0)
