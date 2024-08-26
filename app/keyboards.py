from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
# импорт билдера для вывода данных из БД
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import app.database.requests as rq


play_basket_reply = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Играть в баскетбол на Шаболовке')]
], input_field_placeholder='Нажмите на кнопку',
resize_keyboard=True,
one_time_keyboard=True)


play_basket_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Хочу поиграть в баскетбол на Шаболовке', callback_data='play_basket')]
])


reg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пройти регистрацию', callback_data='reg')]
])


confirm_reg = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Принять')],
    [KeyboardButton(text='Отказаться')]
])


need_ball = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Да')],
    [KeyboardButton(text='Нет')]
])


attribute = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='ФИО name')],
    [KeyboardButton(text='ОП program')],
    [KeyboardButton(text='Курс course')],
    [KeyboardButton(text='Телеграм tg_name')]
])


confirm = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Принять')], [KeyboardButton(text='Отказаться')]
], input_field_placeholder='Нажмите на кнопку',
resize_keyboard=True,
one_time_keyboard=True)


"""
Свободные дни и времена:

Keyword arguments:
argument -- description
Return: return_description
"""


async def get_days():
    keyboard = ReplyKeyboardBuilder()
    days = await rq.get_free_days()
    for day in days:
        keyboard.add(KeyboardButton(text=day))
    return keyboard.adjust(1).as_markup()


async def get_times(day:str):
    keyboard = ReplyKeyboardBuilder()
    times = await rq.get_free_hours(day)
    for time in times:
        keyboard.add(KeyboardButton(text=time))
    return keyboard.adjust(1).as_markup()



"""
Брони для пользователя

Keyword arguments:
argument -- description
Return: return_description
"""


async def get_loan(user_id: int):
    keyboard = ReplyKeyboardBuilder()
    loans = await rq.see_loan(user_id)
    for loan in loans:

        if loan.day == 1:

            if loan.hour == 1:
                day = 'Понедельник'
                hour = '11:00'
            elif loan.hour == 2:
                day = 'Понедельник'
                hour = '12:00'
            elif loan.hour == 3:
                day = 'Понедельник'
                hour = '13:00'
            elif loan.hour == 4:
                day = 'Понедельник'
                hour = '14:00'
            elif loan.hour == 5:
                day = 'Понедельник'
                hour = '15:00'
            elif loan.hour == 6:
                day = 'Понедельник'
                hour = '16:00'
            elif loan.hour == 7:
                day = 'Понедельник'
                hour = '17:00'
            elif loan.hour == 8:
                day = 'Понедельник'
                hour = '18:00'
            elif loan.hour == 9:
                day = 'Понедельник'
                hour = '19:00'

        elif loan.day == 2:

            if loan.hour == 1:
                day = 'Вторник'
                hour = '11:00'
            elif loan.hour == 2:
                day = 'Вторник'
                hour = '12:00'
            elif loan.hour == 3:
                day = 'Вторник'
                hour = '13:00'
            elif loan.hour == 4:
                day = 'Вторник'
                hour = '14:00'
            elif loan.hour == 5:
                day = 'Вторник'
                hour = '15:00'
            elif loan.hour == 6:
                day = 'Вторник'
                hour = '16:00'
            elif loan.hour == 7:
                day = 'Вторник'
                hour = '17:00'
            elif loan.hour == 8:
                day = 'Вторник'
                hour = '18:00'
            elif loan.hour == 9:
                day = 'Вторник'
                hour = '19:00'

        elif loan.day == 3:

            if loan.hour == 1:
                day = 'Среда'
                hour = '11:00'
            elif loan.hour == 2:
                day = 'Среда'
                hour = '12:00'
            elif loan.hour == 3:
                day = 'Среда'
                hour = '13:00'
            elif loan.hour == 4:
                day = 'Среда'
                hour = '14:00'
            elif loan.hour == 5:
                day = 'Среда'
                hour = '15:00'
            elif loan.hour == 6:
                day = 'Среда'
                hour = '16:00'
            elif loan.hour == 7:
                day = 'Среда'
                hour = '17:00'
            elif loan.hour == 8:
                day = 'Среда'
                hour = '18:00'
            elif loan.hour == 9:
                day = 'Среда'
                hour = '19:00'

        elif loan.day == 4:

            if loan.hour == 1:
                day = 'Четверг'
                hour = '11:00'
            elif loan.hour == 2:
                day = 'Четверг'
                hour = '12:00'
            elif loan.hour == 3:
                day = 'Четверг'
                hour = '13:00'
            elif loan.hour == 4:
                day = 'Четверг'
                hour = '14:00'
            elif loan.hour == 5:
                day = 'Четверг'
                hour = '15:00'
            elif loan.hour == 6:
                day = 'Четверг'
                hour = '16:00'
            elif loan.hour == 7:
                day = 'Четверг'
                hour = '17:00'
            elif loan.hour == 8:
                day = 'Четверг'
                hour = '18:00'
            elif loan.hour == 9:
                day = 'Четверг'
                hour = '19:00'

        elif loan.day == 5:

            if loan.hour == 1:
                day = 'Пятница'
                hour = '11:00'
            elif loan.hour == 2:
                day = 'Пятница'
                hour = '12:00'
            elif loan.hour == 3:
                day = 'Пятница'
                hour = '13:00'
            elif loan.hour == 4:
                day = 'Пятница'
                hour = '14:00'
            elif loan.hour == 5:
                day = 'Пятница'
                hour = '15:00'
            elif loan.hour == 6:
                day = 'Пятница'
                hour = '16:00'
            elif loan.hour == 7:
                day = 'Пятница'
                hour = '17:00'
            elif loan.hour == 8:
                day = 'Пятница'
                hour = '18:00'
            elif loan.hour == 9:
                day = 'Пятница'
                hour = '19:00'
                
        keyboard.add(KeyboardButton(text=f'{day} {hour}'))
    return keyboard.adjust(1).as_markup()


'''
cars = ['Tesla', 'BMW', 'Mersedes']

async def get_cars():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(1).as_markup()
'''


async def get_loans():
    keyboard = ReplyKeyboardBuilder()
    users = await rq.get_users()
    for user in users:
        loans = await rq.see_loan(user.tg_id)
        for loan in loans:
            if loan.day == 1:

                if loan.hour == 1:
                    day = 'Понедельник'
                    hour = '11:00'
                elif loan.hour == 2:
                    day = 'Понедельник'
                    hour = '12:00'
                elif loan.hour == 3:
                    day = 'Понедельник'
                    hour = '13:00'
                elif loan.hour == 4:
                    day = 'Понедельник'
                    hour = '14:00'
                elif loan.hour == 5:
                    day = 'Понедельник'
                    hour = '15:00'
                elif loan.hour == 6:
                    day = 'Понедельник'
                    hour = '16:00'
                elif loan.hour == 7:
                    day = 'Понедельник'
                    hour = '17:00'
                elif loan.hour == 8:
                    day = 'Понедельник'
                    hour = '18:00'
                elif loan.hour == 9:
                    day = 'Понедельник'
                    hour = '19:00'

            elif loan.day == 2:

                if loan.hour == 1:
                    day = 'Вторник'
                    hour = '11:00'
                elif loan.hour == 2:
                    day = 'Вторник'
                    hour = '12:00'
                elif loan.hour == 3:
                    day = 'Вторник'
                    hour = '13:00'
                elif loan.hour == 4:
                    day = 'Вторник'
                    hour = '14:00'
                elif loan.hour == 5:
                    day = 'Вторник'
                    hour = '15:00'
                elif loan.hour == 6:
                    day = 'Вторник'
                    hour = '16:00'
                elif loan.hour == 7:
                    day = 'Вторник'
                    hour = '17:00'
                elif loan.hour == 8:
                    day = 'Вторник'
                    hour = '18:00'
                elif loan.hour == 9:
                    day = 'Вторник'
                    hour = '19:00'

            elif loan.day == 3:

                if loan.hour == 1:
                    day = 'Среда'
                    hour = '11:00'
                elif loan.hour == 2:
                    day = 'Среда'
                    hour = '12:00'
                elif loan.hour == 3:
                    day = 'Среда'
                    hour = '13:00'
                elif loan.hour == 4:
                    day = 'Среда'
                    hour = '14:00'
                elif loan.hour == 5:
                    day = 'Среда'
                    hour = '15:00'
                elif loan.hour == 6:
                    day = 'Среда'
                    hour = '16:00'
                elif loan.hour == 7:
                    day = 'Среда'
                    hour = '17:00'
                elif loan.hour == 8:
                    day = 'Среда'
                    hour = '18:00'
                elif loan.hour == 9:
                    day = 'Среда'
                    hour = '19:00'

            elif loan.day == 4:

                if loan.hour == 1:
                    day = 'Четверг'
                    hour = '11:00'
                elif loan.hour == 2:
                    day = 'Четверг'
                    hour = '12:00'
                elif loan.hour == 3:
                    day = 'Четверг'
                    hour = '13:00'
                elif loan.hour == 4:
                    day = 'Четверг'
                    hour = '14:00'
                elif loan.hour == 5:
                    day = 'Четверг'
                    hour = '15:00'
                elif loan.hour == 6:
                    day = 'Четверг'
                    hour = '16:00'
                elif loan.hour == 7:
                    day = 'Четверг'
                    hour = '17:00'
                elif loan.hour == 8:
                    day = 'Четверг'
                    hour = '18:00'
                elif loan.hour == 9:
                    day = 'Четверг'
                    hour = '19:00'

            elif loan.day == 5:

                if loan.hour == 1:
                    day = 'Пятница'
                    hour = '11:00'
                elif loan.hour == 2:
                    day = 'Пятница'
                    hour = '12:00'
                elif loan.hour == 3:
                    day = 'Пятница'
                    hour = '13:00'
                elif loan.hour == 4:
                    day = 'Пятница'
                    hour = '14:00'
                elif loan.hour == 5:
                    day = 'Пятница'
                    hour = '15:00'
                elif loan.hour == 6:
                    day = 'Пятница'
                    hour = '16:00'
                elif loan.hour == 7:
                    day = 'Пятница'
                    hour = '17:00'
                elif loan.hour == 8:
                    day = 'Пятница'
                    hour = '18:00'
                elif loan.hour == 9:
                    day = 'Пятница'
                    hour = '19:00'
                    
            keyboard.add(KeyboardButton(text=f'{day} {hour} {user.tg_name}'))
    return keyboard.adjust(1).as_markup()