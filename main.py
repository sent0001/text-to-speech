"""


Credits: developer (sent#0001) check https://pretendbot.cf for support server


"""
import discord
from discord.ext import commands
import os
import gtts
from gtts import gTTS
import ast
import inspect
import random
import asyncio
import datetime
import time
import sys
import re
from webserver import keep_alive
keep_alive()
def source(o):
    s = inspect.getsource(o).split("\n")
    indent = len(s[0]) - len(s[0].lstrip())
    return "\n".join(i[indent:] for i in s)
source_ = source(discord.gateway.DiscordWebSocket.identify)
patched = re.sub(
    r'([\'"]\$browser[\'"]:\s?[\'"]).+([\'"])',  
    r"\1Discord Android\2", 
    source_
)
loc = {}
exec(compile(ast.parse(patched), "<string>", "exec"), discord.gateway.__dict__, loc)
discord.gateway.DiscordWebSocket.identify = loc["identify"]
token = os.getenv('token')
client = commands.Bot(command_prefix=".", activity=discord.Activity(type=discord.ActivityType.watching, name="Bot made by sent#0001"), help_command=None)

@client.event
async def on_ready():
    print(client.user.name + client.user.discriminator + ' is online')
    print("sent#0001 the coolest")

@client.command()
async def tts(ctx, arg0, *, arg1):
    try:
        mytext = arg1
        language = arg0
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save('tts.mp3')
        await ctx.send(file=discord.File(r'tts.mp3'))
        os.remove('tts.mp3')
    except:
        embedVar = discord.Embed(description="<:check_warning:956780930066964500> " + ctx.message.author.mention + ": I couldn't send that!", color=0xFFFF00)
        await ctx.send(embed=embedVar)

@tts.error
async def flip_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedVar = discord.Embed(title="Missing arguments", description="`;tts [language] [message]`", color=0xFF0000)
        await ctx.send(embed=embedVar)

@client.command()
async def help(ctx):
   embed = discord.Embed(color=0x2f3136, title=client.user.name + "'s Help menu", description="Bot's prefix: **.**\n[Invite me](https://discord.com/api/oauth2/authorize?client_id=965932012143800340&permissions=52224&scope=bot)\n[Support server](https://discord.gg/pretend)")
   embed.add_field(name="tts", value="Replies with an mp3 video of your message", inline=True)
   embed.add_field(name="ping", value="Replies with bot connection in miliseconds", inline=True)
   embed.add_field(name="botinfo", value="Shows informations about the bot", inline=True)
   embed.timestamp = datetime.datetime.utcnow()
   embed.set_thumbnail(url=client.user.avatar_url)
   embed.set_author(name=ctx.message.author.name+ctx.message.author.discriminator, icon_url=ctx.message.author.avatar_url)
   embed.set_footer(text="Made by sent#0001", icon_url=client.user.avatar_url)
   await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    variable=[
        f'webhost',
        f'mommy',
        f'your address',
        f'hot asian around your area',
        f'pretendbot.cf',
        f"sent's work"
    ]
    message = await ctx.send("pinging....")
    await asyncio.sleep(1)
    await message.edit(content=f"it took `{round(client.latency * 1000)}ms` to ping " + random.choice(variable))

@client.command()
async def botinfo(ctx):
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    embed = discord.Embed(color=0x2f3136, title=client.user.name, description="A bot that converts your message into an mp3 file\nType `.help` for more informations")
    embed.add_field(name="statistics", value="guilds: " + " ** "f"{len(client.guilds)}" + "**\nusers: " + f"**{members}" + " ** \npython version: " + " **Python 3.10**\nping: " + f"**{round(client.latency * 1000)}ms**")
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_author(name=ctx.message.author.name+ctx.message.author.discriminator, icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Made by sent#0001", icon_url=client.user.avatar_url)
    await ctx.send(embed=embed)
"""


Credits: developer (sent#0001) check https://pretendbot.cf for support server


"""
client.run(token, bot=True)
