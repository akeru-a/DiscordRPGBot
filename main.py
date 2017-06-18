import discord
from discord.ext import commands

description = '''友達とパーティーを組んで、ボスを倒す'''

bot = commands.Bot(command_prefix='?', description=description)

class Monster():
    def __init__(self, img, hp):
        self.img = img
        self.hp = hp
        self.quote = quote

monster = Monster("http://68.media.tumblr.com/3d48d13edc1c3c9592721078408b6928/tumblr_nu2swkizAH1sulisxo1_1280.png",
                100,
                "わしが倒せるのかい？")

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def boss():
    test = {'title': "ボス",
    'colour': 0xFF5773,
    }

    em = discord.Embed(**test)
    em.set_image(url=monster.img)
    await bot.say('```{}```\n残り体力: {}'.format(monster.quote, monster.hp), embed=em)

bot.run('MzI1ODgwMzMxNjYyMTMxMjAx.DCerOQ.SMMLI_UXthYqCvmtfRoHmATLQgs')
