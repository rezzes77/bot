import telebot
from time import sleep

TOKEN = '7541006559:AAHjiCpiWcbteKJleHNvOEYPLjUNJgOwfBg'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет я бот. Я помогу тебе с математикой, у меня есть игра-викторина по матеше и всего 6 уровня, если хочешь улучшить свои навыки то скинь мне букву s')

@bot.message_handler(content_types=['text'])
def text(message):
    user_input = message.text.upper()  
    print(f"Received input: {user_input}") 
    if user_input == 'S':
        bot.send_message(message.chat.id, 'Хорошо погнали, 1 пример уровень 1/10: 2 + 5')
    elif user_input == '7':
        sleep(1)
        bot.send_message(message.chat.id, 'Правильно! Теперь 2 пример уровень 2.5/10: 20 * 10 ')
    elif user_input == '200':
        sleep(1)
        bot.send_message(message.chat.id, 'Правильно! Теперь 3 пример уровень 5/10: 45 + 12 × 3 ')
    elif user_input == '81':
        sleep(1)
        bot.send_message(message.chat.id, 'Правильно! Теперь 4 пример уровень 7/10: (25 − 5) × (6 + 4 + 2) = ? ')
    elif user_input == '202':
        sleep(1)
        bot.send_message(message.chat.id, 'Правильно! Теперь 5 пример уровень 8.5/10: (8 × 9) − (52) + 36 = ?')
    elif user_input == '56':
        sleep(1)
        bot.send_message(message.chat.id, 'Правильно! Теперь 6 пример уровень 10/10: (25 × 4 + 36 − 15) × (8 + 12) − (50 + 32 × 2) + (7 × 15 − 23) × (14 − 9 + 6) + 100 − 45')
    elif user_input == '3263':
        sleep(1)
        bot.send_message(message.chat.id, 'Правильно! А теперь решим какую оценку тебе надо поставить напиши сколько примеров у тебя вышла правильно и я поставлю тебе оценку напиши типо так 1/6')
    elif user_input == '1/6':
        sleep(1)
        bot.send_message(message.chat.id, 'Как то маловато я не могу поставить даже 2, так что немного подготовся (')
    elif user_input == '2/6':
        sleep(1)
        bot.send_message(message.chat.id, 'Это немного получше но тебе так же надо подготовка а так тебе 2')
    elif user_input == '3/6':
        sleep(1)
        bot.send_message(message.chat.id, 'Так за старание тебе 3')
    elif user_input == '4/6':
        sleep(1)
        bot.send_message(message.chat.id, 'Молодец это хороший результат ставлю тебе 4')
    elif user_input == '5/6':
        sleep(1)
        bot.send_message(message.chat.id, 'Супер! Ты мега харош тебе 5')
    elif user_input == '6/6':
        sleep(1)
        bot.send_message(message.chat.id, 'ТЫ ВАЩЕ КТОО!? ТЕБЕ 5++ ДАЖЕ Я ТАКОЕ НЕ МОГУ')
    elif user_input == 'Конечно это же я гений':
        sleep(1)
        bot.send_message(message.chat.id,'Все викторина закончилась, ожидайте продолжоние или другие викторины)')
    else:
        bot.send_message(message.chat.id, 'Ответ неверный, попытайся еще раз(')

bot.infinity_polling()
