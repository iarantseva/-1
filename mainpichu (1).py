import telebot
from bs4 import BeautifulSoup
import requests
from telebot import types
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

bot = telebot.TeleBot("1614014282:AAG8Jw4ESPvjdeqZorEKCQ9acsztcERxaag")
last_call = ''
dictionary_znaki = {'Овен Овен': [41, 93, 86], 'Овен Телец': [68, 23, 35], 'Овен Близнецы': [97, 83, 78],
                            'Овен Рак': [67, 21, 75], 'Овен Лев': [89, 90, 97], 'Овен Дева': [26, 54, 63],
                            'Овен Весы': [84, 95, 22], 'Овен Скорпион': [88, 19, 72], 'Овен Стрелец': [77, 93, 90],
                            'Овен Козерог': [58, 37, 86], 'Овен Водолей': [78, 98, 93], 'Овен Рыбы': [18, 32, 14],
                            'Телец Овен': [54, 68, 26], 'Телец Телец': [95, 97, 82], 'Телец Близнецы': [16, 20, 35],
                            'Телец Рак': [92, 95, 74], 'Телец Лев': [15, 18, 21], 'Телец Дева': [86, 98, 95],
                            'Телец Весы': [41, 80, 85], 'Телец Скорпион': [53, 78, 90], 'Телец Стрелец': [17, 43, 36],
                            'Телец Козерог': [96, 82, 98], 'Телец Водолей': [47, 25, 37], 'Телец Рыбы': [45, 87, 55],
                            'Близнецы Овен': [68, 95, 98], 'Близнецы Телец': [58, 70, 42],
                            'Близнецы Близнецы': [73, 99, 85], 'Близнецы Рак': [21, 23, 17],
                            'Близнецы Лев': [93, 82, 86], 'Близнецы Дева': [11, 67, 91], 'Близнецы Весы': [95, 97, 84],
                            'Близнецы Скорпион': [63, 47, 85], 'Близнецы Стрелец': [88, 85, 92],
                            'Близнецы Козерог': [38, 12, 61], 'Близнецы Водолей': [76, 90, 88],
                            'Близнецы Рыбы': [24, 78, 11], 'Рак Овен': [71, 24, 14], 'Рак Телец': [86, 90, 98],
                            'Рак Близнецы': [37, 31, 56], 'Рак Рак': [95, 97, 77], 'Рак Лев': [53, 42, 87],
                            'Рак Дева': [84, 97, 91], 'Рак Весы': [32, 36, 20], 'Рак Скорпион': [88, 95, 98],
                            'Рак Стрелец': [46, 28, 32], 'Рак Козерог': [15, 21, 43], 'Рак Водолей': [16, 62, 40],
                            'Рак Рыбы': [93, 97, 76], 'Лев Овен': [78, 91, 98], 'Лев Телец': [38, 17, 65],
                            'Лев Близнецы': [84, 94, 79], 'Лев Рак': [42, 46, 53], 'Лев Лев': [92, 90, 88],
                            'Лев Дева': [17, 65, 86], 'Лев Весы': [86, 97, 94], 'Лев Скорпион': [36, 33, 53],
                            'Лев Стрелец': [76, 90, 82], 'Лев Козерог': [67, 63, 55], 'Лев Водолей': [64, 91, 71],
                            'Лев Рыбы': [62, 43, 27], 'Дева Овен': [36, 28, 15], 'Дева Телец': [92, 95, 97],
                            'Дева Близнецы': [33, 62, 79], 'Дева Рак': [81, 94, 75], 'Дева Лев': [57, 44, 92],
                            'Дева Дева': [81, 98, 95], 'Дева Весы': [35, 10, 77], 'Дева Скорпион': [90, 87, 95],
                            'Дева Стрелец': [38, 36, 24], 'Дева Козерог': [94, 97, 86], 'Дева Водолей': [53, 25, 38],
                            'Дева Рыбы': [16, 67, 58], 'Весы Овен': [96, 82, 58], 'Весы Телец': [73, 87, 90],
                            'Весы Близнецы': [91, 86, 94], 'Весы Рак': [64, 52, 43], 'Весы Лев': [98, 82, 89],
                            'Весы Дева': [24, 17, 85], 'Весы Весы': [90, 78, 47], 'Весы Скорпион': [38, 23, 35],
                            'Весы Стрелец': [98, 83, 94], 'Весы Козерог': [53, 67, 88], 'Весы Водолей': [98, 87, 92],
                            'Весы Рыбы': [28, 41, 76], 'Скорпион Овен': [88, 15, 83], 'Скорпион Телец': [61, 95, 90],
                            'Скорпион Близнецы': [47, 72, 95], 'Скорпион Рак': [84, 88, 91],
                            'Скорпион Лев': [69, 39, 76], 'Скорпион Дева': [88, 97, 94], 'Скорпион Весы': [44, 39, 48],
                            'Скорпион Скорпион': [77, 52, 28], 'Скорпион Стрелец': [65, 13, 81],
                            'Скорпион Козерог': [90, 96, 84], 'Скорпион Водолей': [73, 53, 39],
                            'Скорпион Рыбы': [85, 98, 95], 'Стрелец Овен': [92, 88, 97], 'Стрелец Телец': [17, 52, 47],
                            'Стрелец Близнецы': [78, 90, 84], 'Стрелец Рак': [61, 47, 18], 'Стрелец Лев': [99, 88, 93],
                            'Стрелец Дева': [21, 43, 15], 'Стрелец Весы': [86, 80, 78],
                            'Стрелец Скорпион': [56, 17, 34], 'Стрелец Стрелец': [98, 95, 90],
                            'Стрелец Козерог': [64, 25, 80], 'Стрелец Водолей': [98, 91, 86],
                            'Стрелец Рыбы': [11, 68, 24], 'Козерог Овен': [64, 77, 96], 'Козерог Телец': [93, 88, 90],
                            'Козерог Близнецы': [16, 45, 57], 'Козерог Рак': [64, 21, 36], 'Козерог Лев': [72, 79, 55],
                            'Козерог Дева': [88, 83, 90], 'Козерог Весы': [85, 32, 90],
                            'Козерог Скорпион': [93, 41, 68], 'Козерог Стрелец': [16, 10, 77],
                            'Козерог Козерог': [92, 75, 86], 'Козерог Водолей': [24, 35, 89],
                            'Козерог Рыбы': [90, 94, 22], 'Водолей Овен': [85, 98, 93], 'Водолей Телец': [14, 69, 77],
                            'Водолей Близнецы': [93, 95, 71], 'Водолей Рак': [18, 26, 10], 'Водолей Лев': [41, 83, 56],
                            'Водолей Дева': [28, 16, 10], 'Водолей Весы': [98, 79, 85],
                            'Водолей Скорпион': [36, 17, 41], 'Водолей Стрелец': [92, 80, 89],
                            'Водолей Козерог': [26, 20, 53], 'Водолей Водолей': [73, 95, 45],
                            'Водолей Рыбы': [52, 91, 38], 'Рыбы Овен': [16, 34, 12], 'Рыбы Телец': [84, 78, 62],
                            'Рыбы Близнецы': [19, 55, 27], 'Рыбы Рак': [77, 80, 62], 'Рыбы Лев': [16, 54, 35],
                            'Рыбы Дева': [61, 56, 33], 'Рыбы Весы': [23, 40, 85], 'Рыбы Скорпион': [90, 88, 95],
                            'Рыбы Стрелец': [21, 76, 43], 'Рыбы Козерог': [93, 84, 27], 'Рыбы Водолей': [63, 85, 18],
                            'Рыбы Рыбы': [70, 84, 33]}

@bot.message_handler(commands=['start'])
def send_keyboard(message, text="Привет, чем я могу тебе помочь?"):
    global last_call
    keyboard = types.ReplyKeyboardMarkup(row_width=2)  # наша клавиатура
    itembtn1 = types.KeyboardButton('Узнать свой знак зодиака') # создадим кнопку
    itembtn2 = types.KeyboardButton('Гороскоп на день')
    itembtn3 = types.KeyboardButton('Гадание на любовь по имени')
    itembtn4 = types.KeyboardButton('Самая сильная совместимость')
    itembtn5 = types.KeyboardButton('Совместимость двух знаков')
    itembtn6 = types.KeyboardButton('Совместимость знака со всеми знаками') #график
    itembtn7 = types.KeyboardButton('Общая совместимость')  # график
    keyboard.add(itembtn1, itembtn2)
    keyboard.add(itembtn3, itembtn4, itembtn5, itembtn6)
    keyboard.add(itembtn7)
    msg = bot.send_message(message.from_user.id, text=text, reply_markup=keyboard)
    bot.register_next_step_handler(msg, callback_worker)


def callback_worker( call):
    global dictionary_znaki
    global last_call

    if call.text == 'Гадание на любовь по имени':
        msg = bot.send_message(call.chat.id, 'Введите имя')
        last_call = 'Гадание на любовь по имени'

    elif call.text == 'Гороскоп на день':
        msg = bot.send_message(call.chat.id, 'Введите знак зодиака с большой буквы')
        last_call = 'Гороскоп на день'

    elif call.text == 'Узнать свой знак зодиака':
        msg = bot.send_message(call.chat.id, 'Введите дату в формате ДД.ММ.ГГГГ')
        last_call = 'Узнать свой знак зодиака'


    elif call.text == 'Совместимость двух знаков':
        msg = bot.send_message(call.chat.id, 'Выпишите знак женщины зодиака c большой буквы и знак мужчины с большой буквы в формате: Овен Козерог')
        last_call = 'Совместимость двух знаков'

    elif call.text == 'Самая сильная совместимость':
        msg = bot.send_message(call.chat.id, 'Введите знак зодиака с большой буквы')
        last_call = 'Самая сильная совместимость'

    elif call.text == 'Совместимость знака со всеми знаками':
        msg = bot.send_message(call.chat.id, 'Введите знак зодиака с большой буквы')
        last_call = 'Совместимость знака со всеми знаками'

    elif call.text == 'Общая совместимость':
        msg = bot.send_message(call.chat.id, 'Введите знак зодиака с большой буквы')
        last_call = 'Общая совместимость'


@bot.message_handler(content_types=['text'])
def handle_text(message):
    global last_call
    global dictionary_znaki
    if last_call == 'Гадание на любовь по имени':
        url = 'https://www.predskazanie.ru/aforizmi/?go=do&act=l'
        rez = requests.get(url)
        soup = BeautifulSoup(rez.content)
        phrase = soup.find_all('div', {'class': 'result-text-wide'})[0].text
        bot.send_message(message.from_user.id, text=phrase)

    elif last_call == 'Гороскоп на день':
        url = 'https://my-calend.ru/goroskop'
        rez = requests.get(url)
        soup = BeautifulSoup(rez.content)
        if message.text == 'Козерог':
            i = 9
        if message.text == 'Водолей':
            i = 10
        if message.text == 'Рыбы':
            i = 11
        if message.text == 'Овен':
            i = 0
        if message.text == 'Телец':
            i = 1
        if message.text == 'Близнецы':
            i = 2
        if message.text == 'Рак':
            i = 3
        if message.text == 'Лев':
            i = 4
        if message.text == 'Дева':
            i = 5
        if message.text == 'Весы':
            i = 6
        if message.text == 'Скорпион':
            i = 7
        if message.text == 'Стрелец':
            i = 8
        phrase = soup.find_all('div', {'class': 'goroskop-items-description'})[i].text
        phrase = phrase.split(' ')
        phrase = phrase[1:]
        s = ' '
        phrase = s.join(phrase)
        bot.send_message(message.from_user.id, text=phrase)

    elif last_call == 'Узнать свой знак зодиака':

        msg = message
        (msg.text) = (msg.text).split('.')
        if int(msg.text[1]) == 1:
            if int(msg.text[0]) <= 19:
                bot.send_message(msg.from_user.id, text='Козерог')
            else:
                bot.send_message(msg.from_user.id, text='Водолей')
        if int(msg.text[1]) == 2:
            if int(msg.text[0]) <= 18:
                bot.send_message(msg.from_user.id, text='Водолей')
            else:
                bot.send_message(msg.from_user.id, text='Рыбы')
        if int(msg.text[1]) == 3:
            if int(msg.text[0]) <= 20:
                bot.send_message(msg.from_user.id, text='Рыбы')
            else:
                bot.send_message(msg.from_user.id, text='Овен')
        if int(msg.text[1]) == 4:
            if int(msg.text[0]) <= 20:
                bot.send_message(msg.from_user.id, text='Овен')
            else:
                bot.send_message(msg.from_user.id, text='Телец')
        if int(msg.text[1]) == 5:
            if int(msg.text[0]) <= 20:
                bot.send_message(msg.from_user.id, text='Телец')
            else:
                bot.send_message(msg.from_user.id, text='Близнецы')
        if int(msg.text[1]) == 6:
            if int(msg.text[0]) <= 20:
                bot.send_message(msg.from_user.id, text='Близнецы')
            else:
                bot.send_message(msg.from_user.id, text='Рак')
        if int(msg.text[1]) == 7:
            if int(msg.text[0]) <= 22:
                bot.send_message(msg.from_user.id, text='Рак')
            else:
                bot.send_message(msg.from_user.id, text='Лев')
        if int(msg.text[1]) == 8:
            if int(msg.text[0]) <= 22:
                bot.send_message(msg.from_user.id, text='Лев')
            else:
                bot.send_message(msg.from_user.id, text='Дева')
        if int(msg.text[1]) == 9:
            if int(msg.text[0]) <= 23:
                bot.send_message(msg.from_user.id, text='Дева')
            else:
                bot.send_message(msg.from_user.id, text='Весы')
        if int(msg.text[1]) == 10:
            if int(msg.text[0]) <= 23:
                bot.send_message(msg.from_user.id, text='Весы')
            else:
                bot.send_message(msg.from_user.id, text='Скорпион')
        if int(msg.text[1]) == 11:
            if int(msg.text[0]) <= 21:
                bot.send_message(msg.from_user.id, text='Скорпион')
            else:
                bot.send_message(msg.from_user.id, text='Стрелец')
        if int(msg.text[1]) == 12:
            if int(msg.text[0]) <= 21:
                bot.send_message(msg.from_user.id, text='Стрелец')
            else:
                bot.send_message(msg.from_user.id, text='Козерог')

    elif last_call == 'Самая сильная совместимость':
        l = []
        msg2 = message
        for k, v in dictionary_znaki.items():
            if k == (msg2.text + ' Овен'):
                l.append(v[0])
            if k == (msg2.text + ' Телец'):
                l.append(v[0])
            if k == (msg2.text + ' Близнецы'):
                l.append(v[0])
            if k == (msg2.text + ' Рак'):
                l.append(v[0])
            if k == (msg2.text + ' Лев'):
                l.append(v[0])
            if k == (msg2.text + ' Дева'):
                l.append(v[0])
            if k == (msg2.text + ' Весы'):
                l.append(v[0])
            if k == (msg2.text + ' Скорпион'):
                l.append(v[0])
            if k == (msg2.text + ' Стрелец'):
                l.append(v[0])
            if k == (msg2.text + ' Козерог'):
                l.append(v[0])
            if k == (msg2.text + ' Водолей'):
                l.append(v[0])
            if k == (msg2.text + ' Рыбы'):
                l.append(v[0])
        m = max(l)
        for k, v in dictionary_znaki.items():
            if (k.split()[0] == msg2.text) and (v[0] == m):
                ans = k.split()[1]
        bot.send_message(message.from_user.id, text=("Этот знак наиболее совместим со знаком " + ans + ' (' + str(m) + '%)'))

    elif last_call == 'Совместимость двух знаков':
        msg = message
        sovmestno = dictionary_znaki.get((msg.text))
        bot.send_message(message.from_user.id, text=('Любовь и брак - ' + str(sovmestno[0]) + '%\nДружба - ' + str(sovmestno[1]) + '%\nРабота - ' + str( sovmestno[2]) + '%\n'))

    elif last_call == "Совместимость знака со всеми знаками":
        msg = message
        sovmestno = (msg.text) + ' Овен'
        l = dictionary_znaki.get(sovmestno)
        sovm = dict()
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Телец'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = lsovmestno = (msg.text) + ' Близнецы'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Рак'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Лев'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Дева'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Весы'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Скорпион'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Стрелец'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Козерог'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Водолей'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Рыбы'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        names = []
        loving = []
        friendship = []
        work = []
        for i in sovm:
            names.append(i)
            loving.append(sovm.get(i)[0])
            friendship.append(sovm.get(i)[1])
            work.append(sovm.get(i)[2])
        import pandas as pd
        df = pd.DataFrame({"Знак": names,
                           "Любовь и брак": loving,
                           "Дружба": friendship,
                           "Работа": work})
        df.set_index('Знак', inplace=True)
        import seaborn as sns
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 10))
        df.plot(kind="bar")
        title = 'Совместимость знака' + msg.text + ' cо всеми знаками зодиака'
        plt.title(title, fontsize= 5)
        print('hhhhh')
        plt.savefig('saved_figure.pdf')
        bot.send_photo(message.from_user.id, open('saved_figure.pdf', 'rb'))

    elif last_call  == 'Общая совместимость':
        msg = message
        sovmestno = (msg.text) + ' Овен'
        l = dictionary_znaki.get(sovmestno)
        sovm = dict()
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Телец'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = lsovmestno = (msg.text) + ' Близнецы'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Рак'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Лев'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Дева'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Весы'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Скорпион'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Стрелец'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Козерог'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Водолей'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        sovmestno = (msg.text) + ' Рыбы'
        l = dictionary_znaki.get(sovmestno)
        sovm[sovmestno] = l
        names = []
        loving = []
        friendship = []
        work = []
        total = []
        for i in sovmestimosti:
            names.append(i)
            loving.append(sovmestimosti.get(i)[0])
            friendship.append(sovmestimosti.get(i)[1])
            work.append(sovmestimosti.get(i)[2])
            total.append(float(sovmestimosti.get(i)[0] + sovmestimosti.get(i)[1] + sovmestimosti.get(i)[2])/3)
        import pandas as pd
        df = pd.DataFrame({"znak": names,
                           "Любовь и брак" : loving,
                           "Дружба" : friendship,
                           "Работа" : work,
                           "Общий" : total})
        df.set_index('znak', inplace=True)
        fig, ax = plt.subplots(figsize = (30,50))
        color_graph = ax.scatter(love, friendship, s = df['Общий']*25, c = work, cmap = 'inferno', alpha = 0.5, linewidth = 0)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_xlabel('Любовь и брак', fontsize = 30)
        ax.set_ylabel('Дружба', fontsize = 30)
        plt.colorbar(color_graph);
        for i, znak  in enumerate(names):
            ax.annotate(znak, (df['Любовь и брак'][i], df['Дружба'][i]), fontsize = 20)
        plt.savefig('saved_figure.png')
        bot.send_photo(message.from_user.id, open('saved_figure.pdf', 'rb'))


    send_keyboard(message, "Чем еще могу помочь?")

bot.polling(none_stop=True)

