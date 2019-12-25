import discord
import asyncio
import opuslib


import random
import datetime
import asyncio


from discord.ext import commands
from discord.utils import get
import youtube_dl
import ffmpeg

import random
import datetime
import asyncio

import replit

import os

from itertools import cycle


TOKEN = 'NjQzMzI4MDcyNjIzNDU2Mjc2.XgNa7Q.eO8zEl37Vz8KE22JJTrwCVdjQ04'
BOT_PREFIX = '`'


bot = commands.Bot(command_prefix=BOT_PREFIX)









@bot.event
async def on_ready():

  print ('Logging in...')
  print ('Logged in as ' + bot.user.name + '\n')

@bot.event
async def on_ready():
    replit.clear()
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    bot.remove_command('help')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("with kittens 3>"))




#playing audio in a voice channel


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
        print ('Downloading audio now!\n')
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith('.mp3'):
            name = file
            print (f"Renamed Files: {file}\n")
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print (f"{name} has finished playing!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1

    nname = name.rsplit('-', 2)
    await ctx.send(f"Playing: {nname}")
    print('Playing!\n')

#other commands

@bot.event
async def on_message_delete(message):
    await message.channel.send('There was a message deleted here, haha caught ya!')


@bot.command()
async def jt(ctx):
    await ctx.send('all hail sena!')


@bot.command()
async def Hi(ctx):
    await ctx.send('Haaaai!!! How are you doing?')


@bot.command()
async def m8b(ctx):
    await ctx.send(random.choice(["It is certain :8ball:",
                                  "It is decidedly so :8ball:",
                                  "Without a doubt :8ball:",
                                  "Yes, definitely :8ball:",
                                  "ahan, as far as i think so, no :8ball:",
                                  "Most likely :8ball:",
                                  "yeah it sounds so :8ball:",
                                  "Yes :8ball:",
                                  "Signs point to yes :8ball:",
                                  "Reply hazy try again :8ball:",
                                  "Ask again later :8ball:",
                                  "Better not tell you now :8ball:",
                                  "Cannot predict now :8ball:",
                                  "Concentrate and ask again :8ball:",
                                  "eh im not sure:8ball:",
                                  "My reply is no :8ball:",
                                  "My sources say no :8ball:",
                                  "ahan, well, dont mind if i say yes :8ball:",
                                  "Very doubtful :8ball:"]))


@bot.command()
async def maddi(ctx):
    await ctx.send('all hail kashif!')


@bot.command()
async def f(ctx):
    await ctx.send('F')


@bot.command()
async def oi(ctx):
    await ctx.send('Oye!!')


@bot.command()
async def yeet(ctx):
    await ctx.send('yeetus feetus deletus!')


@bot.command()
async def hey(ctx):
    await ctx.send('hello!')


@bot.command()
async def mahad(ctx):
    await ctx.send('the greatest washing machine')


@bot.command()
async def ashhar(ctx):
    await ctx.send('our master!')


@bot.command()
async def usama(ctx):
    await ctx.send('aapki uber aagaye hai!')


@bot.command()
async def WAHT(ctx):
    await ctx.send('silence, ashar is sleeping.. zzzz!')


@bot.command()
async def HULLOO(ctx):
    await ctx.send('HAAAAAAAAAI')


@bot.command(aliases=["repeat"])
async def echo(ctx, *, words):
    await ctx.send(words)


@bot.command()
async def testembed(ctx):
    embed = discord.Embed(title='Title', descrpition='description', colour=discord.Color.red(),
                          url="https://www.google.com")
    await ctx.send(embed=embed)


@bot.command()
async def userinfo(ctx, member: discord.Member):
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
async def coinflip(ctx):
    choices = ['heads', 'tails']
    ranchoice = random.choice(choices)
    await ctx.send(ranchoice)

#sending dm's to users
@bot.command()
async def dm(ctx):
    await ctx.author.send('Hey!')


#sending dm's pt 2
@bot.command()
async def senddm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)

bot.run(TOKEN)
