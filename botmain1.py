import replit

import discord
from discord.ext import commands

TOKEN = 'NjY4MTYxOTU0NjIzNTIwNzc5.XiNRLw.eKBYzojnK1sawoLZPfBkz5UJN7Y'

BOT_PREFIX = ''

bot = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True)


@bot.event
async def on_ready():
    print('Logged in as ZN BOT')


@bot.command()
@commands.has_any_role(618484528910041123, 513751591208091688, 530968077001687041, 572709257036955649)
async def senddm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)


@bot.event
async def on_ready():
    replit.clear()
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    bot.remove_command('help')
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("cuz i get tired too."))

#allrules
@bot.command()
async def znrules(ctx):
    embed = discord.Embed(color=0xff0000)
    embed.set_author(name="ZNotes Discord Community Rules",
                     url="https://znotes.org", icon_url = "https://znotes.org/icons/znotes-large-1.png")
    embed.set_thumbnail(url="https://znotes.org/icons/znotes-large-1.png")
    embed.add_field(name="Rule 1",
                    value="Be respectful. Please remember that everyone else here is human (though we do have a few bots, Im one too :D)",
                    inline=False)
    embed.add_field(name="Follow Discords Terms of Service AND Community guidelines: ",
                    value=" https://discordapp.com/terms, https://discordapp.com/guidelines",
                    inline=False)
    embed.add_field(name="Rule 2",
                    value="Any form of discrimination, academic dishonesty and offensive jokes involving race, religion and/or ethnicity, gender, and sexuality are prohibited.",
                    inline=False)
    embed.add_field(name="Rule 3", value="Use proper grammar and spelling.",
                    inline=False)
    embed.add_field(name="Rule 4",
                    value="Speaking in languages other than English are only allowed in language subject channels.",
                    inline=False)
    embed.add_field(name="Rule 5",
                    value="**Read the channel topics and descriptions before sending anything:** Post content in the correct channels and don’t go offtopic. IGCSE, AS, A2 and IB subjects all have their own respective channels.",
                    inline=False)
    embed.add_field(name="Rule 6",
                    value="NSFW content/discussion and excessive usage of inappropriate language are prohibited. Any moderator decisions will be made purely out of context, on a case by case basis, and as such there is no blacklist of words. If there is you have any problem with the moderator's discretion, notify a ZNotes Team Member",
                    inline=False)
    embed.add_field(name="Rule 7",
                    value="Mentioning the moderators or a specific person without proper reason is prohibited.",
                    inline=False)
    embed.add_field(name="Rule 8", value="Don't post someone's personal information without their permission.",
                    inline=False)
    embed.add_field(name="Rule 9",
                    value="Joining the server with the intent to cause harm (EX: Causing drama, being toxic to others, raiding, advertising, etc..) Will result in serious actions. We do NOT allow people to harm or harass our members here, and we do not allow people join to cause drama.",
                    inline=False)
    embed.add_field(name="Rule 10",
                    value="**No provocation:** such as instigating others to violate the rules, deliberately making members/staff angry, or being toxic.",
                    inline=False)
    embed.add_field(name="Rule 11",
                    value="**Publicly criticising, starting debates over, or commenting on a moderator’s actions:** If you have issues with any of the mods/staff members in the server please DM one of the mods directly. Criticising it in the server causes drama; breaking this rule will result in mutes/bans.",
                    inline=False)
    embed.add_field(name="Rule 12",
                    value="**No flooding, spamming or raiding:** Flooding can refer to all of these things: typing irrelevant or repeated messages, using caps, emoticons, etc. Remember that raiding is against Discord TOS. Discussion of raiding another server is punishable.",
                    inline=False)
    embed.add_field(name="Rule 13",
                    value="**No bypassing either punishments or rules:** for example, leaving and rejoining to escape a mute or saying that you were not being toxic, but rather just having some 'fun' will result in heavier punishments than originally.",
                    inline=False)
    embed.add_field(name="Rule 14",
                    value="Profile pictures used must be appropriate. Nicknames that are inappropriate or use unusual or unreadable Unicode are prohibited.",
                    inline=False)
    embed.add_field(name="Rule 15",
                    value="Sending any harmful material such as viruses, IP grabbers or malware results in an immediate and permanent ban.",
                    inline=False)
    embed.add_field(
        name="TL;DR",
        value='In conclusion, this community is designed to help YOU and your future education. It is a safe space for everyone to ask and learn together. Every user and their questions will be respected. Let\'s make the best use of the great intellect and experiences we all bring to the table!',
        inline=False)

    await ctx.send(embed=embed)





# rules
@bot.command()
async def zn1(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 1** : Be respectful. Please remember that everyone else here is human "
                                      "(though we do have a few bots, Im one too :D) ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn2(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 2 ** : Any form of discrimination, academic dishonesty and offensive jokes involving race, religion and/or ethnicity, gender, and sexuality are prohibited. ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn3(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 3** : Use proper grammar and spelling. ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn4(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 4** : Speaking in languages other than English are only allowed in language subject channels. ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn5(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 5** : Read the channel topics and descriptions before sending anything: Post content in the correct channels and don’t go offtopic. IGCSE, AS, A2 and IB subjects all have their own respective channels. ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn6(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 6** : NSFW content/discussion and excessive usage of inappropriate language are prohibited. Any moderator decisions will be made purely out of context, on a case by case basis, and as such there is no blacklist of words. If there is you have any problem with the moderator\'s discretion, notify a ZNotes Team Member. ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn7(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 7** : Mentioning the moderators or a specific person without proper reason is prohibited. ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn8(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 8** : Don\'t someone\'s personal information without their permission. ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn9(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 9** : Joining the server with the intent to cause harm (EX: Causing drama, being toxic to others, raiding, advertising, etc..) Will result in serious actions. We do NOT allow people to harm or harass our members here, and we do not allow people join to cause drama.** :  ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn10(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 10** : No provocation: such as instigating others to violate the rules, deliberately making members/staff angry, or being toxic. ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn11(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 11** : Publicly criticising, starting debates over, or commenting on a moderator’s actions: If you have issues with any of the mods/staff members in the server please DM one of the mods directly. Criticising it in the server causes drama; breaking this rule will result in mutes/bans ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn12(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 12** : No flooding, spamming or raiding: Flooding can refer to all of these things: typing irrelevant or repeated messages, using caps, emoticons, etc. Remember that raiding is against Discord TOS. Discussion of raiding another server is punishable ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn13(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 13** : No flooding, spamming or raiding: Flooding can refer to all of these things: typing irrelevant or repeated messages, using caps, emoticons, etc. Remember that raiding is against Discord TOS. Discussion of raiding another server is punishable ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn14(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 14** : Profile pictures used must be appropriate. Nicknames that are inappropriate or use unusual or unreadable Unicode are prohibited. ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


@bot.command()
async def zn15(ctx):
    embed = discord.Embed(title='ZNOTES - RULES',
                          description="**Rule # 15** : Sending any harmful material such as viruses, IP grabbers or malware results in an immediate and permanent ban. ",
                          colour=discord.Color.blue(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


# embed testing
@bot.command()
async def zntestingembed(ctx):
    embed = discord.Embed(title='ZNOTES - testing embeds',
                          description=' **Here is how to warn someone using Thanos Bot commands.** : ``Thanos Warn <User:User Mention> <Reason:Text>`` \n'
                                      '**Here is how to check the number of warnings a user has got** : ``Thanos Warnings <User:User Mention>`` \n'
                                      '**Here is how to delete a warning from a user** : ``Thanos DelWarning <Id: Whole number>`` \n'
                                      '**Here is how to clear warnings from a user** : ``Thanos ClearWarnings <User:Mention/ID>`` ',
                          colour=discord.Color.red(),
                          url="https://znotes.org")
    await ctx.send(embed=embed)


# testing embeds and guides


# guide
@bot.command()
@commands.has_any_role(618484528910041123, 513751591208091688, 530968077001687041, 572709257036955649)
async def znmodrefkick(ctx):
    embed = discord.Embed(title='ZNOTES - MOD GUIDE',
                          description="**Here is how to kick a member** : ``Kick <User:Mention/ID> [Reason:Text]`` ",
                          colour=discord.Color.red(),
                          url="https://znotes.org")

    await ctx.send(embed=embed)

@bot.command()
@commands.has_any_role(618484528910041123, 513751591208091688, 530968077001687041, 572709257036955649)
async def znmodrefclear(ctx):
    embed = discord.Embed(title='ZNOTES - MOD GUIDE',
                          description="**Here is how to clear messages* \n "
                                      "   **Clean 100 most recent messages** : ``Thanos clean 100`` \n"
                                      "**Clean 100 messages sent in the last 2 hours.** : ``Thanos clean -ma 2h 100`` \n"
                                      "**Cleans 100 messages containing pineapple** : ``Thanos clean -r pineapple 100`` \n"
                                      "**Cleans 100 messages sent by @user** : ``Cleans 100 messages sent by @user`` \n"

                                      "**Cleans 100 messages containing pineapple, and ignoring case sensitivity** : ``Thanos clean -r pineapple -i 100`` \n"
                                      "**Cleans 100 messages sent by @user in the last 5 hours containing pineapple, ignoring case sensitivity** : ``Thanos clean -ma 5h -r pineapple -i @user 100``",
                          colour=discord.Color.red(),
                          url="https://znotes.org")

    await ctx.send(embed=embed)

@bot.command()
@commands.has_any_role(618484528910041123, 513751591208091688, 530968077001687041, 572709257036955649)
async def znmodrefmute(ctx):
    embed = discord.Embed(title='ZNOTES - MOD GUIDE',
                          description="**Here's how to mute a member** : ``Thanos Mute <User:User Mention> <Reason:Text>`` \n"
                                      '**Here is how to mute a member for a set duration** : ``Thanos Mute <User:User Mention> <Duration:Duration> <Reason:Text>`` \n   **__OR__** \n``Thanos Mute <User:User Mention> <Reason:Text> <Duration:Duration>`` \n'
                                      "**Here is how to unmute a member** : ``Unmute <User:User Mention> [Reason:Text]``",
                          colour=discord.Color.red(),
                          url="https://znotes.org")

    await ctx.send(embed=embed)

@bot.command()
@commands.has_any_role(618484528910041123, 513751591208091688, 530968077001687041, 572709257036955649)
async def znmodrefwarn(ctx):
    embed = discord.Embed(title='ZNOTES - MOD GUIDE',
                          description=' **Here is how to warn someone using Thanos Bot commands.** : ``Thanos Warn <User:User Mention> <Reason:Text>`` \n'
                                      '**Here is how to check the number of warnings a user has got** : ``Thanos Warnings <User:User Mention>`` \n'
                                      '**Here is how to delete a warning from a user** : ``Thanos DelWarning <Id: Whole number>`` \n'
                                      '**Here is how to clear warnings from a user** : ``Thanos ClearWarnings <User:Mention/ID>`` ',
                          colour=discord.Color.red(),
                          url="https://znotes.org")

    await ctx.send(embed=embed)

#help
@bot.command()
@commands.has_any_role(618484528910041123, 513751591208091688, 530968077001687041, 572709257036955649)
async def znhelp(ctx):
    embed = discord.Embed(title="ZNotes Bot Commands Help", description="Below are the commands for the ZNotes Bot.",
                          color=0xff8000)
    embed.set_author(name="ZNotes Bot - Help",
                     url="https://znotes.org/icons/znotes-large-1.png", icon_url = "https://znotes.org/icons/znotes-large-1.png")
    embed.set_thumbnail(url="https://znotes.org/icons/znotes-large-1.png")
    embed.add_field(name="Basic Moderation", value="znmodrefkick / znmodrefmute / znmodrefclear / znmodrefwarn    ",
                    inline=False)
    embed.add_field(name="Rules ",
                    value="For printing individual rules, use zn(n) where n = 1 -> 15           [ie : zn1, zn15]                                                                             For printing the whole Rules list, use the command znrules",
                    inline=False)
    embed.add_field(name="Userinfo", value="use [znuserinfo @user] to print out a user's info", inline=False)
    embed.add_field(name="Sending DM's", value="[senddm @user 'message'] to send a dm to any user in the server",
                    inline=False)
    await ctx.message.author.send(embed=embed)

#clearing messages

#@bot.command()
#@commands.has_permissions(manage_messages=True)
#async def clear(ctx, amount: int):
#   await ctx.channel.purge(limit=amount +1)
#  await ctx.send(f"{amount} message/messages got deleted")

#userinfo
@bot.command()
async def znuserinfo(ctx, member: discord.Member):
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






bot.run(TOKEN)
