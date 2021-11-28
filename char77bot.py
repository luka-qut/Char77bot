import telebot
import os
from flask import Flask, request
import logging

APP_URL = 'https://char77-bot.herokuapp.com/'
token = '2146891986:AAE_cNVXBaH5pTMkfqAJBOoYfcrftP0eyA0'
logger = telebot.logger
logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(token)
server = Flask(__name__)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Apple',callback_data='apple')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Samsung',callback_data='samsung')
    )    
    keyboard.row( 
        telebot.types.InlineKeyboardButton('Xiaomi',callback_data='xiaomi'),
        telebot.types.InlineKeyboardButton('Huawei',callback_data='huawei'),
        telebot.types.InlineKeyboardButton('Honor',callback_data='honor')
        )
    
    bot.send_message(message.chat.id,'Выберите бренд',reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def char_message(message):
    print(message.data)
    id = message.id
    if 'apple' == message.data:
        print(message.message.id)
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('iPhone11',callback_data='iPhone 11'),
            telebot.types.InlineKeyboardButton('iPhone11Pro',callback_data='iPhone 11pro'),
            telebot.types.InlineKeyboardButton('iPhone11ProMax',callback_data='iPhone 11ProMax')
            )
        keyboard.row(
            telebot.types.InlineKeyboardButton('iPhone12',callback_data='iPhone 12'),
            telebot.types.InlineKeyboardButton('iPhone12Pro',callback_data='iPhone 12Pro'),
            telebot.types.InlineKeyboardButton('iPhone12ProMax',callback_data='iPhone 12ProMax')
            )
        keyboard.row(
            telebot.types.InlineKeyboardButton('iPhone13',callback_data='iPhone13'),
            telebot.types.InlineKeyboardButton('iPhone13Pro',callback_data='iPhone 13Pro'),
            telebot.types.InlineKeyboardButton('iPhone13ProMax',callback_data='iPhone 13ProMax')
            )
        
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад',callback_data='to_brand_list')
            )        
        bot.edit_message_text(text='Выберите телефон', chat_id=message.message.chat.id, message_id=message.message.id)
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.id, reply_markup=keyboard)
    
    #Тут apple
    elif 'iPhone 11' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/SJTp64t/iphn11.png',caption='Характеристики 11',reply_markup=keyboard)

    elif 'iPhone 11pro' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/1M3wAz1FxFMCGw',caption='Характеристики 11Pro',reply_markup=keyboard)

    elif 'iPhone 11ProMax' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/ZVRq6-425T4k-w',caption='Характеристики 11ProMax',reply_markup=keyboard)


    elif 'iPhone 12' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/7bBfdM3/iphone12.png',caption='Характеристики 12',reply_markup=keyboard)
    
    elif 'iPhone 12Pro' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/cgnjHzq/iphone12pro.png',caption='Характеристики 12 Pro',reply_markup=keyboard)

    elif 'iPhone 12ProMax' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/YpT136p/iphone12promax.png',caption='Характеристики 12 ProMax',reply_markup=keyboard)

    elif 'iPhone13' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/CVJKm71/iphone13.png',caption='Характеристики 13',reply_markup=keyboard)

    elif 'iPhone 13Pro' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/RcJNLWq/iphone13prozagruzispliz.png',caption='Характеристики 13Pro',reply_markup=keyboard)

    elif 'iPhone 13ProMax' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/v8-q-6LSjM_KTA',caption='Характеристики 13ProMax',reply_markup=keyboard)
    


    

    elif 'to_brand_list' == message.data:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
        telebot.types.InlineKeyboardButton('Apple',callback_data='apple')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Samsung',callback_data='samsung')
    )    
        keyboard.row( 
        telebot.types.InlineKeyboardButton('Xiaomi',callback_data='xiaomi'),
        telebot.types.InlineKeyboardButton('Huawei',callback_data='huawei'),
        telebot.types.InlineKeyboardButton('Honor',callback_data='honor')
        )
        bot.edit_message_text(chat_id=message.message.chat.id, text='Выберите бренд', message_id=message.message.id)
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.id, reply_markup=keyboard)
    
    elif 'to_new_request' == message.data:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
        telebot.types.InlineKeyboardButton('Apple',callback_data='apple')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Samsung',callback_data='samsung')
    )    
        keyboard.row( 
        telebot.types.InlineKeyboardButton('Xiaomi',callback_data='xiaomi'),
        telebot.types.InlineKeyboardButton('Huawei',callback_data='huawei'),
        telebot.types.InlineKeyboardButton('Honor',callback_data='honor')
        )
        bot.send_message(chat_id=message.message.chat.id, text='Выберите бренд', reply_markup=keyboard)
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.id, reply_markup=None)



@server.route(f"/{token}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200



if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))