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
    gitEmbed=discord.Embed(title="GitHub", url="https://github.com/NicksQ69/al1ce", description="GitHub by NicksQ69, co-written with Squidoss", color=0x0080ff)
    gitEmbed.set_author(name="AL1CE",, icon_url="https://c.wallhere.com/photos/62/1e/shelter_video_Rin_Shelter_sky_space_planet-11546.jpg!d")
    gitEmbed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/1200px-Octicons-mark-github.svg.png")
    await bot.say(embed=gitEmbed)
    #await bot.say("https://github.com/NicksQ69/al1ce")


bot.run(TOKEN)
