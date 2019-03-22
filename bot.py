#!/usr/bin/env python       #Indication d'un fichier python.
# -*- coding: utf-8 -*-     #Lecture du fichier sous format UTF-8 (inclut les accents).

import discord, subprocess, os, sys, youtube_dl, nacl, asyncio      #Importer des modules.
from discord.ext.commands import Bot        #Importer des fonctions depuis des modules divers.
from discord.ext import commands    
from discord import Game
from discord import opus
from ctypes.util import find_library

file=open('/home/al1ce/Discord/token.txt', 'r')     #Définit la variable «file» sur le contenu du fichier «token.txt».
TOKEN = file.read().rstrip("\n")        #Module discord, lecture du «TOKEN» contenu dans la variable «file».

description = '''AL1CE_Bot in Python'''     #Description du bot.
client = commands.Bot(command_prefix='>>', description=description)     #Définit le préfixe «>>» pour ordonner le bot.
client.remove_command('help')

players = {}
owners = ['192361476844027904', '357566595029008387']

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
    if ctx.message.author.id in owners:       #Si l'identification correspond à l'identification donnée, ...
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
    
@client.command(pass_context=True)      #Définit une commande pour le bot.
async def help(ctx):        #Définit la fonction <<help>>.
    """Replies all command"""       #Description de la commande <<help>>.
    embed = discord.Embed(colour = discord.Colour.blue())       #Encadrement avec une couleur, pour rendre plus esthétique la commande.
    embed.set_author(name='Help')       #Ajout du titre de l'encadré <<'Help'>>.
    embed.add_field(name='>>hello', value='Al1ce answers you!', inline= False)      #Ajout des commandes avec leur descriptions.
    embed.add_field(name='>>github', value='Give github link', inline= False)
    embed.add_field(name='>>website', value='Give official website link', inline= False)
    embed.add_field(name='>>reboot', value='Ask to reboot now', inline= False)
    embed.add_field(name='>>ping', value='Replies pong!', inline= False)
    embed.add_field(name='>>join', value='Ask to join the voice channel', inline= False)
    embed.add_field(name='>>leave', value='Ask to leave the voice channel', inline= False)
    embed.add_field(name='>>play', value='Ask to play the music', inline= False)
    embed.add_field(name='>>pause', value='Ask to pause the music', inline= False)
    embed.add_field(name='>>stop', value='Ask to stop the music', inline= False)
    embed.add_field(name='>>resume', value='Ask to resume the music', inline= False)
    await client.say(embed=embed)       #Lecture de la commande par le bot.
    
#Commands Vocal
    
@client.command(pass_context=True)      #Définit une commande pour le bot.
async def join(ctx):        #Définit la fonction <<join>>.
    """Ask to join the voice channel"""     #Description de la commande <<join>>.
    opus_path = find_library('opus')        #Définit 'opus_path' à une librairie de commande dans le module 'opus'.
    discord.opus.load_opus(opus_path)       #Exécution du module 'opus'.
    if not opus.is_loaded():        #Si le module 'opus' n'est pas exécuté.
        print("Opus was not loaded")        #Afficher que 'Opus n'a pas été chargé'.
    else:       #Sinon, ...
        channel = ctx.message.author.voice.voice_channel        #Définit 'channel' la connexion du bot à un salon vocal.
        await client.join_voice_channel(channel)        #Lecture de la commande par le bot.
        
@client.command(pass_context=True)      #Définit une commande pour le bot.
async def leave(ctx):       #Définit la fonction <<leave>>.
    """Ask to leave the voice channel"""        #Description de la commande <<leave>>.
    for x in client.voice_clients:      #Pour 'x' dans le salon vocal : ...
        if(x.server == ctx.message.server):     #Si un utilisateur utilise la commande, ...
            return await x.disconnect()     #Alors le bot se déconnecte du salon vocal.
    return await client.say("I am not connected to any voice channel on this server!")      #Sinon, le bot annonce qu'il n'est pas connecté à un salon vocal.

@client.command(pass_context=True)      #Définit une commande pour le bot.
async def play(ctx, url):       #Définit la fonction <<play>>.
    """Ask to play the music"""     #Description de la commande <<play>>.
    server = ctx.message.server     #Définit server pour les messages adressés au bot.
    voice_client = client.voice_client_in(server)       #Définit 'voice_client' pour la connexion du bot au salon vocal.
    player = await voice_client.create_ytdl_player(url)     #Réception et exécution du module 'youtube_dl'.
    players[server.id] = player     #L'ensemble des utilisateurs ont accès à l'utilisation du module 'youtube_dl'.
    player.start()      #Exécute la musique sélectionné et téléchargé via le module 'youtube_dl'.
    
@client.command(pass_context=True)      #Définit une commande pour le bot.
async def pause(ctx):       #Définit la fonction <<pause>>.
    """Ask to pause the music"""        #Description de la commande <<pause>>.
    id = ctx.message.server.id      #Définit 'id' les identifications disponibles de ceux qui utilisent la commande.
    players[id].pause()     #Exécute la commande, et met en pause la musique.
    
@client.command(pass_context=True)      #Définit une commande pour le bot.
async def stop(ctx):        #Définit la fonction <<stop>>.
    """Ask to stop the music"""     #Description de la commande <<stop>>.
    id = ctx.message.server.id      #Définit 'id' les identifications disponibles de ceux qui utilisent la commande.
    players[id].stop()      #Exécute la commande, et arrête la lecture de la musique.
    
@client.command(pass_context=True)      #Définit une commande pour le bot.
async def resume(ctx):      #Définit la fonction <<resume>>.
    """Ask to resume the music"""       #Description de la commande <<resume>>.
    id = ctx.message.server.id      #Définit 'id' les identifications disponibles de ceux qui utilisent la commande.
    players[id].resume()        #Exécute la commande, et reprend la lecture de la musique.
    
client.run(TOKEN)      #Exécution du bot à partir de la variable «TOKEN».
