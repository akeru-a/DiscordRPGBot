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

    def to_object(self):
        objectified = {}
        objectified['name'] = self.name
        objectified['level'] = self.level
        objectified['hp'] = self.hp
        objectified['armour'] = self.armour
        objectified['weapons'] = self.weapons
        return objectified

class Item:
    def __init__(self, item_id=None, name=None, dmg=None, img=None):
        self.item_id, self.name, self.dmg, self.img = item_id, name, dmg, img

    def to_object(self):
        objectified = {}
        objectified['item_id'] = self.item_id
        objectified['name'] = self.name
        objectified['dmg'] = self.dmg
        objectified['img'] = self.img
        return objectified



with open('players.json', 'r') as f:
    players = json.load(f)

bossmonster = {
    'name': 'テスト・ボス',
    'hp': 100,
    'max_hp': 100,
    'dmg': 15,
    'armour': 30,
    'quote': 'わしが倒せるのかい？',
    'img': 'http://68.media.tumblr.com/3d48d13edc1c3c9592721078408b6928/tumblr_nu2swkizAH1sulisxo1_1280.png'
}
monster = Monster(**bossmonster)


firesword_blueprint = {
    'item_id': 2,
    'name': '炎の剣',
    'dmg': 30,
    'img': 'http://pixelartmaker.com/art/2635d6c2b056dfb.png'
}
firesword = Item(**firesword_blueprint)

wooden_sword_blueprint = {
    'item_id': 1,
    'name': '木剣',
    'dmg': 10,
    'img': 'http://pixelartmaker.com/art/57fe9b5aa5cb622.png'
}
wooden_sword = Item(**wooden_sword_blueprint)
with open('items.json', 'r') as f:
    items = json.load(f)

if '1' not in items:
    items['1'] = wooden_sword.to_object()
    with open('items.json', 'w') as f:
         json.dump(items, f)
if '2' not in items:
    items['2'] = firesword.to_object()
    with open('items.json', 'w') as f:
         json.dump(items, f)

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
    players[author_id] = newplayer.to_object()
    with open('players.json', 'w') as f:
         json.dump(players, f)

@bot.command(pass_context=True, aliases=['kougeki'])
async def attack(ctx):
    author_id = ctx.message.author.id
    if author_id in players:
        player = players[author_id]
        weapon = items[player['weapons'][0]]

        test = {'title': "",
        'colour': 0xEF6C00,     # 色の設定
        }
        em = discord.Embed(**test)
        em.set_image(url=weapon['img'])
        await bot.say('```武器：{}\n{}はボスを攻撃しました！ボスは{}ダメージを受けました。```'
                        .format(weapon['name'], ctx.message.author.name, weapon['dmg']), embed=em)
@bot.command(pass_context=True)
async def equipment(ctx):
    author_id = ctx.message.author.id
    if author_id in players:
        player = players[author_id]
        weapons = player['weapons']
        print(weapons)
        string = ''
        for weapon in weapons:
            string += items[weapon]['name'] + ' dmg: {}'.format(items[weapon]['dmg']) + '\n'
        await bot.say(string)


@bot.command(pass_context=True)
async def get_firesword(ctx):
    author_id = ctx.message.author.id
    if author_id in players:
        player = players[author_id]
        players[author_id]['weapons'].append('2')
        print(players[author_id]['weapons'])

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
