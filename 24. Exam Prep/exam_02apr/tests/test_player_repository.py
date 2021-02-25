import unittest
from exam_02apr.project.player.beginner import Beginner
from exam_02apr.project.player.player_repository import PlayerRepository


class PlayerRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.player_repository = PlayerRepository()

    def test_playerRepositoryInit_shouldZeroCountAndEmptyPlayersList(self):
        self.assertEqual(0, self.player_repository.count)
        self.assertListEqual([], self.player_repository.players)

    def test_playerRepositoryAdd_whenPlayerNotInPlayers_shouldAddItAndIncreaseCount(self):
        player = Beginner('test')
        self.player_repository.add(player)

        self.assertListEqual([player], self.player_repository.players)
        self.assertEqual(1, self.player_repository.count)

    def test_playerRepositoryAdd_whenPlayerInPlayers_shouldRaise(self):
        player = Beginner('test')
        self.player_repository.add(player)

        with self.assertRaises(ValueError) as context:
            self.player_repository.add(player)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), f'Player {player.username} already exists!')
