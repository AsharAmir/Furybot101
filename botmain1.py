import discord
import asyncio


import random 
from random import randint
import datetime
import asyncio

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

bot = commands.Bot(command_prefix=BOT_PREFIX)


@bot.event
async def on_ready():
    print('Logging in...')
    print('Logged in as ' + bot.user.name + '\n')


@bot.event
async def on_ready():
    replit.clear()
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    bot.remove_command('help')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("with kittens 3> | dm Hi"))


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
async def roll(ctx):
    await ctx.send(random.choice(["1", "2", "3", "4", "5", "6"]))


@bot.command()
async def ok(ctx):
    await ctx.send('boomer')


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


# sending dm's to users
@bot.command()
async def dm(ctx):
    await ctx.author.send('Hey!')


# sending dm's pt 2
@bot.command()
async def senddm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)

#moderation

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason = "Yeeting"):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}. for [{reason}]")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = "Yeeting"):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} was banned by {ctx.author.mention}. for [{reason}]")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount +1)
    await ctx.send(f"{amount} message/messages got deleted")

@bot.command()
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == 'Muted':
            await member.add_roles(role)
            await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))
            return

        overwrite = discord.PermissionOverwrite(send_messages=False)
        newRole = await guild.create_role(name="Muted")

        for channel in guild.text_channels:
            await channel.set_permissions(newRole,overwrite=overwrite)


        await member.add_roles(newRole)
        await ctx.send("{} has {} has been muted" .format(member.mention,ctx.author.mention))


@bot.command()
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} has {} has been unmuted" .format(member.mention,ctx.author.mention))
            return

@bot.command()
async def goyt(ctx, *, search):
    query_string = urllib.parse.urlencode({"search_query": str(search)})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    await ctx.send ("Best Result from Youtube: " + "http://www.youtube.com/watch?v=" + search_results[0])
    return str("http://www.youtube.com/watch?v=" + search_results[0])




#fun - fight
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

#fun - rps
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

#fun - hack
@bot.command()
async def gohack(ctx, *, target: discord.Member = None):
    if target is None:
      target = ctx.message.author
    v = 4
    if v == 4:
      bits = getrandbits(32) # generates an integer with 32 random bits
      addr = IPv4Address(bits) # instances an IPv4Address object from those bits
      a = str(addr) # get the IPv4Address object's string representation
    elif v == 6:
      bits = getrandbits(128) # generates an integer with 128 random bits
      addr = IPv6Address(bits) # instances an IPv6Address object from those bits
      # .compressed contains the short version of the IPv6 address
      # str(addr) always returns the short address
      # .exploded is the opposite of this, always returning the full address with all-zero groups and so on
      a = addr.compressed
    async def random_with_N_digits(n):
      range_start = 10**(n-1)
      range_end = (10**n)-1
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
    await message.edit(content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address```")
    await asyncio.sleep(2)
    await message.edit(content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...```")
    await asyncio.sleep(2)
    await message.edit(content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com```")
    await message.edit(content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******```")
    await asyncio.sleep(2)
    await message.edit(content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...```")
    await asyncio.sleep(2)
    await message.edit(content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.```")
    await asyncio.sleep(2)
    await message.edit(content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...```")
    await asyncio.sleep(2)
    await message.edit(content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...\nConnection Closed.```")
    await message.edit(content=f"```css\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...\nConnection Closed.\nExited port {j}```")
    await asyncio.sleep(2)
    await ctx.send(f"Finished hacking user **{target.display_name}**.")

#weather
@bot.command()
async def weather(ctx, *, loc):
    embed=discord.Embed(discription="Weather")
    embed.set_author(name='Requested by ' + str(ctx.message.author), icon_url= ctx.message.author.avatar_url)
    embed.set_image(url="https://wttr.in/{0}.png?m".format(loc))
    embed.set_footer(text="Location: " + str(loc))
    embed.color = random.randint(0, 0xffffff)
    await ctx.send(embed=embed)




bot.run(TOKEN)
