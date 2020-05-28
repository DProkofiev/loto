"""
   класс "Карточка". Имеет методы:
   1. Init
   Генерируется новая карточка тремя списками (по количеству строк в карточке)
   2. Update
   Пробегаем по карточке и смотрим есть ли выпавшая цифра. Если есть, меняем ее на ' '
   3. Str
   Показывем карточку. Пробел добавляется если в числе одна цифра
"""
import random


class Card:

    def __init__(self):
        self.card = []
        a = (chr(9581) + 2 * chr(9472)) + 4 * (2 * chr(9472) + chr(9516) + 2 * chr(9472)) + (2 * chr(9472) + chr(9582))
        b = (chr(9584) + 2 * chr(9472)) + 4 * (2 * chr(9472) + chr(9524) + 2 * chr(9472)) + (2 * chr(9472) + chr(9583))
        a.encode('utf-8')
        b.encode('utf-8')
        self.design = a + '\n'+'| {} | {} | {} | {} | {} |' + '\n' + b + '\n'
        all_set = (set(random.randint(1, 90) for i in range(91)))
        for i in range(3):
            row = sorted(set(random.sample(all_set, 5)))
            all_set.difference_update(row)
            self.card.append(row)

    def __str__(self):
        str_card = ''
        for item in self.card:
            s1 = str(item[0]) + ' ' if len(str(item[0])) == 1 else str(item[0])
            s2 = str(item[1]) + ' ' if len(str(item[1])) == 1 else str(item[1])
            s3 = str(item[2]) + ' ' if len(str(item[2])) == 1 else str(item[2])
            s4 = str(item[3]) + ' ' if len(str(item[3])) == 1 else str(item[3])
            s5 = str(item[4]) + ' ' if len(str(item[4])) == 1 else str(item[4])
            str_card += str(self.design).format(s1, s2, s3, s4, s5)
        return str_card

    def __eq__(self, other):
        for row_a in self.card:
            for row_b in other:
                if row_a == row_b:
                    return True
                else:
                    return False

    def __lt__(self, other):

        return True

    def update(self, digit):
        digit_is_present = False
        for row in self.card:
            for i, val in enumerate(row):
                if val == digit:
                    row[i] = ' '
                    digit_is_present = True
        return digit_is_present


