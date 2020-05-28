"""
   класс "ИГРОК"
   имеет имя и роль (1 - компьютер, 2 - игрок)
   обработки нет - если выберут не 1 и не 2 игрок будет 1 - компьютером
"""
from card import Card


class Player:

    def __init__(self):
        self.player_name = 'noname'
        self.player_role = '1'
        self.card = Card()

    def __str__(self):
        return f'{self.player_name, self.player_role}'

    def __eq__(self, other):
        if self.player_name == other.player_name:
            return True

    def set_player(self, player_name, player_role):
        self.player_name = player_name
        self.player_role = player_role
