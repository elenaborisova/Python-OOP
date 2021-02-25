import unittest
from exam_02apr.project.card.magic_card import MagicCard
from exam_02apr.project.controller import Controller
from exam_02apr.project.player.beginner import Beginner


class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_controllerInit_shouldInitializeRepositoriesAsAttributes(self):
        self.assertEqual('CardRepository', self.controller.card_repository.__class__.__name__)
        self.assertEqual('PlayerRepository', self.controller.player_repository.__class__.__name__)

    def test_controllerAddPlayer_shouldAddPlayerToRepository(self):
        type_p_1 = 'Beginner'
        username_1 = 'test username'
        type_p_2 = 'Advanced'
        username_2 = 'test username 2'
        result_1 = self.controller.add_player(type_p_1, username_1)
        result_2 = self.controller.add_player(type_p_2, username_2)

        self.assertEqual('test username', self.controller.player_repository.players[0].username)
        self.assertEqual('Beginner', self.controller.player_repository.players[0].__class__.__name__)
        self.assertEqual('Successfully added player of type Beginner with username: test username', result_1)
        self.assertEqual('test username 2', self.controller.player_repository.players[1].username)
        self.assertEqual('Advanced', self.controller.player_repository.players[1].__class__.__name__)
        self.assertEqual('Successfully added player of type Advanced with username: test username 2', result_2)

    def test_controllerAddCard_shouldAddCardToRepository(self):
        type_c_1 = 'Magic'
        name_1 = 'test name'
        type_c_2 = 'Trap'
        name_2 = 'test name 2'
        result_1 = self.controller.add_card(type_c_1, name_1)
        result_2 = self.controller.add_card(type_c_2, name_2)

        self.assertEqual('test name', self.controller.card_repository.cards[0].name)
        self.assertEqual('MagicCard', self.controller.card_repository.cards[0].__class__.__name__)
        self.assertEqual('Successfully added card of type MagicCard with name: test name', result_1)
        self.assertEqual('test name 2', self.controller.card_repository.cards[1].name)
        self.assertEqual('TrapCard', self.controller.card_repository.cards[1].__class__.__name__)
        self.assertEqual('Successfully added card of type TrapCard with name: test name 2', result_2)

    def test_controllerAddPlayerCard_shouldAddCardToPlayersCardRepository(self):
        username = 'test username'
        card_name = 'test card name'
        player = Beginner(username)
        card = MagicCard(card_name)
        self.controller.player_repository.add(player)
        self.controller.card_repository.add(card)

        result = self.controller.add_player_card(username, card_name)

        self.assertListEqual([card], player.card_repository.cards)
        self.assertEqual('Successfully added card: test card name to user: test username', result)

    def test_controllerFight_shouldPlayersFightInBattleField(self):
        attack_name = 'test attack name'
        enemy_name = 'test enemy name'
        self.controller.add_player('Advanced', attack_name)
        self.controller.add_player('Advanced', enemy_name)

        result = self.controller.fight(attack_name, enemy_name)

        self.assertEqual('Attack user health 250 - Enemy user health 250', result)

    def test_controllerReport_shouldReturnStringInformation(self):
        self.controller.add_player('Beginner', 'test beginner')
        self.controller.add_player('Advanced', 'test advanced')
        self.controller.add_card('Magic', 'test magic')
        self.controller.add_card('Trap', 'test trap')
        self.controller.add_player_card('test beginner', 'test magic')
        self.controller.add_player_card('test beginner', 'test trap')

        expected = f'Username: test beginner - Health: 50 - Cards 2\n' \
                   f'### Card: test magic - Damage: 5\n' \
                   f'### Card: test trap - Damage: 120\n' \
                   f'Username: test advanced - Health: 250 - Cards 0\n'
        actual = self.controller.report()

        self.assertEqual(actual, expected)
