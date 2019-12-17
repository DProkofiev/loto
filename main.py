import files
from barrel import Barrel
from player import Player

# правила игры. Загружаются из файла


def show_rules():
    print(files.load_txt('loto.txt', 'r'))


# меню сделано так, что любое действие вызывается методом. В том числе и выход

def game_exit():
    exit()


"""
конфигурируем  игрока . Все игроки в игре хранятся в глобальном списке players_list
понятно что плохо, но это не баг а фича : 
так можно доблять игрока в любой момент до начала игры и предыдущий ввод не пропадает.
когда игру начнут покупать, хранить будем в файле )))))
"""


def set_players():

    num = input('Выберите количество игроков: ')
    if num.isdigit():
        while len(players_list) < int(num):
            player = Player()
            player.set_player(input('Введите имя: '),
                              input('Введите роль (1-компьютер, 2-человек): '))
            players_list.append(player)
        print('В игре участвуют игроки:')
        for i, item in enumerate(players_list):
            if item.player_role == '1':
                role = 'Компьютер'
            elif item.player_role == '2':
                role = 'Человек'
            else:
                role = 'none'
            print(' Игрок {}: имя - {}, роль - {}'.format(i+1, item.player_name, role))
    else:
        print('количество должно быть цифрой')
# а вот здесь и сама "фича"


"""
тут собственно обработчик логики игры
до начала игры нужно сконфигурировать игроков!
1. сначала показываем карточки всех игроков
2. потом по нажатию кнопки -ввод- вытаскиваем из мешка новый бочонок Barrel 
3. далее если игрок = человек обрабатываем от него ввод, а если компьютер - обрабатываем ввод автоматически
4. обновляем карточки на экране. Выпавшие на бочонке цифры из карточки стираются
5. считаем результаты и если кто-то вдруг закрыл все цифры в карточке, завершаем игру
"""
players_list = []


def game():
    print('играем!')
    barrel = Barrel()
    if not players_list:
        print('нужно сначала задать игроков')
    else:
        for i in range(len(players_list)):
            print('--- Игрок {} ---'.format(players_list[i].player_name))
            print(players_list[i].card.show())
        while True:
            enter = input('нажмите кнопку -Ввод- для следующего хода, -3- выход ')
            if enter == '3':
                game_exit()
            else:
                barrel.next()
                print('\n', 'Цифра - ', barrel.digit, 'в мешке осталось - ', barrel.count)
                for player in players_list:
                    if player.player_role == '2':
                        while True:
                            answer = input('Зачеркнуть цифру? (y/n)')
                            if answer == 'y':
                                if player.card.update(barrel.digit):
                                    break
                                else:
                                    print('вы проиграли :-(')
                                    game_exit()
                            else:
                                if answer == 'n':
                                    if player.card.update(barrel.digit):
                                        print('вы проиграли :-(')
                                        game_exit()
                                    else:
                                        break
                                else:
                                    print('повторите ввод')
                    print('--- Игрок {} ---'.format(player.player_name))
                    player.card.update(barrel.digit)
                    print(player.card.show())
                    if (player.card.card[0].count(' ') &
                        player.card.card[1].count(' ') &
                        player.card.card[2].count(' ')) == 5:
                        print('Игра завершена. Победил Игрок', player.player_name, '\n', 3*chr(11088), 'CONGRATULATIONS!', 3*chr(11088))
                        game_exit()


"""
   класс "МЕНЮ" 
   на вход словарь с цифрами, текстом для пункта, и функция которую хотим вызвать.
"""


class Menu:
    def __init__(self, links):
        self.links = links

    def show(self):
        for key, val in self.links.items():
            print('{}. {}'.format(str(key), str(val[0])))
        while True:
            link = input('Выберите пункт меню: ')
            for items in self.links.items():
                if str(link) == str(items[0]):
                    items[1][1]()
                    break
            else:
                print('повторите ввод')


if __name__ == '__main__':


# Создаем главное меню

    main_menu = Menu({1: ('правила', show_rules),
                      2: ('добавить игроков', set_players),
                      3: ('играть', game),
                      4: ('выйти', game_exit)})

# показываем главное меню
    main_menu.show()
