#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord, subprocess, os
from discord.ext import commands

file=open('/home/al1ce/Bot/token.txt', 'r')
TOKEN = file.read().rstrip("\n")

description = '''AL1CE_Bot in Python'''
bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print("ID : " + bot.user.id)
    print("Token : " + TOKEN)
    print('------')
    await bot.change_presence(game=discord.Game(name='you, master ... <3', type=2))

#Commands

@bot.command()
async def hello():
    """Al1ce answers you!"""
    gitEmbed=discord.Embed(title="Who am I? <3", description="Hi! My name is Al1ce, and i was created to make your life easier! =D", color=0x0080ff)
    gitEmbed.set_author(name="AL1CE", icon_url="https://i.imgur.com/TwxY5sr.png")
    gitEmbed.set_thumbnail(url="https://i.imgur.com/TwxY5sr.png")
    await bot.say(embed=gitEmbed)

@bot.command()
async def github():
    """Give github's link"""
    gitEmbed=discord.Embed(title="GitHub", url="https://github.com/NicksQ69/al1ce", description="GitHub by NicksQ69, co-written with Squidoss and Elmunt", color=0x0080ff)
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

@bot.command(pass_context=True)
async def reboot(ctx):
    """Ask to reboot now"""
    if ctx.message.author.id == '192361476844027904':
        await bot.say("Restart in progress")
        await bot.say("{} , my beloved master ... <3.".format(ctx.message.author.mention))
        print("Restart in progress")
        subprocess.call("./start.sh", shell=True)
        sys.exit()
    else:
        await bot.say("Unauthorized access")

bot.run(TOKEN)
