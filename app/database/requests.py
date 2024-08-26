from app.database.models import User,Time,Day,DayTimeUser
from app.database.models import async_session

from sqlalchemy import select, update


"""

хз что это

"""

# Достаем всех пользователей из БД
async def get_users():
    async with async_session() as session:
        users = await session.scalars(select(User))
    return users


# Достаем дни недели, в которых есть свободные часы
async def get_free_days():
    async with async_session() as session:
        days = await session.scalars(select(Day.day_str, Day.id).distinct().
                                    join(DayTimeUser, Day.id == DayTimeUser.day).
                                    where(DayTimeUser.is_free == True).
                                    order_by(Day.id))
    return days


# Достаем свободные временные слоты 
async def get_free_hours(day:str):
    async with async_session() as session:
        hours = await session.scalars(select(Time.hour_str).distinct().
                                    join(DayTimeUser, Time.id == DayTimeUser.hour).
                                    join(Day, Day.id == DayTimeUser.day).
                                    where(DayTimeUser.is_free == True).
                                    where(Day.day_str == day).
                                    order_by(Time.hour_str)
                                    )
    return hours


# Определяем идентификаор пользователя в Телеграм по его нику
async def get_user_tg_id(tg_name:str) -> int:
    async with async_session() as session:
        user_id = await session.scalar(select(User.tg_id).where(User.tg_name == tg_name))
    return user_id


async def get_user(tg_id:int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
    return user


async def get_user_tg_name(tg_id:int) -> str:
    async with async_session() as session:
        user_name = await session.scalar(select(User.tg_name).where(User.tg_id == tg_id))
    return user_name


async def get_day_id(day:str) -> int:
    async with async_session() as session:
        day_id = await session.scalar(select(Day.id).where(Day.day_str == day))
    return day_id


async def get_hour_id(hour:str):
    async with async_session() as session:
        hour_id = await session.scalar(select(Time.id).where(Time.hour_str == hour))
    return hour_id



"""

Незарегистрированный пользователь:

"""


# Заносим запись о пользователе в БД
async def set_user(tg_id: int, name: str, program: str, course:str, tg_name:str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id,name=name,program=program,course=course,tg_name=tg_name))
            await session.commit()



"""
Зарегистрированный пользователь:

"""



# Функция оформления брони

async def new_loan(user_id: int, day_id:int, hour_id:int, need_ball:bool):
    async with async_session() as session:
        await session.execute(update(DayTimeUser).
                    values(is_free = False).
                    values(user = user_id).
                    values(need_ball = need_ball).
                    where(DayTimeUser.day == day_id).
                    where(DayTimeUser.hour == hour_id)
        )
        await session.commit()


# Функция возвращает брони пользователя
async def see_loan(user_id: int):
    async with async_session() as session:
        loans = await session.scalars(select(DayTimeUser).
                                      join(User, User.tg_id == DayTimeUser.user).
                                      where(DayTimeUser.user == user_id))
    return loans


# функция отмены своей брони пользователем
async def cancel_loan(user_id: int, day:int, hour: int):
    async with async_session() as session:
        loan = await session.scalar(select(DayTimeUser).
                                      where(DayTimeUser.day == day).
                                      where(DayTimeUser.hour == hour)
                                      )
        if loan.user == user_id:
            await session.execute(update(DayTimeUser).
                        values(is_free = True).
                        values(user = None).
                        values(need_ball = None).
                        where(DayTimeUser.day == day).
                        where(DayTimeUser.hour == hour)
                        )
            await session.commit()


#Смена данных профиля
async def change_profile_fio(user_id: int, text: str):
    async with async_session() as session:
        await session.execute(update(User).
                    values(name = text).
                    where(User.tg_id == user_id)
        )
        await session.commit()


async def change_profile_program(user_id: int, text: str):
    async with async_session() as session:
        await session.execute(update(User).
                    values(program = text).
                    where(User.tg_id == user_id)
        )
        await session.commit()


async def change_profile_course(user_id: int, text: str):
    async with async_session() as session:
        await session.execute(update(User).
                    values(course = text).
                    where(User.tg_id == user_id)
        )
        await session.commit()


async def change_profile_tg_name(user_id: int, text: str):
    async with async_session() as session:
        await session.execute(update(User).
                    values(tg_name = text).
                    where(User.tg_id == user_id)
        )
        await session.commit()



"""
Админ-панель:

"""


async def see_loans():
    async with async_session() as session:
        loans = await session.scalars(select(DayTimeUser).
                                      join(Time, Time.id == DayTimeUser.hour).
                                      join(Day, Day.id == DayTimeUser.day).
                                      join(User, User.tg_id == DayTimeUser.user).
                                      where(DayTimeUser.is_free == False))
    return loans



async def cancel_loans(day:int, hour: int):
    async with async_session() as session:
        await session.execute(update(DayTimeUser).
                    values(is_free = True).
                    values(user = None).
                    values(need_ball = None).
                    where(DayTimeUser.day == day).
                    where(DayTimeUser.hour == hour)
                    )
        await session.commit()


'''
(select(Time.hour).distinct().
                                    join(DayTimeUser, Time.id == DayTimeUser.hour).
                                    join(Day, Day.id == DayTimeUser.day).
                                    where((DayTimeUser.is_free is False)and(Day.day == day)).
                                    order_by(Time.hour)
                                    )
'''