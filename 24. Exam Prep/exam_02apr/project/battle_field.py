from exam_02apr.project.player.beginner import Beginner
from exam_02apr.project.player.player import Player


class BattleField:
    @staticmethod
    def increase_beginner_attr(player: Beginner):
        player.health += 40

        for c in player.card_repository.cards:
            c.damage_points += 30

    @staticmethod
    def get_bonus_points(player: Player):
        return sum([c.health_points for c in player.card_repository.cards])

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead!')

        if isinstance(attacker, Beginner):
            self.increase_beginner_attr(attacker)

        if isinstance(enemy, Beginner):
            self.increase_beginner_attr(enemy)

        attacker.health += self.get_bonus_points(attacker)
        enemy.health += self.get_bonus_points(enemy)

        for card in attacker.card_repository.cards:
            if enemy.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if attacker.is_dead:
                return
            attacker.take_damage(card.damage_points)
