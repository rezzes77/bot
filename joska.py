

# import telebot
# import webbrowser



# bot = telebot.TeleBot('7546222072:AAELNOTMtY8NGxfCuCSWuDKirhuN_vcBtU0')


# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://chatgpt.com/c/66ec4f39-d280-8011-b12a-eb5ccad7d269')

# @bot.message_handler(commands=['start','hello','sigma'])
# def start(message):
#     bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.username}')

# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>help you</b>', parse_mode='html')
    
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'lol':
#         bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.username}')
#     elif message.text.lower() == 'id':
#         bot.send_message(message.chat.id, f'ID: {message.from_user.id}')

    
# bot.polling(non_stop=True)


















# import telebot

# TOKEN = '7546222072:AAELNOTMtY8NGxfCuCSWuDKirhuN_vcBtU0'
# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id,'5 Декабрь, оставался 1 день для священного дня рождение Абдулхамида, это было в школе и с ним было 3 друзей Муслим,Абидин и Нурэл и вдруг Абидин заметил что Абдулхамид пропал и они начали искать и они заметили что школа была заперта и все ученики пропали кроме них.Они были в ужасе и в раздевалке они нашли Абдулхамида с прореззанным горлом и он уже был мертвб ина стене было надпись среди вас убийца вы должны найти его либа вас настигнет та же участь!!!')
# bot.polling(non_stop=True)