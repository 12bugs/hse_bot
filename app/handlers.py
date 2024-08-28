from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import app.keyboards as kb 
import app.database.requests as rq


router = Router()


class User(StatesGroup):
    name = State()
    program = State()
    course = State()
    tg_name = State()
    confirm = State()


class Loan(StatesGroup):
    day = State()
    hour = State()
    need_ball = State()
    confirm = State()


class Cancel(StatesGroup):
    loan = State()
    confirm = State()


class ChangeProfile(StatesGroup):
    desicion = State()
    attribute = State()
    text = State()
    again = State()


"""
Старт

Keyword arguments:
argument -- description
Return: return_description
"""

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=kb.play_basket_inline)


@router.callback_query(F.data == 'play_basket')
async def play_basket(callback: CallbackQuery):
    await callback.answer('Вы нажали на кнопку.')
    tg_id = callback.from_user.id
    users = await rq.get_users()
    l = list()
    for user in users:
        l.append(user.tg_id)
    if tg_id in l:
        await callback.message.answer('Вы зарегистрированы, это здорово!\n\nВозможные команды:\n/see_loan (посмотреть свои активные брони)\n/new_loan (оформить новую бронь)\n/cancel_loan (отменить свою, раннее зарегестрированную бронь)\n/change_profile (изменить данные профиля)')
    else:
        await callback.message.answer('Необходимо пройти регистрацию.', reply_markup=kb.reg)
    


"""
Пользователь зарегистрирован 

Keyword arguments:
argument -- description
Return: return_description
"""

@router.message(Command('change_profile'))
async def change_profile(message: Message, state: FSMContext):
    user = await rq.get_user(message.from_user.id)
    await state.set_state(ChangeProfile.desicion)
    await message.answer(f'Ваши данные:\n\nФИО:{user.name}\nОП:{user.program}\nКурс:{user.course}\nTg_name:{user.tg_name}\n\nХотите изменить данные?',
                         reply_markup=kb.need_ball)


@router.message(ChangeProfile.desicion)
async def change_profile(message: Message, state: FSMContext):
    await state.update_data(desicion=message.text)
    data = await state.get_data()
    if data['desicion'] == 'Да':
        await state.set_state(ChangeProfile.attribute)
        await message.answer('Выберите поле, которое хотите изменить:', 
                             reply_markup=kb.attribute)
    elif data['desicion'] == 'Нет':
        await message.answer('Данные сохранены без изменений.')
        await state.clear()
    

@router.message(ChangeProfile.attribute)
async def change_profile(message: Message, state: FSMContext):
    await state.update_data(attribute = message.text.split(' ')[1])
    await state.set_state(ChangeProfile.text)
    data = await state.get_data()
    await message.answer(f'Введите новое значение для поля {data["attribute"]}:')


@router.message(ChangeProfile.text)
async def change_profile(message: Message, state: FSMContext):  
    await state.update_data(text=message.text)
    data = await state.get_data()
    if data['attribute'] == 'name':
        await rq.change_profile_fio(message.from_user.id, data['text'])
        await state.set_state(ChangeProfile.again)
        await message.answer('Имя успешно изменено. Хотите ли изменить еще что-то?',
                             reply_markup=kb.need_ball)
    elif data['attribute'] == 'program':
        await rq.change_profile_program(message.from_user.id, data['text'])
        await state.set_state(ChangeProfile.again)
        await message.answer('Название ОП успешно изменено. Хотите ли изменить еще что-то?',
                             reply_markup=kb.need_ball)
    elif data['attribute'] == 'course':
        await rq.change_profile_course(message.from_user.id, data['text'])
        await state.set_state(ChangeProfile.again)
        await message.answer('Курс обучения успешно изменен. Хотите ли изменить еще что-то?',
                             reply_markup=kb.need_ball)
    elif data['attribute'] == 'tg_name':
        await rq.change_profile_tg_name(message.from_user.id, data['text'])
        await state.set_state(ChangeProfile.again)
        await message.answer('Ник в TG успешно изменен. Хотите ли изменить еще что-то?',
                             reply_markup=kb.need_ball)


@router.message(ChangeProfile.again)
async def change_profile(message: Message, state: FSMContext): 
    await state.update_data(again=message.text)
    data = await state.get_data()
    if data['again'] == 'Да':
        await state.clear()
        await message.answer('Введите команду /change_profile')
    elif data['again'] == 'Нет':
        user_id = message.from_user.id
        user = await rq.get_user(user_id)
        await message.answer(f'Ваши текущие данные:\n\nФИО:{user.name}\nОП:{user.program}\nКурс:{user.course}\nTG-ник:{user.tg_name}')
        await state.clear()



@router.message(Command('see_loan'))
async def see_loan(message: Message):
    tg_id = message.from_user.id
    loans = await rq.see_loan(tg_id)

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

        await message.answer(f'День недели: {day}, Время: {hour}')
    await message.answer('Это все текущие брони. Если брони не появились, то это значит, что у тебя нет активных броней. Введите команду /new_loan для оформления брони.')



@router.message(Command('new_loan'))
async def new_loan(message:Message, state:FSMContext):
    await state.set_state(Loan.day)
    await message.answer('Выберите свободный день недели для брони: (если не появился список со свободными днями, это означает, что все дни, к сожалению, уже заняты)',
                             reply_markup=await kb.get_days())


@router.message(Command('cancel_loan'))
async def cancel_loan(message: Message, state:FSMContext):
    tg_id = message.from_user.id
    await state.set_state(Cancel.loan)
    await message.answer("Выберите бронь для отмены: (если не появился список с бронями, это ознанчает, что у тебя нет активной брони, введите команду /new_loan для ее оформления)",
                                  reply_markup = await kb.get_loan(tg_id))



@router.message(Cancel.loan)
async def cancel_day(message: Message, state:FSMContext):

    #day = await rq.get_day_id(message.text.split(' ')[0].lower())
    await state.update_data(loan = message.text)
    await state.set_state(Cancel.confirm)
    await message.answer('Подтверждаете отмену?',
                         reply_markup=kb.need_ball)
    
'''
@router.message(Cancel.hour)
async def cancel_hour(message: Message, state:FSMContext):
    hour = await rq.get_hour_id(message.text.split(' ')[1])
    await state.update_data(hour = hour)
    await state.set_state(Cancel.confirm)
    await message.answer('Подтверждаете отмену?',
                         reply_markup=kb.need_ball)
'''

@router.message(Cancel.confirm)
async def cancel_confirm(message:Message, state:FSMContext):
    await state.update_data(confirm = message.text)
    data = await state.get_data()
    if data['confirm'] == 'Да':
        day_str = data['loan'].split(' ')[0].lower()
        day_int = await rq.get_day_id(day_str)
        hour_str = data['loan'].split(' ')[1]
        hour_int = await rq.get_hour_id(hour_str)
        await rq.cancel_loan(message.from_user.id, day_int, hour_int)
        await message.answer(f'Бронь отменена, теперь дата: {data["loan"]} свободна для бронирования другим пользователям')
    elif data['confirm'] == 'Нет':
        await message.answer('Операция отменена')
    await state.clear()



"""
Регистрация и оформление брони

Keyword arguments:
argument -- description
Return: return_description
"""


@router.callback_query(F.data == 'reg')
async def reg_one(callback:CallbackQuery, state:FSMContext):
    await state.set_state(User.name)
    await callback.message.answer('Введите ФИО')


@router.message(User.name)
async def reg_two(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(User.program)
    await message.answer('Введите ОП')


@router.message(User.program)
async def reg_three(message:Message, state:FSMContext):
    await state.update_data(program=message.text)
    await state.set_state(User.course)
    await message.answer('Введите курс обучения')


@router.message(User.course)
async def reg_four(message:Message, state:FSMContext):
    await state.update_data(course=message.text)
    await state.set_state(User.tg_name)
    await message.answer('Введите ник в ТГ для связи (в формате @name):')


@router.message(User.tg_name)
async def reg_five(message:Message, state:FSMContext):
    await state.update_data(tg_name=message.text)
    await state.set_state(User.confirm)
    data = await state.get_data()
    await state.set_state(User.confirm)
    await message.answer(f'ФИО: {data['name']}\nОП: {data["program"]}\nКурс: {data["course"]}\ntg_name: {data["tg_name"]}\n\nПроверьте введенные данные: нажмите ПРИНЯТЬ в случае корректности данных либо ОТКЛОНИТЬ если данные не корректны',
                         reply_markup=kb.confirm_reg)

    #await message.answer('Выберите свободный день недели для брони', 
    #                    reply_markup=await kb.get_days())


@router.message(User.confirm)
async def reg_four(message:Message, state:FSMContext):
    await state.update_data(confirm=message.text)
    data = await state.get_data()
    if data['confirm'] == 'Принять':
        await rq.set_user(message.from_user.id, data['name'], data['program'], data['course'], data['tg_name'])
        await state.clear()
        await state.set_state(Loan.day)
        await message.answer('Вы прошли регистрацию!\nТеперь необходимо оформить бронь\n\nВыберите свободный день недели для брони:',
                             reply_markup=await kb.get_days())
    elif data['confirm'] == 'Отказаться':
        await state.clear()
        await message.answer('Пройдите регистрацию заново',
                             reply_markup=kb.reg)
    #await rq.set_user(message.from_user.id, data['name'], data['program'], data['course'], data['tg_id'])
    #await message.answer(f'Вы прошли регистрацию!\n\nФИО:{data["name"]}\nОП:{data["program"]}\nКурс:{data["course"]}\nНик в ТГ:{data["tg_id"]}\n\nВыберите день недели для брони.', 
    #                     reply_markup=await kb.get_days())
    # await message.answer(text = f'ФИО: {data["name"]}\nОП: {data["program"]}\nКурс: {data["course"]}\ntg_name: {data["tg_name"]}\n\nДень недели: {data["day"]}\nВремя: {data["hour"]}\nНужен инвентарь? {message.text}\n\nПодтверждая бронь времени, вы несете ответственность за происходящее на площадке и инвентарь, который вам предоставил Отдел по работе со студентами', 
    #              reply_markup=kb.confirm)
    

@router.message(Loan.day)
async def reg_six(message:Message, state:FSMContext):
    await state.update_data(day=message.text)
    await state.set_state(Loan.hour)
    await message.answer('Вы выбрали день.\nВыберите свободное время:',
                        reply_markup=await kb.get_times(message.text))


@router.message(Loan.hour)
async def reg_seven(message:Message, state:FSMContext):
    await state.update_data(hour=message.text)
    await state.set_state(Loan.need_ball)
    await message.answer('Вы выбрали время.\n\nНужен ли вам мяч или иной инвентарь от Отдела по работе со студентами? Для использования инвентаря необходимо подойти в 4310 для уточнения его наличия.',
                        reply_markup=kb.need_ball)


@router.message(Loan.need_ball)
async def reg_eight(message:Message, state:FSMContext):
    if message.text == 'Да':
        need_ball = True
    if message.text == 'Нет':
        need_ball = False    
    await state.update_data(need_ball=need_ball)
    data = await state.get_data()
#    await rq.set_user(data['name'], data['program'], data['course'], data['tg_id'])
#    user_id = await rq.get_user_id(data['tg_id'])
#    day_id = await rq.get_day_id(data['day'])
#    hour_id = await rq.get_hour_id(data['hour']) 
#    await rq.update_loan(user_id=user_id, 
#                        day_id=day_id,
#                        hour_id=hour_id,
#                        need_ball=data['need_ball'])
    await state.set_state(Loan.confirm)
    await message.answer(f'День недели: {data["day"]}\nВремя: {data["hour"]}\nНужен инвентарь? {message.text}\n\nПодтверждая бронь времени, вы несете ответственность за происходящее на площадке и инвентарь, который вам предоставил Отдел по работе со студентами.', 
                    reply_markup=kb.confirm)
                  
    #await state.clear()


@router.message(Loan.confirm)
async def reg_nine(message:Message, state:FSMContext):
    await state.update_data(confirm=message.text)
    data = await state.get_data()
    day_id = await rq.get_day_id(data['day'])
    hour_id = await rq.get_hour_id(data['hour'])
    if data['confirm'] == 'Принять': 
        await rq.new_loan(user_id=message.from_user.id, 
                        day_id=day_id,
                        hour_id=hour_id,
                        need_ball=data['need_ball'])
        await message.answer(f'Отлично, твоя бронь зарегистрирована! По подробностям можешь написать Менеджеру Отдела по работе со студентами ВШБ Покидову Егору Сергеевичу @egorchpok')
    if data['confirm'] == 'Отказаться':
        await message.answer('Бронь сброшена.\n\nВведите команду /start для оформления новой брони')
    await state.clear()







'''
@router.callback_query(F.data.startswith('day_'))
async def category(callback: CallbackQuery, state: FSMContext):
    await state.update_data(day = callback.data.split('_')[1])
    await callback.message.answer('Вы выбрали день.\nВыберите свободное время.',
                        reply_markup=await kb.get_times(callback.data.split('_')[1]))
'''

'''
@router.callback_query(User.day)
async def reg_day(callback:CallbackQuery, state:FSMContext):
    await state.update_data(day=callback.data.split('_')[1])
    await message.answer('Вы выбрали день.\nВыберите свободное время.',
                     reply_markup=await kb.get_times(message.text))
'''

'''
@router.callback_query(F.data.startswith('hour_'))
async def category(callback: CallbackQuery, state: FSMContext):
    await state.update_data(hour = callback.data.split('_')[1])
    await callback.message.answer('Вы выбрали время.\n\nНужен ли вам мяч или иной инвентарь от Отдела по работе со студентами? Для использования инвентаря необходимо подойти в 4310 для уточнения его наличия.',
                        reply_markup=kb.need_ball)

'''
'''
@router.callback_query(User.hour)
async def reg_hour(callback: CallbackQuery, state:FSMContext):
    await state.update_data(hour=callback.data.split('_')[1])
    data = await state.get_data()
    await rq.set_user(data['name'], data['program'], data['course'], data['tg_id'])
    user_id = await rq.get_user_id(data['tg_id'])
    day_id = await rq.get_day_id(data['day'])
    hour_id = await rq.get_hour_id(data['hour'])
    await rq.update_loan(user_id=user_id, 
                        day_id=day_id,
                        hour_id=hour_id)
    await callback.message.answer(f'Вы выбрали время и успешно прошли регистрацию')
    await state.clear()
'''

'''
@router.callback_query(F.data == 'yes')
async def ball_yes(callback: CallbackQuery, state:FSMContext):
    await state.update_data(need_ball = True)
    await callback.answer('Вы нажали на кнопку.')
    await callback.message.answer(text = 'Подтверждая бронь времени, вы несете ответственность за происходящее на площадке и инвентарь, который вам предоставил Отдел по работе со студентами', 
                    reply_markup=kb.confirm)


@router.callback_query(F.data == 'no')
async def ball_no(callback: CallbackQuery, state: FSMContext):
    await state.update_data(need_ball = False)
    await callback.answer('Вы нажали на кнопку.')
    await callback.message.answer(text = 'Подтверждая бронь времени, вы несете ответственность за происходящее на площадке и инвентарь, который вам предоставил Отдел по работе со студентами', 
                    reply_markup=kb.confirm)
    
'''


