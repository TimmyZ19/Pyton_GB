# Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

print('Игра \"КРЕСТИКИ НОЛИКИ\"')

board = list(range(1, 10))
NumWin = ((1, 2, 3), (4, 5, 6), (7, 8, 9,), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))


def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    # valid = False
    while True:
        player_answer = input("Куда поставим " + player_token + "? ")
        if len(player_answer) > 1:
            print('Ошибка! Необходимо вводить только одно число!')
            continue
        if player_answer in '123456789':
            player_answer = int(player_answer)
            if str(board[player_answer - 1]) in 'XO':
                print('Ячейка занята, выберите другую!')
                continue
            else:
                board[player_answer - 1] = player_token
                break
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
            continue


def check_win(board):
    for each in NumWin:
        if board[each[0] - 1] == board[each[1] - 1] == board[each[2] - 1]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, f"выйграл {chr(127942)}!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)
