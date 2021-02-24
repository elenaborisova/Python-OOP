from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository: PlayerRepository = PlayerRepository()
        self.card_repository: CardRepository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == 'Beginner':
            self.player_repository.players.append(Beginner(username))
        elif type == 'Advanced':
            self.player_repository.players.append(Advanced(username))

        return f'Successfully added player of type {type} with username: {username}'

    def add_card(self, type: str, name: str):
        if type == 'Magic':
            self.card_repository.cards.append(MagicCard(name))
        elif type == 'Trap':
            self.card_repository.cards.append(TrapCard(name))

        return f'Successfully added card of type {type}Card with name: {name}'

    def add_player_card(self, username: str, card_name: str):
        player = self.find_player_by_username(username)
        card = self.find_card_by_name(card_name)

        player.card_repository.append(card)
        return f'Successfully added card: {card_name} to user: {username}'

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.find_player_by_username(attack_name)
        enemy = self.find_player_by_username(enemy_name)

        bf = BattleField()
        bf.fight(attacker, enemy)

        return f'Attack user health {attacker.health} - Enemy user health {enemy.health}'

    def find_player_by_username(self, username):
        return [p for p in self.player_repository.players if p.username == username][0]

    def find_card_by_name(self, name):
        return [c for c in self.card_repository.cards if c.name == name][0]

    def report(self):
        result = ''

        for player in self.player_repository.players:
            result += f'Username: {player.username} - Health: {player.health} - Cards {len(player.card_repository)}\n'

        for card in self.card_repository.cards:
            result += f'### Card: {card.name} - Damage: {card.damage_points}\n'

        return result[:-1]
