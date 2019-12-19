from barrel import Barrel
import random


class TestBarrel:

    def test_setup(self):
        barrel = Barrel()
        assert barrel.bag[barrel.bag.index(2)] == 2
        assert barrel.count == 90
        assert barrel.digit == 0

    def test_new(self):
        barrel = Barrel()
        barrel.next()
        assert barrel.count == 89

