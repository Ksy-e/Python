from loader import dp
from aiogram.types import Message
import game
import random


@dp.message_handler(commands=['help'])
async def mes_help(message: Message):
    await message.answer(f'Правила игры:\n На столе лежит 150 конфет. '
                         f'Играют два игрока делая ход друг после друга.\n'
                         f'За один ход можно забрать от 1 до 28 конфет.\n '
                         f'Кто заберёт последние выигрывает.\n'
                         f'Чтобы изменить стартовое количество конфет на столе введи /set и через пробел число.')

@dp.message_handler(commands=['set'])
async def mes_set(message: Message):
    global max_total
    count = message.text.split()[1]
    max_total = int(count)
    await message.answer(f'Установили новое количество конфет в размере - {max_total}')

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    count = message.text
    if count.isdigit() and 0 < int(count) < 29:
                duel[2] -= int(count)
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer(f'Игра уже начата. На столе {duel[2]} конфет, бери от 1 до 28.')
            break
    else:
        await message.answer(f'Привет, {message.from_user.full_name}. '
                             f'Давай поиграем в конфетки. На столе 150 конфет. Бери от 1 до 28...\n'
                             f'Если не знаешь правила, нажми /help \n'
                             f'Чтобы изменить стартовое количество конфет на столе введи /set  и через пробел число.')
        my_game = [message.from_user.id, message.from_user.first_name, max_total]
        game.total.append(my_game)



@dp.message_handler()
async def mes_help(message: Message):
    for duel in game.total:

        if message.from_user.id == duel[0]:

            count = message.text
            if count.isdigit() and 0 < int(count) < 29:
                duel[2] -= int(count)
                if await check_win(message, 'Ты', duel):
                    return True
                await message.answer(f'{duel[1]} взял {count} конфет и на столе осталось {duel[2]}\n'
                                     f'Теперь ход бота...')
                bot_take = random.randint(1, 28) if duel[2] > 28 else duel[2]
                duel[2] -= bot_take
                if await check_win(message, 'Бот', duel):
                    return True
                await message.answer(f'Бот взял {bot_take} конфет и '
                                     f'на столе осталось {duel[2]}\n'
                                     f'Теперь твой ход...')
            else:
                await message.answer(f'Введи число от 1 до 28')


async def check_win(message: Message, win: str, duel: list):
    if duel[2] <= 0:
        await message.answer(f'{win} победил! Поздравляю!')
        game.total.remove(duel)
        return True
    return False

