from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, Filter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keyboards as kb
import app.database.requests as rq
from config import ADMINS

admin = Router()


class DeleteLoan(StatesGroup):
    loan = State()
    confirm = State()


class Newsletter(StatesGroup):
    letter = State()


class AdminProtect(Filter):
    async def __call__(self, message: Message):
        return message.from_user.id in ADMINS


@admin.message(AdminProtect(), Command('apanel'))
async def apanel(message: Message):
    await message.answer(f'Привет, администратор {message.from_user.first_name}!\n\n Твои возможные команды: \n/delete_loans (удалить существующую бронь)\n/see_loans (посмотреть активные брони)\n/newsletter (отправить сообщение всем пользователям)')



@admin.message(AdminProtect(), Command('see_loans'))
async def see_loans(message: Message):
    loans = await rq.see_loans()
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

        user_name = await rq.get_user_tg_name(loan.user)
        await message.answer(f'День недели: {day}, Время: {hour}, Пользователь: {user_name}')
    await message.answer(f'Администратор, {message.from_user.first_name}!\nЭто все брони. Если спиоск броней не появился, это означает, что никто из пользователей еще не оформил бронь.')


@admin.message(AdminProtect(), Command('delete_loans'))
async def cancel_loans(message: Message, state:FSMContext):
    await state.set_state(DeleteLoan.loan)
    await message.answer(f'Администратор, {message.from_user.first_name}!\nВыбери бронь, которую хочешь отменить: (Если список с активными бронями не появился, это означает, что никто из пользователей еще не оформил бронь)',
                         reply_markup=await kb.get_loans())
    


@admin.message(AdminProtect(), DeleteLoan.loan)
async def loan(message: Message, state:FSMContext):
    await state.update_data(loan = message.text)
    await state.set_state(DeleteLoan.confirm)
    await message.answer(f'Администратор, {message.from_user.first_name}!\nПодтверждаешь отмену?', 
                         reply_markup=kb.need_ball)
    


@admin.message(AdminProtect(), DeleteLoan.confirm)
async def confirm(message: Message, state:FSMContext):
    await state.update_data(confirm = message.text)
    data = await state.get_data()
    if data['confirm'] == 'Да':
        day_str = data['loan'].split(' ')[0].lower()
        day_int = await rq.get_day_id(day_str)
        hour_str = data['loan'].split(' ')[1]
        hour_int = await rq.get_hour_id(hour_str)
        await rq.cancel_loans(day_int, hour_int)
        await message.answer(f'Администратор, {message.from_user.first_name}!\nБронь отменена, теперь дата: {day_str} {hour_str} снова свободна для бронирования пользователями.')
    elif data['confirm'] == 'Нет':
        await message.answer(f'Администратор, {message.from_user.first_name}!\nОперация отменена.')
    await state.clear()


@admin.message(AdminProtect(), Command('newsletter'))
async def newsletter(message: Message, state: FSMContext):
    await state.set_state(Newsletter.letter)
    await message.answer(f'Администратор, {message.from_user.first_name}!\nДанная команда позволит тебе отправить сообщение всем пользователям, которые прошли регистрацию в боте (оформили бронь).\nВведи сообщение для рассылки:')


@admin.message(AdminProtect(), Newsletter.letter)
async def newsletter_message(message: Message, state:FSMContext):
    await message.answer('Рассылка началась.')
    users = await rq.get_users()
    for user in users:
        try:
            await message.send_copy(chat_id=user.tg_id)
        except Exception as e:
            print(e)
    await message.answer('Рассылка завершена.')
    await state.clear()
     