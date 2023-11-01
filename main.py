import telebot
from telebot import types

import re

bot = telebot.TeleBot('6792133211:AAGWiPd5bptiZy9DMaysYagf2FoTLtGsF8E')




@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text ="🖥️ ZAK/OPER | (Компьютер ЗА/разборщика)", callback_data="ZAK")
    btn2 = types.InlineKeyboardButton(text ='🖥️ SRV/KAS | (Компьютер касса-сервер/касса)', callback_data='SRV')
    btn3 = types.InlineKeyboardButton(text ="Другая причина", callback_data='other')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.from_user.id, "👋 Здравствуйте, я новый бот помощник." 
                                           "\nПомогу оперативнее разобраться с возникшей проблемой в Вашей аптеке"
                                           "\nP.S. Я еще совсем мал, но очень активно развиваюсь благодаря нашему отделу ИТ"
                                           "\nСпасибо за понимание."
                                           "\n\n\n Выберете из списка ниже компьютер с которым возникли проблемы", reply_markup=markup)

#Функция отчистки чата
@bot.message_handler(commands=['clear'])
def clear_chat(message):
    chat_id = message.chat.id
    message_id = message.message_id

    # Получаем список всех сообщений в чате
    messages = bot.fetch_all(chat_id)

    # Удаляем каждое сообщение
    for m in messages:
        bot.delete_message(chat_id, m.message_id)

    # Удаляем сообщение, которое отправил пользователь
    bot.delete_message(chat_id, message_id)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    #Кнопки проблем пк ЗА
    if callback.data == 'ZAK':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Не работает Skype", callback_data='Skype')
        btn2 = types.InlineKeyboardButton('Не работает почта', callback_data='Outlook')
        btn3 = types.InlineKeyboardButton('Проблема с принтером', callback_data='Printers')
        btn4 = types.InlineKeyboardButton('Проблема удаленного доступа', callback_data='RMS')
        btn5 = types.InlineKeyboardButton('Проблема со сканером товара', callback_data='barcode')
        btn6 = types.InlineKeyboardButton('Не работают наушники', callback_data='headph')
        btn7 = types.InlineKeyboardButton('Оборудование вышло из строя', callback_data='break')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        markup.row(btn7)
        bot.send_message(callback.message.chat.id, 'Какая проблема на Вашем компьютере? из этого списка.', reply_markup=markup)

    # Кнопки проблем пк СРВ
    elif callback.data == 'SRV':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Проблема со сканером товара', callback_data='barcode')
        btn2 = types.InlineKeyboardButton('Не работает безналичный расчет', callback_data='sber')
        btn3 = types.InlineKeyboardButton('Не работают бонусные карты', callback_data='bk')
        btn4 = types.InlineKeyboardButton('Проблема с интернетом', callback_data='no_link')
        btn5 = types.InlineKeyboardButton('Проблемы с кассой. (ККТ/Кассовый апарат/*дописать*', callback_data='KKT')
        #btn6 = types.InlineKeyboardButton('////', callback_data='')
        btn7 = types.InlineKeyboardButton('Оборудование вышло из строя', callback_data='break')
        #btn8 = types.InlineKeyboardButton('НАЗАД',)
        markup.add(btn1, btn2, btn3, btn4, btn5)
        markup.row(btn7)
       # markup.row(btn8)
        bot.send_message(callback.message.chat.id, 'Какая проблема на Вашем компьютере? из этого списка.',
                         reply_markup=markup)
        #bot.send_message(callback.message.chat.id, 'Какая проблема на компьютере? из этого списка.',
        #                 reply_markup=markup)
    elif callback.data == 'Skype':
        #clear_chat(message)
        bot.send_message(callback.message.chat.id, '''❗Если возникла проблема со скайпом:'''
                                                   'Проверьте пожалуйста запущено ли приложение skype '
                                                   'на вашем компьютере. В правом нижнем углу должна '
                                                   'отображаться иконка программы. Если ее нет, нужно '
                                                   'запустить приложение из меню ПУСК (левый нижний улол) либо '
                                                   'с помощью ярклыка на рабочем столе.'
                                                   '\n\n\n Если моей помощи оказалось недостаточно, '
                                                   'напишите номер аптеки. Я передам, и специалист свяжется '
                                                   'в ближайшее время😉')
        #здесь нужно вызвать функцию number_apt
    elif callback.data == 'barcode':
        bot.send_message(callback.message.chat.id, '''❗Если возникла проблема со сканером товара:'''
                                                   '\nДля начала, давайте проверим кабель от сканера до '
                                                   'системного блока.'
                                                   '\nВажно что бы разъем куда подключен сканер не '
                                                   'болтался, и кабель был плотно подключен к соответствующему '
                                                   'разъему (USB) системного блока'
                                                   '\nЕсли это не так, попробуйте переподключить кабель в другой '
                                                   '(соседний/аналогичный) разъём.'
                                                   '\n\n\n Если моей помощи оказалось недостаточно, или иная '
                                                   'проблема со сканером '
                                                   'напишите номер аптеки. Я передам, и специалист свяжется '
                                                   'в ближайшее время😉')
        # здесь нужно вызвать функцию number_apt
    elif callback.data == 'Outlook':
        bot.send_message(callback.message.chat.id, '''❗Если возникла проблема с почтой:'''
                                                   '\nПопробуйте перезапустить приложение почты. И обратите '
                                                   'внимание на самую нижнюю строчку в окне программы. '
                                                   'Если там упоминается требование пароля, нажмите и введите данные: '
                                                   '\n  логин: mz\\nsk_mz_а[НОМЕР АПТЕКИ]'
                                                   '\n пароль: Gjhjcz3001 (Порося 3001)'
                                                   '\n\n\n Если моей помощи оказалось недостаточно, '
                                                   'напишите номер аптеки. Я передам, и специалист свяжется '
                                                   'в ближайшее время😉')
        # здесь нужно вызвать функцию number_apt
    elif callback.data == 'RMS':
        bot.send_message(callback.message.chat.id, '''❗Если у вас не работает удаленный доступ:'''
                                                   '\n Для начала нам необходимо закрыть работающую программу (Viewer) '
                                                   'После этого перезапустить программу, '
                                                   '\n далее важно обратить внимание на правый верхний угол '
                                                   'программы.\n'
                                                   'Там в прямоугольной рамке должен быть написан логин по типу: '
                                                   '\nNsk_zav[цифры].'
                                                   '\nЕсли же вместо этого изображена кнопка, ВХОД '
                                                   'Нажимаем на неё и подтверждаем вход.'
                                                   '\nВ большенстве случаев Ваша проблема будет решена с помощью '
                                                   'этих простых действий'
                                                   '\n\n\n Если у Ваша проблема иного характера '
                                                   'напишите номер аптеки. Я передам, и специалист свяжется '
                                                   'в ближайшее время😉')
        # здесь нужно вызвать функцию number_apt
    elif callback.data == 'other':
        bot.send_message(callback.from_user.id, "Хорошо, сейчас разберемся. Напишите номер аптеки, где столкнулись с проблемой")

        # number_apt()

@bot.message_handler()
def number_apt (message):
    #Определение номера аптеки из сообщения
    i=0
    num = ''
    while i<=len(message.text):
        #print (f'!итерация внешенего цикла: {i}')
        while i < len(message.text) and '0'<= message.text[i] <='9':
            num += message.text[i]
            i += 1
        else:
            num += ' '
            i += 1
    number_apt = num.split()
    print (f'номер аптеки {number_apt}')
    if number_apt != 0 and len(number_apt) == 1:
        print(f'определенный номер аптеки: {number_apt[0]}')
        bot.send_message(message.from_user.id, f'Понял аптека {number_apt}')


    else:
        print(f'В тексте больше цифр, введите снова!\n {number_apt}')
        bot.send_message(message.from_user.id, "Не разобрал, какой номер. Попробуйте иначе. \n пример: Аптека 34 \n А34 \n 34-ая аптека \nи т.д ")






bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть