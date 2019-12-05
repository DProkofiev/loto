import random
import files
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

players_list = []

"""
тут собственно обработчик логики игры
до начала игры нужно сконфигурировать игроков!
1. сначала показываем карточки всех игроков
2. потом по нажатию кнопки -ввод- вытаскиваем из мешка новый бочонок Barrel 
3. далее если игрок = человек обрабатываем от него ввод, а если компьютер - обрабатываем ввод автоматически
4. обновляем карточки на экране. Выпавшие на бочонке цифры из карточки стираются
5. считаем результаты и если кто-то вдруг закрыл все цифры в карточке, завершаем игру
"""

def game():
    print('играем!')
    barrel = Barrel()
    if not players_list:
        print('нужно сначала задать игроков')
    else:
        for i in range(len(players_list)):
            print('--- Игрок {} ---'.format(players_list[i].player_name))
            players_list[i].card.show()
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
                    player.card.show()
                    if (player.card.card[0].count(' ') &
                        player.card.card[1].count(' ') &
                        player.card.card[2].count(' ')) == 5:
                        print('Игра завершена. Победил Игрок', player.player_name, '\n', 3*chr(11088), 'CONGRATULATIONS!', 3*chr(11088))
                        game_exit()


"""
   класс "БОЧОНОК" с функциями мешка
   сначала мешок полный.  вызывая NEXT, выбирается случайная цифра и удаляется из мешка
"""
class Barrel:
    def __init__(self):
        self.digit = 0
        self.bag = [i for i in range(1, 91)]

    def next(self):
        self.digit = random.choice(self.bag)
        self.bag.remove(self.digit)
        self.count = len(self.bag)
        return()


"""
   класс "Карточка". Имеет три метода:
   1. New
   Новая генерируется тремя списками (по количеству строк в карточке)
   2. Update
   Пробегаем по карточке и смотрим есть ли выпавшая цифра. Если есть, меняем ее на ' ' 
   3. Show
   Показывем карточку.
   Задумка такова, что форма карточки задается в одном месте в свойстве design. 
   А данные вставляется в форму
"""
class Card:

    def __init__(self):
        self.card = []
        a = (chr(9581) + 2 * chr(9472)) + 4 * (2 * chr(9472) + chr(9516) + 2 * chr(9472)) + (2 * chr(9472) + chr(9582))
        b = (chr(9584) + 2 * chr(9472)) + 4 * (2 * chr(9472) + chr(9524) + 2 * chr(9472)) + (2 * chr(9472) + chr(9583))
        a.encode('utf-8')
        b.encode('utf-8')
        self.design = a + '\n'+'| {} | {} | {} | {} | {} |' + '\n' + b


    def new(self):
        all_set = (set(random.randint(1, 90) for i in range(91)))
        for i in range(3):
            row = sorted(set(random.sample(all_set, 5)))
            all_set.difference_update(row)
            self.card.append(row)
        return(self)

    def show(self):


# эта конструкция реализует вывод в позиции формы карточки,
# при этом добавляется пробел к цифрам, имеющим один знак (чтобы форма карточки  не разъезжалась)

        for item in self.card:
            s1 = str(item[0]) + ' ' if len(str(item[0])) == 1 else str(item[0])
            s2 = str(item[1]) + ' ' if len(str(item[1])) == 1 else str(item[1])
            s3 = str(item[2]) + ' ' if len(str(item[2])) == 1 else str(item[2])
            s4 = str(item[3]) + ' ' if len(str(item[3])) == 1 else str(item[3])
            s5 = str(item[4]) + ' ' if len(str(item[4])) == 1 else str(item[4])
            print(str(self.design).format(s1, s2, s3, s4, s5))

        return()

    def update(self, digit):
        digit_is_present = False
        for row in self.card:
            for i, val in enumerate(row):
                if val == digit:
                    row[i] = ' '
                    digit_is_present = True
        return(digit_is_present)


"""
   класс "ИГРОК" 
   имеет имя и роль (1 - компьютер, 2 - игрок)
   обработки нет - если выберут не 1 и не 2 игрок будет 1 - компьютером
"""

class Player:

    def __init__(self):
        self.player_name = 'noname'
        self.player_role = '1'
        self.card = Card().new()

    def set_player(self, player_name, player_role):
        self.player_name = player_name
        self.player_role = player_role
        return()


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