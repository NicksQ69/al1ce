import discord
from discord.ext import commands

TOKEN = 'Insert Token Here'

description = '''AL1CE_Bot in Python'''
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
    gitEmbed=discord.Embed(title="GitHub", url="https://github.com/NicksQ69/al1ce", description="GitHub by NicksQ69, co-written with Squidoss", color=0x0080ff)
    gitEmbed.set_author(name="AL1CE", icon_url="https://i.imgur.com/TwxY5sr.png")
    gitEmbed.set_thumbnail(url="https://i.imgur.com/IHRXykr.png")
    await bot.say(embed=gitEmbed)
    #await bot.say("https://github.com/NicksQ69/al1ce")

@bot.command()
async def website():
    """Give official website's link"""
    gitEmbed=discord.Embed(title="AL1CE", url="http://al1ce.fr", description="Official website of AL1CE, made by NicksQ69", color=0x0080ff)
    gitEmbed.set_author(name="AL1CE", icon_url="https://i.imgur.com/TwxY5sr.png")
    gitEmbed.set_thumbnail(url="https://i.imgur.com/Tyohpwv.png")
    await bot.say(embed=gitEmbed)
    #await bot.say("http://al1ce.fr")

bot.run(TOKEN)
