"""


Credits: developer (sent#0001) check https://pretendbot.cf for support server


"""
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import inspect
import asyncio
import random
import os
import gtts
from gtts import gTTS
import datetime
import re
import ast
from webserver import keep_alive
keep_alive()
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all(), activity=discord.Activity(type=discord.ActivityType.watching, name="/help for commands"), help_command=None)
slash = SlashCommand(bot, sync_commands=True)
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

@bot.event
async def on_ready():
    print(f'{bot.user} is online')

@slash.slash(name="ping", description="Shows bot connection", guild_ids=[])
async def _ping(ctx: SlashContext):
    variable=[
        f'webhost',
        f'mommy',
        f'your address',
        f'hot asian around your area',
        f'pretendbot.cf'
    ]
    message = await ctx.send("pinging....")
    await asyncio.sleep(1)
    await message.edit(content=f"it took `{round(bot.latency * 1000)}ms` to ping " + random.choice(variable))

@bot.command()
async def ping(ctx):
    variable=[
        f'webhost',
        f'mommy',
        f'your address',
        f'hot asian around your area',
        f'pretendbot.cf'
    ]
    message = await ctx.send("pinging....")
    await asyncio.sleep(1)
    await message.edit(content=f"it took `{round(bot.latency * 1000)}ms` to ping " + random.choice(variable))

@slash.slash(name="help", description="Shows bot commands", guild_ids=[])
async def _help(ctx: SlashContext):
   embed = discord.Embed(color=0x2f3136, title=bot.user.name + "'s Help menu", description="Bot works on slash commands and prefix `.`\n[Invite me](https://discord.com/api/oauth2/authorize?client_id=965932012143800340&permissions=2147601408&scope=bot%20applications.commands)\n[Support server](https://discord.gg/pretend)")
   embed.add_field(name="tts", value="Replies with an mp3 file of your message", inline=True)
   embed.add_field(name="ping", value="Replies with bot connection in miliseconds", inline=True)
   embed.add_field(name="botinfo", value="Shows informations about the bot", inline=True)
   embed.timestamp = datetime.datetime.utcnow()
   embed.set_thumbnail(url=bot.user.avatar_url)
   await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
   embed = discord.Embed(color=0x2f3136, title=bot.user.name + "'s Help menu", description="Bot works on slash commands and prefix `.`\n[Invite me](https://discord.com/api/oauth2/authorize?client_id=965932012143800340&permissions=2147601408&scope=bot%20applications.commands)\n[Support server](https://discord.gg/pretend)")
   embed.add_field(name="tts", value="Replies with an mp3 file of your message", inline=True)
   embed.add_field(name="ping", value="Replies with bot connection in miliseconds", inline=True)
   embed.add_field(name="botinfo", value="Shows informations about the bot", inline=True)
   embed.timestamp = datetime.datetime.utcnow()
   embed.set_thumbnail(url=bot.user.avatar_url)
   await ctx.send(embed=embed)

@slash.slash(name="botinfo", description="Shows bot information", guild_ids=[])
async def _botinfo(ctx: SlashContext):
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
    embed = discord.Embed(color=0x2f3136, title=bot.user.name, description="A bot that converts your message into an mp3 file\nType `.help` or `/help` for more informations")
    embed.add_field(name="statistics", value="guilds: " + " ** "f"{len(bot.guilds)}" + "**\nusers: " + f"**{members}" + " ** \nDiscord.py version: " + f" **{discord.__version__}**\nping: " + f"**{round(bot.latency * 1000)}ms**")
    embed.set_thumbnail(url=bot.user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def botinfo(ctx):
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
    embed = discord.Embed(color=0x2f3136, title=bot.user.name, description="A bot that converts your message into an mp3 file\nType `.help` or `/help` for more informations")
    embed.add_field(name="statistics", value="guilds: " + " ** "f"{len(bot.guilds)}" + "**\nusers: " + f"**{members}" + " ** \nDiscord.py version: " + f" **{discord.__version__}**\nping: " + f"**{round(bot.latency * 1000)}ms**")
    embed.set_thumbnail(url=bot.user.avatar_url)
    await ctx.send(embed=embed)

@slash.slash(
    name="tts",
    description="converts message in mp3 file",
    guild_ids=[],
    options=[
        create_option(
            name="language",
            description="Choose language",
            required=True,
            option_type=3,
            choices=[
                create_choice(
                    name="en (english)",
                    value="en"
                ),
                create_choice(
                    name="ro (romanian)",
                    value="ro"
                ),
                create_choice(
                    name="ja (japanese)",
                    value="ja"
                ),
                create_choice(
                    name="ru (russian)",
                    value="ru"
                ),
                create_choice(
                    name="de (german)",
                    value="de"
                ),
                create_choice(
                    name="fr (french)",
                    value="fr"
                ),
                create_choice(
                    name="es (spanish)",
                    value="es"
                )
            ]
        ),
        create_option(
            name="text",
            description="Type text",
            required=True,
            option_type=str
        )
    ]
)
async def _nush(ctx:SlashContext, language:str, text:str):
    mytext = text
    langu = language
    myobj = gTTS(text=mytext, lang=langu, slow=False)
    myobj.save('tts.mp3')
    await ctx.send(file=discord.File(r'tts.mp3'))
    os.remove('tts.mp3')

@bot.command()
async def tts(ctx, arg0, *, arg1):
    try:
        mytext = arg1
        language = arg0
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save('tts.mp3')
        await ctx.send(file=discord.File(r'tts.mp3'))
        os.remove('tts.mp3')
    except:
        embedVar = discord.Embed(description="<:check_warning:956780930066964500>: I couldn't send that!", color=0xFFFF00)
        await ctx.send(embed=embedVar)

@tts.error
async def flip_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedVar = discord.Embed(title="Missing arguments", description="`;tts [language] [message]`", color=0xFF0000)
        await ctx.send(embed=embedVar)
"""


Credits: developer (sent#0001) check https://pretendbot.cf for support server


"""
client.run("your bot's token", bot=True)
