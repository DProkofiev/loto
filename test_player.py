from player import Player

class TestPlayer:

    def test_setplayer(self):

        player = Player()
        assert player.player_name == 'noname'
        assert player.player_role == '1'