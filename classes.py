import json

class Monster:
    def __init__(self, name=None, hp=None, max_hp=None, dmg=None, armour=None, quote=None, img=None):
        self.name, self.hp, self.max_hp, self.dmg, self.armour = name, hp, max_hp, dmg, armour
        self.quote, self.img = quote, img

class Player:
    players_json = {}
    def __init__(self, player_id, name=None, level=1, hp=None, armour=None, weapons=None, equipped_weapon=None):
        self.player_id = player_id
        self.name, self.level, self.hp, self.armour, self.weapons = name, level, hp, armour, weapons
        try:
            self.equipped_weapon = weapons[0]
        except:
            self.equipped_weapon = '1'

    def new_player(self):
        self.hp = 100
        self.level = 1
        self.armour = 5
        self.weapons = ['1'] # wooden sword

    def to_dict(self):
        '''プレイヤーのデータを保存するために、プレイヤーをDictに変化する'''
        player_dict = {}
        player_dict['name'] = self.name
        player_dict['level'] = self.level
        player_dict['hp'] = self.hp
        player_dict['armour'] = self.armour
        player_dict['weapons'] = self.weapons
        player_dict['equipped_weapon'] = self.equipped_weapon
        return player_dict

    @staticmethod
    def save_players():
        with open('players.json', 'w') as f:
             json.dump(Player.players_json, f)

class Item:
    def __init__(self, item_id=None, name=None, dmg=None, img=None):
        self.item_id, self.name, self.dmg, self.img = item_id, name, dmg, img

    def to_dict(self):
        '''アイテムのデータを保存するために、アイテムをDictに変化する'''
        item_dict = {}
        item_dict['item_id'] = self.item_id
        item_dict['name'] = self.name
        item_dict['dmg'] = self.dmg
        item_dict['img'] = self.img
        return item_dict
