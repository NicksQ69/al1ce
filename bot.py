import discord
from discord.ext import commands

TOKEN = 'Insert Token Here'

description = '''Al1ce bot in Python'''
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
    
@bot.command()
async def github():
    """Give github's link"""
    await bot.say("https://github.com/NicksQ69/al1ce")


bot.run(TOKEN)
