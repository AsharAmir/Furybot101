import discord
import asyncio

import random
from random import randint
import datetime
import asyncio

import urllib.request
from urllib.parse import urlparse
import re

from discord.ext import commands
from discord.utils import get
import youtube_dl
import ffmpeg

from random import getrandbits
from ipaddress import IPv4Address, IPv6Address

import random
import datetime
import asyncio

import replit

import os

from itertools import cycle

TOKEN = 'NjQzMzI4MDcyNjIzNDU2Mjc2.XguZGA.WkbmdCN33T2asrV99vf5dUh23_Y'
BOT_PREFIX = ''

bot = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True)


@bot.event
async def on_ready():
    print('Logging in...')
    print('Logged in as ' + bot.user.name + '\n')


@bot.event
async def on_ready():
    replit.clear()
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    bot.remove_command('help')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("with kittens 3> | plshelp"))

@bot.command()
async def plsinvite(ctx):
    await ctx.send('Here is the link to invite me : https://discordapp.com/api/oauth2/authorize?client_id=643328072623456276&permissions=0&scope=bot ; the help menu : plshelp')
 
@bot.command()
async def plsserver(ctx):
    await ctx.send(f"(Im in {len(bot.guilds)} servers)")

# playing audio in a voice channel


@bot.command(pass_context=True)
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot is connected to the {channel} ")

    await ctx.send(f"Joined {channel} :white_check_mark: ")


@bot.command(pass_context=True)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left{channel}")
        await ctx.send(f"Left {channel} :white_check_mark: ")
    else:
        print("")


@bot.command(pass_context=True)
async def play(ctx, url: str):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
            print('Removed old song file!')
    except PermissionError:
        print('Trying to delete song file but its being played.')
        await ctx.send('ERROR: music playing...')
        return
    await ctx.send('Getting everything ready now!')

    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading audio now!\n')
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith('.mp3'):
            name = file
            print(f"Renamed Files: {file}\n")
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print(f"{name} has finished playing!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1

    nname = name.rsplit('-', 2)
    await ctx.send(f"Playing: {nname}")
    print('Playing!\n')


# other commands

# @bot.event
# async def on_message_delete(message):
#     if message.author.bot = False:
#         await message.channel.send('There was a message deleted here, hehe, yes i got eyes on you ;)!')


# @bot.command()
# async def jt(ctx):
#     await ctx.send('all hail sena!')


@bot.command()
async def Hi(ctx):
    await ctx.send('Haaaai!!! How are you doing?')


@bot.command()
async def m8b(ctx):
    await ctx.send(random.choice(["It is certain :8ball:",
                                  "It is definetly so :8ball:",
                                  "Without a doubt :8ball:",
                                  "Yes, definitely :8ball:",
                                  "ahan, as far as i think so, no :8ball:",
                                  "Most likely :8ball:",
                                  "yeah it sounds so :8ball:",
                                  "Yes :8ball:",
                                  "Signs point to yes :8ball:",
                                  "its a 100% no:8ball:",
                                  "Ask again later :8ball:",
                                  "Better not tell you now :8ball:",
                                  "its a 100% yes :8ball:",
                                  "dont mind if i say no :8ball:",
                                  "eh im not sure:8ball:",
                                  "My reply is no :8ball:",
                                  "My sources say no :8ball:",
                                  "ahan, well, dont mind if i say yes :8ball:",
                                  "Very doubtful :8ball:"]))


@bot.command()
async def goroll(ctx):
    await ctx.send(random.choice(["1", "2", "3", "4", "5", "6"]))


@bot.command()
async def okay(ctx):
    await ctx.send('boomer')


# @bot.command()
# async def maddi(ctx):
#     await ctx.send('all hail kashif!')


@bot.command()
async def f(ctx):
    await ctx.send('F')


# @bot.command()
# async def oi(ctx):
#     await ctx.send('Oye!!')


@bot.command()
async def yeet(ctx):
    await ctx.send('yeetus feetus deletus!')


@bot.command()
async def hey(ctx):
    await ctx.send('hello!')


# @bot.command()
# async def mahad(ctx):
#     await ctx.send('the greatest washing machine')
#
#
# @bot.command()
# async def ashhar(ctx):
#     await ctx.send('our master!')
#
#
# @bot.command()
# async def usama(ctx):
#     await ctx.send('aapki uber aagaye hai!')
#
#
# @bot.command()
# async def WAHT(ctx):
#     await ctx.send('silence, ashar is sleeping.. zzzz!')
#
#
# @bot.command()
# async def HULLOO(ctx):
#     await ctx.send('HAAAAAAAAAI')


@bot.command(aliases=["repeat"])
async def plssay(ctx, *, words):
    await ctx.send(words)


# @bot.command()
# async def testembed(ctx):
#     embed = discord.Embed(title='Title', descrpition='description', colour=discord.Color.red(),
#                           url="https://www.google.com")
#     await ctx.send(embed=embed)


@bot.command()
async def plsuserinfo(ctx, member: discord.Member):
    roles = [role for role in member.roles]

    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)

    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join({role.mention for role in roles}))
    embed.add_field(name="Top Role:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)


@bot.command()
async def plscoinflip(ctx):
    choices = ['heads', 'tails']
    ranchoice = random.choice(choices)
    await ctx.send(ranchoice)


# # sending dm's to users
# @bot.command()
# async def dm(ctx):
#     await ctx.author.send('Hey!')


# sending dm's pt 2
@bot.command()
async def senddm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)


# moderation

@bot.command()
@commands.has_permissions(kick_members=True)
async def gokick(ctx, member: discord.Member, *, reason="Yeeting"):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}. for [{reason}]")


@bot.command()
@commands.has_permissions(ban_members=True)
async def goban(ctx, member: discord.Member, *, reason="Yeeting"):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} was banned by {ctx.author.mention}. for [{reason}]")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def goclear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} message/messages got deleted")


@bot.command()
async def gomute(ctx, member: discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == 'Muted':
            await member.add_roles(role)
            await ctx.send("{} has {} has been muted".format(member.mention, ctx.author.mention))
            return

        overwrite = discord.PermissionOverwrite(send_messages=False)
        newRole = await guild.create_role(name="Muted")

        for channel in guild.text_channels:
            await channel.set_permissions(newRole, overwrite=overwrite)

        await member.add_roles(newRole)
        await ctx.send("{} has {} has been muted".format(member.mention, ctx.author.mention))


@bot.command()
async def gounmute(ctx, member: discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} has {} has been unmuted".format(member.mention, ctx.author.mention))
            return


@bot.command()
async def goyt(ctx, *, search):
    query_string = urllib.parse.urlencode({"search_query": str(search)})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    await ctx.send("Best Result from Youtube: " + "http://www.youtube.com/watch?v=" + search_results[0])
    return str("http://www.youtube.com/watch?v=" + search_results[0])


# fun - fight
@bot.command()
async def gofight(ctx, challenger1="", challenger2=""):
    print("A fight is taking place...")
    if challenger1 == "":
        challenger2 = ctx.author.mention
    if challenger2 == "":
        challenger2 = ctx.author.mention
    possible_responses = [
        f'{challenger1} has won!',
        f'{challenger2} has won!'
    ]
    winner = random.choice(possible_responses)
    await ctx.send(winner)


# fun - rps
@bot.command()
async def gorps(ctx, choice):
    choice = choice.lower()
    possible_choices = [
        'rock',
        'paper',
        'scissors'
    ]
    avy = str(ctx.message.author.avatar_url)
    name = ctx.message.author.display_name
    var1 = random.choice(possible_choices)
    if choice == "rock":
        thumb = "https://pngimg.com/uploads/stone/stone_PNG13545.png"
        if var1 == "paper":
            winner = "Yay! I won!"
        elif var1 == "rock":
            winner = "It's a tie!"
        elif var1 == "scissors":
            winner = f"{name} wins!"
        else:
            winner = "woahhhhh"
    elif choice == "paper":
        thumb = "https://cdn.pixabay.com/photo/2017/10/07/21/57/pape-2828083_960_720.png"
        if var1 == "rock":
            winner = f"{name} wins!"
        elif var1 == "paper":
            winner = "It's a tie!"
        elif var1 == "scissors":
            winner = "Yay! I win!"
        else:
            winner = "woahhhhh"
    elif choice == "scissors":
        thumb = "https://pngimg.com/uploads/scissors/scissors_PNG25.png"
        if var1 == "rock":
            winner = "Yay! I won!"
        elif var1 == "paper":
            winner = f"{name} wins!"
        elif var1 == "scissors":
            winner = "It's a tie!"
    else:
        await ctx.send("You must either say rock, paper, or scissors!")
        return
    embed = discord.Embed(description="Rock Paper Scissors!")
    embed.add_field(name=f"{name}'s Choice", value=choice, inline=False)
    embed.add_field(name="My Choice", value=var1, inline=False)
    embed.add_field(name="Results:", value=winner, inline=False)
    embed.set_thumbnail(url=thumb)
    embed.set_author(name=name, icon_url=avy)
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)


# fun - hack
@bot.command()
async def gohack(ctx, *, target: discord.Member = None):
    if target is None:
        target = ctx.message.author
    v = 4
    if v == 4:
        bits = getrandbits(32)  # generates an integer with 32 random bits
        addr = IPv4Address(bits)  # instances an IPv4Address object from those bits
        a = str(addr)  # get the IPv4Address object's string representation
    elif v == 6:
        bits = getrandbits(128)  # generates an integer with 128 random bits
        addr = IPv6Address(bits)  # instances an IPv6Address object from those bits
        # .compressed contains the short version of the IPv6 address
        # str(addr) always returns the short address
        # .exploded is the opposite of this, always returning the full address with all-zero groups and so on
        a = addr.compressed

    async def random_with_N_digits(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    f = await random_with_N_digits(4)
    b = target.name.lower()
    b = b.replace(" ", "")
    j = await random_with_N_digits(5)
    if j > 65535:
        j = 65535
    message = await ctx.send("```css\nHacking...```")
    await asyncio.sleep(2)
    await message.edit(content="```css\nHacking...\nMember found!```")
    await asyncio.sleep(2)
    await message.edit(content="```css\nHacking...\nMember found!\nGetting ip...```")
    await asyncio.sleep(2)
    await message.edit(content="```css\nHacking...\nMember found!\nGetting ip...\nip found```")
    await message.edit(
        content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address```")
    await asyncio.sleep(2)
    await message.edit(
        content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...```")
    await asyncio.sleep(2)
    await message.edit(
        content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com```")
    await message.edit(
        content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******```")
    await asyncio.sleep(2)
    await message.edit(
        content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...```")
    await asyncio.sleep(2)
    await message.edit(
        content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.```")
    await asyncio.sleep(2)
    await message.edit(
        content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...```")
    await asyncio.sleep(2)
    await message.edit(
        content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...\nConnection Closed.```")
    await message.edit(
        content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...\nConnection Closed.\nExited port {j}```")
    await asyncio.sleep(2)
    await ctx.send(f"Finished hacking user **{target.display_name}**.")


# weather
@bot.command()
async def plsweather(ctx, *, loc):
    embed  = discord.Embed(discription="Weather")
    embed.set_author(name='Requested by ' + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_image(url="https://wttr.in/{0}.png?m".format(loc))
    embed.set_footer(text="Location: " + str(loc))
    embed.color = random.randint(0, 0xffffff)
    await ctx.send(embed=embed)




from translator import *


@bot.command()
async def plstranslate(ctx, src, dest, *, rawcontent):
    translator = GoogleTranslator()
    embed = discord.Embed(title='Translator', description='Translating from ' + str(src) + ' to ' + str(dest))
    embed.add_field(name='Source : ', value='```' + rawcontent + '```')
    destination = (translator.translate(rawcontent, dest=dest, src=src))
    embed.add_field(name='Translated to : ', value='```' + destination + '```')
    embed.color = random.randint(0, 0xffffff)
    await ctx.send(embed=embed)


@bot.command()
async def langhelp(ctx):
    await ctx.send('Use this link for the language codes -- > http://www.mathguide.de/info/tools/languagecode.html')

@bot.command()
async def plsremind(ctx, tim: int, work = ""):
    await ctx.send(
        ctx.author.mention + ' - Your task <' + work + '> has been set! You\'ll be reminded after ' + int(
            tim) + ' minute(s)!')
    await asyncio.sleep(tim)
    await ctx.send(ctx.author.mention + '**REMINDER** - Go commit ' + work + ' right now :point_down_tone2: ;<')

@bot.command()
async def plsbotping(ctx):
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Bot Latency:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)

import time

bot.uptime = time.time()
bot.message_count = 0
bot.messages_sent = 0
bot.mentions_count = 0


@bot.listen()
async def on_message(message):
    if message.author.bot:
        bot.messages_sent += 1
    bot.message_count += 1

    if (
            bot.user.name.lower() in message.content.lower() or
            bot.user.mentioned_in(message)
    ):
        bot.mentions_count += 1

import psutil

# bot status
@bot.command()
async def botstatus(ctx):
    uptime = time.time() - bot.uptime
    minutes, seconds = divmod(uptime, 60)
    hours, minutes = divmod(minutes, 60)

    process = psutil.Process(os.getpid())
    mem_usage = process.memory_info().rss
    mem_usage /= 1024 ** 2

    embed = discord.Embed(
        colour=discord.Colour.green(),
        title='Status - Fury the Bot'
    )
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(
        name='Bot Uptime 🕖',
        value=f'{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds',
        inline=False
    )
    embed.add_field(name='Messages Received in the server 📥', value=bot.message_count)
    embed.add_field(name='Messages Sent by any bot 📤', value=bot.messages_sent)
    embed.add_field(name='Mentions to this bot 🏷️', value=bot.mentions_count)
    embed.add_field(name='Memory Usage 💾', value=f'{mem_usage:.2f} MiB')
    embed.add_field(name='Bot version #️⃣',
                    value='This bot is running on version ' + discord.__version__ + ' of discord.py')
    embed.add_field(name='Python version 🐍', value='3.7')

    await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    print("Member named  " + member.name + " has joined")

    await member.send("**Welcome to the server boiiiii!, ** " + member.mention + "We're so happy to have you :D, have fun and make sure to spread love!")

import PyDictionary
from PyDictionary import PyDictionary


@bot.command(pass_context=True)
async def plsdefine(ctx):
    dictionary = PyDictionary()
    splitWord = (ctx.message.content.split(" ")[1])
    definedWord = dictionary.meaning(splitWord)
    embed = discord.Embed(title="Definition of " + splitWord, description="Here's what I could find.", color=0x00ffff)
    for k, v in definedWord.items():
        for e in v:
            embed.add_field(name=k, value=e, inline=False)
    await ctx.send(embed=embed)


import wikipedia

# WIKIPEDIA
@bot.command()
async def gowiki(ctx, userInput):
    try:
        await ctx.send(format(wikipedia.summary(userInput, sentences=4)))
    except wikipedia.exceptions.DisambiguationError as e:
        await ctx.send(format(("Error: {0}".format(e))))
        await ctx.send("Error: too many results, please try again with more details.")


@bot.command()
async def gopic(ctx, userInput):
    try:
        picFind = wikipedia.page(userInput)
        await ctx.send("Picture from: <{}>".format(picFind.url))
        await ctx.send(picFind.images[6])

    except wikipedia.exceptions.DisambiguationError as e:
        await ctx.send(format(("Error: {0}".format(e))))
        await ctx.send("Please try again with more details.")

@bot.command()
async def gotimer(ctx, time: int):
    newtime = int(time * 60)
    if time == 1:
        await ctx.send('Timer set for ' + str(time) + ' minute')
        await asyncio.sleep(newtime)
        await ctx.send(str(time) + ' minute has passed! ' + ctx.message.author.mention)
    if time > 1:
        await ctx.send('Timer set for ' + str(time) + ' minutes')
        await asyncio.sleep(newtime)
        await ctx.send(str(time) + ' minutes has passed! ' + ctx.message.author.mention)

@bot.command()
async def plshelp(ctx):
    embed = discord.Embed(title="Fury the Bot - Help", description="Below are the commands for Fury The Bot")
    embed.set_author(
        name="Fury The Bot",
        icon_url="https://discordapp.com/channels/@me/571013644830244864/694975138801778778")
    embed.set_thumbnail(url="https://discordapp.com/channels/@me/571013644830244864/694975138801778778")
    embed.add_field(name="Getting information for a user", value="```plsuserinfo <@user>```", inline=False)
    # embed.add_field(name="Bot's information", value="```znbotinfo```", inline=False)
    # embed.add_field(name="Send a mail to the team", value="```znmail <content>```", inline=False)
    # embed.add_field(name="Send a report to the team", value="```znreport <content>```", inline=False)
    embed.add_field(name="Fight a user xD", value="```gofight @user```", inline=False)
    embed.add_field(name="8ball", value="```m8b <question>```", inline=False)
    embed.add_field(name="Rock paper scissor", value="```gorps <rock/paper/scissor>```", inline=False)
    embed.add_field(name="Hack someone (hak0rman)", value="```gohack @user```", inline=False)
    embed.add_field(name="Fetching a youtube link", value="```goyt <keyword>```", inline=False)
    embed.add_field(name="Fetching an article summary from Wikipedia", value="```gowiki <keyword>```", inline=False)
    embed.add_field(name="Fetching a picture from Wikipedia", value="```gopic <keyword>```", inline=False)
    embed.add_field(name="Fetching Weather", value="```plsweather <location>```", inline=False)
    # embed.add_field(name="For printing individual rules",
    #                 value="```use zn(n) where n = 1 -> 15 [ie : zn1, zn15] For printing the whole Rules list, use the command znrules```",
    #                 inline=False)
    embed.add_field(name="For starting a poll",
                    value="```gopoll <question in quotations> <entries in quotations each if they're more than a single word> (max entries = 10)```",
                    inline=False)
    embed.add_field(name="For setting a timer",
                    value="```gotimer <minutes>```",
                    inline=False)
    embed.add_field(name="For sending dm's to a user",
                    value="```senddm <@user>```",
                    inline=False)
    embed.add_field(name="For flipping a coin",
                    value="```plscoinflip```",
                    inline=False)
    embed.add_field(name="For getting the bot to say something",
                    value="```plssay <content>```",
                    inline=False)
    embed.add_field(name="For kicking someone",
                    value="```gokick <@user>```",
                    inline=False)
    embed.add_field(name="For banning someone",
                    value="```plsban <@user>```",
                    inline=False)
    embed.add_field(name="For muting someone",
                    value="```plsmute <@user>```",
                    inline=False)

    embed.add_field(name="For unmuteing someone",
                    value="```plsunmute <@user>```",
                    inline=False)
    embed.add_field(name="For getting reminders",
                    value="```plsremind <content>```",
                    inline=False)
    embed.add_field(name="For searching the dictionary",
                    value="```plsdefine <word>```",
                    inline=False)
    embed.add_field(name="For translating a text",
                    value="```plstranslate <source <dest> <content>```",
                    inline=False)
        embed.add_field(name="For starting a poll",
                    value="```plspoll <question in quotations> <entries in quotations each if they're more than a single word> (max entries = 10)```",
                    inline=False)
    # embed.add_field(name="For printing the whole rule list", value="```znrules```", inline=False)
    embed.add_field(name="For getting the bot status", value="```botstatus```", inline=False)
    # embed.add_field(name="For getting the invite link and the link to the ZNotes website", value="```zninfo```",
    #                 inline=False)
    await ctx.send('A DM has been sent to you!')
    embed.set_footer(text="For queries, dm Fury™#7941 (Furry)")
    embed.color = random.randint(0, 0xffffff)
    await ctx.message.author.send(embed=embed)

    
    
@bot.command()
async def plspoll(ctx, query = '', *args):

        var1 = len(args)
        print(var1)

        embed = discord.Embed(title=query, description='React below to cast your vote!')
        embed.set_author(
            name="ZNotes Bot",
            icon_url="https://cdn.discordapp.com/attachments/670613038662942751/674287370048110602/znlogo.png")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/670613038662942751/674287370048110602/znlogo.png")

        for x, arg in enumerate(args):
                labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
                var2 = labels[x]
                x += 1
                embed.add_field(name='**' + var2 + '**', value=arg, inline=False)

        embed.color = random.randint(0, 0xffffff)
        msg = await ctx.send(embed=embed)

        for i in range (len(args)):
            reacts = ['\U0001f1e6', '\U0001f1e7', '\U0001f1e8', '\U0001f1e9',  '\U0001f1ea', '\U0001f1eb', '\U0001f1ec', '\U0001f1ed', '\U0001f1ee', '\U0001f1ef']
            reaction = reacts[i]

            i += 1
            await msg.add_reaction(reaction)




bot.run(TOKEN)
