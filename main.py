import discord
from discord.ext import commands
import json

description = '''友達とパーティーを組んで、ボスを倒す'''

bot = commands.Bot(command_prefix='?', description=description)

class Monster:
    def __init__(self, name=None, hp=None, max_hp=None, dmg=None, armour=None, quote=None, img=None):
        self.name, self.hp, self.max_hp, self.dmg, self.armour = name, hp, max_hp, dmg, armour
        self.quote, self.img = quote, img

class Player:
    def __init__(self, player_id, name=None, level=1, hp=None, armour=None, weapons=None):
        self.player_id = player_id
        self.name, self.level, self.hp, self.armour, self.weapons = name, level, hp, armour, weapons

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
        return player_dict

    @staticmethod
    def save_players():
        with open('players.json', 'w') as f:
             json.dump(players_json, f)

players = {}
with open('players.json', 'r') as f:
    players_json = json.load(f)
    for key, val in players_json.items():
        players[key] = Player(key, **val)



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

monsters = {}
with open('monsters.json', 'r') as f:
    monsters_json = json.load(f)
    for key, val in monsters_json.items():
        monsters[key] = Monster(**val)
monster = monsters['1']

items = {}
with open('items.json', 'r') as f:
    items_json = json.load(f)
    for key, val in items_json.items():
        items[key] = Item(**val)

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True, aliases=['touroku'])
async def register(ctx):
    author_id = ctx.message.author.id
    newplayer = Player(author_id)
    Player.new_player(newplayer)
    players_json[author_id] = newplayer.to_dict()
    players[author_id] = newplayer
    Player.save_players()

@bot.command(pass_context=True, aliases=['kougeki'])
async def attack(ctx):
    author_id = ctx.message.author.id
    if author_id in players:
        player = players[author_id]
        weapon = items[player.weapons[0]]

        test = {'title': "",
        'colour': 0xEF6C00,     # 色の設定
        }
        em = discord.Embed(**test)
        em.set_image(url=weapon.img)
        await bot.say('```武器：{}\n{}はボスを攻撃しました！ボスは{}ダメージを受けました。```'
                        .format(weapon.name, ctx.message.author.name, weapon/dmg), embed=em)
@bot.command(pass_context=True)
async def equipment(ctx):
    author_id = ctx.message.author.id
    if author_id in players:
        player = players[author_id]
        weapons = player.weapons
        string = ''
        for weapon in weapons:
            string += items[weapon].name + ' dmg: {}'.format(items[weapon].dmg) + '\n'
        await bot.say(string)

@bot.command()
async def list_items():
    response = ""
    for key, val in items.items():
        response += val.name + ' ダメージ: {}'.format(val.dmg) + '\n'
    await bot.say("ゲームに含まれているアイテム: \n" + response)

@bot.command(pass_context=True)
async def get_firesword(ctx):
    author_id = ctx.message.author.id
    if author_id in players:
        player = players[author_id]
        players[author_id].weapons.append('2')
        print(players[author_id].weapons)
        await bot.say("_{}_を手に入れました".format(items['2'].name))

@bot.command()
async def boss():
    test = {'title': "ボス",
    'colour': 0xFF5773,     # 色の設定
    }

    em = discord.Embed(**test)
    em.set_image(url=monster.img)
    await bot.say('```{}```\n残り体力: {}/{}'.format(monster.quote, monster.hp, monster.max_hp), embed=em)

@bot.command()
async def firesword():
    monster.hp = monster.hp - fireken.dmg
    test = {'title': "{}で攻撃".format(fireken.name),
    'colour': 0xEF6C00,     # 色の設定
    }
    em = discord.Embed(**test)
    em.set_image(url=fireken.img)
    await bot.say(embed=em)
    await bot.say('```{}ダメージ与えた！\nボスの残り体力: {}/{}```'.format(fireken.dmg, monster.hp, monster.max_hp))
bot.run('MzI1ODgwMzMxNjYyMTMxMjAx.DCerOQ.SMMLI_UXthYqCvmtfRoHmATLQgs')
