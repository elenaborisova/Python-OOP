import unittest
from exam_02apr.project.card.card_repository import CardRepository
from exam_02apr.project.card.magic_card import MagicCard


class CardRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.card_repository = CardRepository()

    def test_cardRepositoryInit_shouldZeroCountAndEmptyCardsList(self):
        self.assertEqual(0, self.card_repository.count)
        self.assertListEqual([], self.card_repository.cards)

    def test_cardRepositoryAdd_whenCardNotInCards_shouldAddItAndIncreaseCount(self):
        card = MagicCard('test')
        self.card_repository.add(card)

        self.assertListEqual([card], self.card_repository.cards)
        self.assertEqual(1, self.card_repository.count)

    def test_cardRepositoryAdd_whenCardInCards_shouldRaise(self):
        card = MagicCard('test')
        self.card_repository.add(card)

        with self.assertRaises(ValueError) as context:
            self.card_repository.add(card)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), f'Card {card.name} already exists!')

    def test_cardRepositoryRemove_whenValidCard_shouldRemoveItAndDecreaseCount(self):
        card_name = 'test'
        card = MagicCard(card_name)
        self.card_repository.add(card)

        self.assertListEqual([card], self.card_repository.cards)
        self.assertEqual(1, self.card_repository.count)

        self.card_repository.remove(card_name)
        self.assertListEqual([], self.card_repository.cards)
        self.assertEqual(0, self.card_repository.count)

    def test_cardRepositoryRemove_whenEmptyStringCard_shouldRaise(self):
        card_name = ''

        with self.assertRaises(ValueError) as context:
            self.card_repository.remove(card_name)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), 'Card cannot be an empty string!')

    def test_cardRepositoryFind_whenGivenUsername_shouldFindAndReturnCard(self):
        username = 'test'
        card = MagicCard(username)
        self.card_repository.add(card)

        result = self.card_repository.find(username)
        self.assertEqual(card, result)
