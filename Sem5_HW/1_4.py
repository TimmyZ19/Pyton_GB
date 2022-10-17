# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"
#

from random import shuffle

candies = int(input('Введите кол-во конфет на столе: '))
limit = 28


def bot_run(cand: int) -> int:
    if cand <= limit:  # забрать остаток
        result = cand
    else:
        result = limit
        cnt_step = cand // limit
        if cand % limit > 0:
            cnt_step += 1
        if cnt_step % 2 == 0:
            if cand - limit < limit:
                result = cand - (limit - 1)
    return result


rest_cand = candies
person_1 = input('Игрок 1 представтесь: ')
person_2 = input('Игрок 2 представтесь: ')
players = [person_1, "Бот" if int(input('Игра с ботом 1 - да, 0 - нет? ')) else person_2]
shuffle(players)

active_player = players[0]
print(f'1 игрок - {players[0]}, 2 игрок - {players[1]}')

while rest_cand > 0:
    print(f'\n На столе осталось {rest_cand} конфет, вы можете взять [1 .. {limit}]')
    print(f"Ход {active_player}'а")

    if active_player == "Бот":
        get_candies = bot_run(rest_cand)
        print(f'Бот берет {get_candies} конфет')
    else:
        get_candies = int(input(f'Сколько конфет вы хотите взять {active_player}: '))

    if get_candies not in range(1, limit + 1):
        print('Превышен лимит конфет за ход!')
    else:
        rest_cand -= get_candies
        if rest_cand > 0:
            if "Бот" in players:
                active_player = person_1 if active_player == "Бот" else "Бот"
            else:
                active_player = person_1 if active_player == person_2 else person_2
        else:
            print(f'Игрок {active_player} выйграл!')
