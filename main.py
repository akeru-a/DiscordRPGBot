import discord
from discord.ext import commands

description = '''友達とパーティーを組んで、ボスを倒す'''

bot = commands.Bot(command_prefix='!', description=description)

class Monster():
    def __init__(self, img, hp):
        self.img = img
        self.hp = hp

boss = Monster("http://68.media.tumblr.com/3d48d13edc1c3c9592721078408b6928/tumblr_nu2swkizAH1sulisxo1_1280.png", 100)

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def boss():
    em = discord.Embed(**test)
    em.set_image(url=boss.img)
    await bot.say('```わしを倒せるのかい？```\n残り体力: {}'.format(boss.hp), embed=em)

bot.run('325880331662131201')
