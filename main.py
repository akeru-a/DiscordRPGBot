import discord
from discord.ext import commands
import json
from classes import Item, Monster, Player

description = '''友達とパーティーを組んで、ボスを倒す'''

bot = commands.Bot(command_prefix='?', description=description)

players = {}
with open('players.json', 'r') as f:
    Player.players_json = json.load(f)
    for key, val in Player.players_json.items():
        players[key] = Player(key, **val)





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

items_by_name = {}
for key, val in items.items():
    items_by_name[val.name] = key

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
    Player.players_json[author_id] = newplayer.to_dict()
    players[author_id] = newplayer
    Player.save_players()

@bot.command(pass_context=True, aliases=['kougeki'])
async def attack(ctx):
    author_id = ctx.message.author.id
    if author_id in players:
        player = players[author_id]
        weapon = items[player.equipped_weapon]

        test = {'title': "",
        'colour': 0xEF6C00,     # 色の設定
        }
        em = discord.Embed(**test)
        em.set_image(url=weapon.img)
        await bot.say('```武器：{}\n{}はボスを攻撃しました！ボスは{}ダメージを受けました。```'
                        .format(weapon.name, ctx.message.author.name, weapon.dmg), embed=em)
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
        Player.save_players()
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

@bot.command()
async def test():
    weapon = items['3']
    test = {'title': "{}".format(weapon.name),
        'colour': 0xEF6C00,     # 色の設定
    }
    em = discord.Embed(**test)
    em.set_image(url=weapon.img)
    await bot.say(embed=em)

@bot.command(pass_context=True)
async def equip(ctx, item_name : str):
    author_id = ctx.message.author.id
    if author_id in players:
        player = players[author_id]
        try:
            item_id = items_by_name[item_name]
            player.equipped_weapon = item_id
            print(player.equipped_weapon)
        except:
            await bot.say("item not found")

@bot.command(pass_context=True)
async def me(ctx):
    author_id = ctx.message.author.id
    if author_id in players:
        player = players[author_id]
        response = ""
        weapon = items[player.equipped_weapon]
        response += "名前：{}\nレベル：{}\n体力：{}\n装備している武器：{}".format(ctx.message.author.name, player.level, player.hp, weapon.name)

        await bot.say("```{}```".format(response))

bot.run('MzI1ODgwMzMxNjYyMTMxMjAx.DCerOQ.SMMLI_UXthYqCvmtfRoHmATLQgs')
