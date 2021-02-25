from exam_02apr.project.battle_field import BattleField
from exam_02apr.project.card.card_repository import CardRepository
from exam_02apr.project.card.magic_card import MagicCard
from exam_02apr.project.card.trap_card import TrapCard
from exam_02apr.project.player.advanced import Advanced
from exam_02apr.project.player.beginner import Beginner
from exam_02apr.project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository: PlayerRepository = PlayerRepository()
        self.card_repository: CardRepository = CardRepository()

    def add_player(self, type_p: str, username: str):
        if type_p == 'Beginner':
            self.player_repository.add(Beginner(username))
        elif type_p == 'Advanced':
            self.player_repository.add(Advanced(username))

        return f'Successfully added player of type {type_p} with username: {username}'

    def add_card(self, type_c: str, name: str):
        if type_c == 'Magic':
            self.card_repository.add(MagicCard(name))
        elif type_c == 'Trap':
            self.card_repository.add(TrapCard(name))

        return f'Successfully added card of type {type_c}Card with name: {name}'

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)

        player.card_repository.add(card)
        return f'Successfully added card: {card_name} to user: {username}'

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)

        battle_field = BattleField()
        battle_field.fight(attacker, enemy)

        return f'Attack user health {attacker.health} - Enemy user health {enemy.health}'

    def report(self):
        result = ''

        for player in self.player_repository.players:
            result += f'Username: {player.username} - Health: {player.health} - ' \
                      f'Cards {len(player.card_repository.cards)}\n'

            for card in player.card_repository.cards:
                result += f'### Card: {card.name} - Damage: {card.damage_points}\n'

        return result
