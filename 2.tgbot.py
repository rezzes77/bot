import telebot

TOKEN = '7074421179:AAGw1HKg14J3uasM47XVwLENZFVfBTzMGbk'

bot = telebot.TeleBot(TOKEN)

def send_main_menu(chat_id):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('ANIME')
    button2 = telebot.types.KeyboardButton('MUSIC')
    keyboard.add(button1, button2)
    
    bot.send_message(
        chat_id,
        'Welcome to the bot where you can find your favourite music or anime! There are openings, photos and more! Please choose anime or music!',
        reply_markup=keyboard
    )

@bot.message_handler(commands=['start'])
def send_welcome(message):
    send_main_menu(message.chat.id)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'ANIME':
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = telebot.types.KeyboardButton('TOKYO GHOUL')
        button2 = telebot.types.KeyboardButton('BLACK CLOVER')
        button3 = telebot.types.KeyboardButton('LAIN')
        button4 = telebot.types.KeyboardButton('ATTACK ON TITAN')
        back_button = telebot.types.KeyboardButton('BACK')  
        keyboard.add(button1, button2, button3, button4, back_button)
        
        bot.send_message(message.chat.id, 'Choose your anime:', reply_markup=keyboard)

    elif message.text == 'MUSIC':
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = telebot.types.KeyboardButton('SEE YOU AGAIN')
        button2 = telebot.types.KeyboardButton('DARK RED')
        button3 = telebot.types.KeyboardButton('BAD HABIT')
        button4 = telebot.types.KeyboardButton('DUVET')
        back_button = telebot.types.KeyboardButton('BACK')  
        keyboard.add(button1, button2, button3, button4, back_button)
        
        bot.send_message(message.chat.id, 'Choose your music:', reply_markup=keyboard)

    elif message.text == 'BACK':
        send_main_menu(message.chat.id)

@bot.message_handler(func=lambda message: message.text == 'TOKYO GHOUL')
def send_tokyo_ghoul(message):
    try:
        with open('image/176019-kirishima_touka-ken_kaneki-anime-tokijskij_gul-rize_kamishiro-3840x2160.jpg', 'rb') as img:
            bot.send_photo(message.chat.id, img, caption='THIS IS TOKYO GHOUL ANIME')
        
        with open('image/tokiyskiy-gul--1-sezon-1-opening.mp3', 'rb') as audio_file:
            bot.send_audio(message.chat.id, audio_file, caption='THIS IS OPENING TOKYO GHOUL')
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Image or audio file not found.")
    except Exception as e:
        bot.send_message(message.chat.id, f"An error occurred: {e}")

bot.polling(none_stop=True)


# @bot.message_handler(func=lambda message: message.text == 'The cheapest BMW')
# def send_cheapest_bmw(message):
#     try:
#         with open('image/bmw-2002-modified.avif', 'rb') as img:
#             bot.send_photo(message.chat.id, img, caption='The cheapest BMW. BMW car price starts at Rs 43.90 Lakh for the cheapest model, the 2 Series Gran Coupe, and the price of the most expensive model, XM, starts at Rs 2.60 Crore.')
#     except FileNotFoundError:
#         bot.send_message(message.chat.id, "Image not found.")

# @bot.message_handler(func=lambda message: message.text == 'The oldest BMW')
# def send_oldest_bmw(message):
#     try:
#         with open('image/bmw-throughout-history-327-coupe.jpg', 'rb') as img:
#             bot.send_photo(message.chat.id, img, caption='This is the oldest BMW. BMW was officially founded on 7 March 1916 as Bayerische Flugzeugwerke, later renamed to Bayerische Motoren Werke (BMW) in 1922.')
#     except FileNotFoundError:
#         bot.send_message(message.chat.id, "Image not found.")

# @bot.message_handler(func=lambda message: message.text == 'The newest BMW')
# def send_newest_bmw(message):
#     try:
#         with open('image/9eb9e792-18cd-4214-a0a4-b0f8790ce3e6-NewBMWs_060721_ES03.webp', 'rb') as img:
#             bot.send_photo(message.chat.id, img, caption='This is the newest BMW. The newest model in the BMW line-up is the 5 Series with a price tag of ₹ 72.90 Lakh.')
#     except FileNotFoundError:
#         bot.send_message(message.chat.id, "Image not found.")

# @bot.message_handler(func=lambda message: message.text == 'Video')
# def send_video_bmw(message):
#     try:
#         with open('image/88481-606110665.mp4', 'rb') as vid:
#             bot.send_video(message.chat.id, vid, caption="Это видео.")
#     except FileNotFoundError:
#         bot.send_message(message.chat.id, "Video not found.")


import telebot

# Укажите ваш токен бота
TOKEN = '7547107727:AAFHX5NUJp9cF0ER12y4mtp2HiidTGGtGtc'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создание клавиатуры с кнопками
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('gucci')
    button2 = telebot.types.KeyboardButton('perfume')
    button3 = telebot.types.KeyboardButton('Video-Nike')
    button4 = telebot.types.KeyboardButton('Help') 
    button5 = telebot.types.KeyboardButton('Audio') 
    keyboard.add(button1, button2, button3, button4, button5)

    # Отправка приветственного сообщения с клавиатурой
    bot.send_message(message.chat.id, "Welcome to my shopping bot! Please choose an option:", reply_markup=keyboard)

# Обработчик нажатия на кнопку "Nike"
@bot.message_handler(func=lambda message: message.text == 'gucci')
def send_nike(message):
    # Отправка изображения
    with open('gucci1.webp', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="This is the first shirt. Nice!")

@bot.message_handler(func=lambda message: message.text == 'perfume')
def send_nike(message):
    # Отправка изображения
    with open('gucci-women-s-perfume-gucci-bloom-eau-de-parfum-women-s-perfume-spray-30ml-50ml-100ml-36397336854687.png.webp', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="This is the first perfume. Nice!")        

# Обработчик нажатия на кнопку "Video-Nike"
@bot.message_handler(func=lambda message: message.text == 'Video-Nike')
def send_video_nike(message):
    # Отправка видео
    with open('NIKE - COMMERCIAL - 2024 -  JUST DO IT - AI ENTERTAINMENT.mp4', 'rb') as vid:
        bot.send_video(message.chat.id, vid, caption="Это видео.")

# Обработчик нажатия на кнопку "Help"
@bot.message_handler(func=lambda message: message.text == 'Help')
def send_help(message):
    # Отправка сообщения со справкой
    bot.send_message(message.chat.id, "Это справочное сообщение. Введите /start для начала работы с ботом.")

# Обработчик нажатия на кнопку "Audio"
@bot.message_handler(func=lambda message: message.text == 'Audio')
def send_audio(message):
    # Отправка аудиосообщения
    with open('АДЛИН - No Love.mp3', 'rb') as audio:
        bot.send_voice(message.chat.id, audio, caption="Это аудиосообщение.")

# Запуск бота
bot.polling()