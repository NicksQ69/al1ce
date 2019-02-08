import discord
from discord.ext import commands

TOKEN = 'NTM2OTY3NzEyMTExNTkxNDMz.Dzykmw.J1nBswy-HqDTBu9yafoOUdAo_MU'

description = '''SquidBot in Python'''
bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")


bot.run(TOKEN)
