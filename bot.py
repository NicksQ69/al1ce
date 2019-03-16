#!/usr/bin/env python       #Indication d'un fichier python.
# -*- coding: utf-8 -*-     #Lecture du fichier sous format UTF-8 (inclut les accents).

import discord, subprocess, os, sys, youtube_dl, nacl, asyncio      #Importer des modules.
from discord.ext.commands import Bot        #Importer des fonctions depuis des modules divers.
from discord.ext import commands    
from discord import Game
from discord import opus
from ctypes.util import find_library

file=open('/home/al1ce/Bot/token.txt', 'r')     #Définit la variable «file» sur le contenu du fichier «token.txt».
TOKEN = file.read().rstrip("\n")        #Module discord, lecture du «TOKEN» contenu dans la variable «file».

description = '''AL1CE_Bot in Python'''     #Description du bot.
client = commands.Bot(command_prefix='.', description=description)     #Définit le préfixe «.» pour ordonner le bot.

@client.event      #Démarrage du bot.
async def on_ready():       #Définit la fonction de démarrage «on_ready».
    print('------')     #Affiche des marges sur le terminal pour rendre lisible le contenu (esthétique).
    print('Logged in as')       #Afficher l'identification du bot (le nom).
    print(client.user.name)
    print("ID : " + client.user.id)
    print("Token : " + TOKEN)       #Afficher le token utilisé sur le terminal.
    print('------')
    await client.change_presence(game=discord.Game(name='you, master ... <3', type=2))     #Définit le statut du bot pour les utilisateurs «listening to».

#Commands

@client.command()      #Définit une commande pour le bot.
async def hello():      #Définit la fonction «hello».
    """Al1ce answers you!"""        #Description de la commande «hello».
    gitEmbed=discord.Embed(title="Who am I?", description="Hi! My name is Al1ce, and i was created to make your life easier! =D", color=0x0080ff)       #Définit le contenu de la fonction «hello».
    gitEmbed.set_author(name="AL1CE", icon_url="https://i.imgur.com/TwxY5sr.png")       #Ajout des images pour rendre plus esthétiques la commande.
    gitEmbed.set_thumbnail(url="https://i.imgur.com/TwxY5sr.png")
    await client.say(embed=gitEmbed)       #Lecture de la commande par le bot.

@client.command()      #Définit une commande pour le bot.
async def github():     #Définit la fonction «github».
    """Give github's link"""        #Descritpion de la commande «github».
    gitEmbed=discord.Embed(title="GitHub", url="https://github.com/NicksQ69/al1ce", description="GitHub by NicksQ69, co-written with Squidoss and Elmunt", color=0x0080ff)      #Définit le contenu de la fonction «github».
    gitEmbed.set_author(name="AL1CE", icon_url="https://i.imgur.com/TwxY5sr.png")       #Ajout des images pour rendre plus esthétiques la commande.
    gitEmbed.set_thumbnail(url="https://i.imgur.com/IHRXykr.png")
    await client.say(embed=gitEmbed)       #Lecture de la commande par le bot.
    #await client.say("https://github.com/NicksQ69/al1ce")

@client.command()      #Définit une commande pour le bot.
async def website():        #Définit la fonction «website».
    """Give official website's link"""      #Description de la commande «website».
    gitEmbed=discord.Embed(title="AL1CE", url="http://al1ce.fr", description="Official website of AL1CE, made by NicksQ69", color=0x0080ff)     #Définit le contenu de la fonction «website».
    gitEmbed.set_author(name="AL1CE", icon_url="https://i.imgur.com/TwxY5sr.png")       #Ajout des images pour rendre plus esthétiques la commande.
    gitEmbed.set_thumbnail(url="https://i.imgur.com/Tyohpwv.png")
    await client.say(embed=gitEmbed)       #Lecture de la commande par le bot.
    #await client.say("http://al1ce.fr")

@client.command(pass_context=True)     #Définit une commande pour le bot.
async def reboot(ctx):      #Définit la fonction «reboot».
    """Ask to reboot now"""     #Description de la commande «reboot».
    if ctx.message.author.id == '192361476844027904':       #Si l'identification correspond à l'identification donnée, ...
        await client.say("Restart in progress")        #Alors, le programme de redémarrage s'éffectue.
        await client.say("{} , my beloved master ... <3.".format(ctx.message.author.mention))
        print("Restart in progress")
        subprocess.call("./start.sh", shell=True)       #Exécute le programme "shell" : «start.sh»
        sys.exit()      #Fermeture du programme «bot.py».
    else:       #Sinon, ...
        await client.say("Unauthorized access")        #Afficher que l'accès n'est pas autorisé.
        
@client.command()      #Définit une commande pour le bot.
async def ping():   #Définit la fonction «ping».
    """Replies pong !"""        #Description de la commande «ping».
    await client.say("Pong !")      #Lecture de la commande par le bot.
    
#Commands Vocal
    
@client.command(pass_context=True)
async def join(ctx):
    """Ask to join the voice channel"""
    opus_path = find_library('opus')
    discord.opus.load_opus(opus_path)
    if not opus.is_loaded():
        print("Opus was not loaded")
    else:
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)
        print("Bot joined the voice channel")
        
@client.command(pass_context=True)
async def leave(ctx):
    """Ask to leave the voice channel"""
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
    return await client.say("I am not connected to any voice channel on this server!")
    
client.run(TOKEN)      #Exécution du bot à partir de la variable «TOKEN».
