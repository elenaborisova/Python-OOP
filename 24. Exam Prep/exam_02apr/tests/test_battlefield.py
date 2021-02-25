import unittest
from exam_02apr.project.battle_field import BattleField
from exam_02apr.project.card.magic_card import MagicCard
from exam_02apr.project.player.advanced import Advanced
from exam_02apr.project.player.beginner import Beginner


class BattleFieldTests(unittest.TestCase):
    def setUp(self):
        self.battle_field = BattleField()

    def test_battleFieldFight_whenAttackerIsBeginnerAndWithoutCards_shouldIncreasePoints(self):
        attacker = Beginner('attacker test')
        enemy = Advanced('enemy test')

        self.battle_field.fight(attacker, enemy)

        self.assertEqual(50 + 40, attacker.health)
        self.assertEqual(250, enemy.health)

    def test_battleFieldFight_whenEnemyIsBeginnerAndWithoutCards_shouldIncreaseAttr(self):
        attacker = Advanced('attacker test')
        enemy = Beginner('enemy test')

        self.battle_field.fight(attacker, enemy)

        self.assertEqual(250, attacker.health)
        self.assertEqual(50 + 40, enemy.health)

    def test_battleFieldFight_whenPlayersWithCards_shouldIncreasePointsAndTakeDamage(self):
        attacker = Advanced('attacker test')
        enemy = Advanced('enemy test')
        card = MagicCard('magic card test')
        attacker.card_repository.add(card)

        self.battle_field.fight(attacker, enemy)

        self.assertEqual(250 + 80, attacker.health)
        self.assertEqual(245, enemy.health)

    def test_battleFieldFight_whenAttackerOrEnemyIsDead_shouldRaise(self):
        attacker = Beginner('attacker test')
        enemy = Advanced('enemy test')
        attacker.health = 0

        with self.assertRaises(ValueError) as context:
            self.battle_field.fight(attacker, enemy)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), 'Player is dead!')
