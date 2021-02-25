import discord
import json
import os
from itertools import cycle
from discord.ext import commands, tasks


def get_prefix(ctx, message):
    with open("./text/prefixes.json", 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
status = cycle(["you shower", "you sleep", "you fap", "you cry", "you watching me"])
client = commands.Bot(command_prefix=get_prefix, intents=intents)


""" Client Events """


# Set bot status and prints to console when bot is ready to go
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    # change_status.start()
    print('Bot is ready')


# Adds a '.' for the bot prefix on server join
@client.event
async def on_guild_join(guild):
    with open("./text/prefixes.json", 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open("./text/prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)


# Removes the server prefix when removed from the server
@client.event
async def on_guild_remove(guild):
    with open("./text/prefixes.json", 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("./text/prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)


# Activity Enums
#    playing = 0
#    streaming = 1
#    listening = 2
#    watching = 3
#    competing = 5
#
# Changes the status of what the bot is doing cycling through the status variable above
@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=3, name=next(status)))


""" Client Commands """


# Changes the prefix for the bot
@client.command()
@commands.has_guild_permissions(administrator=True)
async def setPrefix(ctx, prefix):
    with open("./text/prefixes.json", 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("./text/prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)

    await displayEmbed(ctx, "Prefix Change", f"Prefix has been changed to {prefix}")


# Loads (turns on) the cog passed
# The user needs administrator permissions to run this command
# extension: the name of the cog to load
@client.command()
@commands.has_guild_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f"{ctx.author} loaded {extension}")


# Unloads (turns off) the cog passed
# The user needs administrator permissions to run this command
# extension: the name of the cog to unload
@client.command()
@commands.has_guild_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    print(f"{ctx.author} unloaded {extension}")


# "Reloads" all the cogs by unloading them and loading them back in
# The user needs administrator permissions to run this command
# extension: the name of the cog to reload
@client.command()
@commands.has_guild_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f"{ctx.author} reloaded {extension}")


""" Embed Messages """


# Creates an embedded message with the arguments passed. Text to speech can also be enabled
# title: the title (bold text at the top) of the embedded message
# description: the content of the embedded message
# isTts: a boolean to turn text to speech on (True = on; False = off)
@client.command()
async def displayEmbed(ctx, title, description, isTts=False):
    embed = discord.Embed(
        title=title,
        description=description,
        colour=discord.Colour.green()
    )
    if isTts:
        tts = title + " " + description
        await ctx.send(tts, embed=embed, tts=isTts)
    else:
        await ctx.send(embed=embed, tts=isTts)


# Creates an embedded message with an image or gif attached
# img: the link to the image or gif
# title: the title (bold text at the top) of the embedded message
# description: the content of the embedded message
@client.command()
async def imgEmbed(ctx, img="", title="", description=""):
    embed = discord.Embed(
        title=title,
        description=description
    )
    embed.set_image(url=img)
    await ctx.send(embed=embed)


# Error Handlers
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await displayEmbed(ctx, "Command Error!", "Command doesn't exist")


@load.error
@unload.error
@reload.error
async def load_error(ctx, error):
    await displayEmbed(ctx, "COG Error!", f"Error: {error}Incorrect COG selected or COG doesn't exist")


# loops through each file in the cogs directory
for filename in os.listdir("./cogs"):
    # searches for python files
    if filename.endswith(".py"):
        # loads the files using the load()
        client.load_extension(f"cogs.{filename[:-3]}")

client.run()
