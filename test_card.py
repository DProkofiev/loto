from card import Card


class TestCard:

    def test_new(self):
        card = Card()
        card.new()
        carddigits = [1, 20, 35, 49, 56]
        for i in carddigits:
            assert i in range(90)

    def test_update(self):
        card = Card()
        card.new()
        carddigit = card.card[1][4]
        assert card.update(carddigit)