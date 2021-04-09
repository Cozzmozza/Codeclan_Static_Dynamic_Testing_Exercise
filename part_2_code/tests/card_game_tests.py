import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('hearts', 8)
        self.card2 = Card('spades', 6)
        self.card3 = Card('clubs', 1)
        self.cards = [self.card1, self.card2, self.card3]

    def test_for_no_ace(self):
        method = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(False, method)

    def test_for_ace(self):
        method = CardGame.check_for_ace(self, self.card3)
        self.assertEqual(True, method)

    def test_highest_card(self):
        method = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card1, method)

    def test_cards_total(self):
        method = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 15", method)