import discord
import json
import os
from itertools import cycle
from discord.ext import commands, tasks


def get_prefix(client, message):
    with open("./text/prefixes.json", 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
status = cycle(["you shower", "you sleep", "you fap", "you cry", "you watching me"])
client = commands.Bot(command_prefix=get_prefix, intents=intents)


# Client Events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    change_status.start()
    print('Bot is ready')


@client.event
async def on_guild_join(guild):
    with open("./text/prefixes.json", 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open("./text/prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open("./text/prefixes.json", 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("./text/prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command()
@commands.has_guild_permissions(administrator=True)
async def set_prefix(ctx, prefix):
    with open("./text/prefixes.json", 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("./text/prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)

    await display_embed(ctx, "Prefix Change", f"Prefix has been changed to {prefix}")


# Activity Enums
# playing = 0
# streaming = 1
# listening = 2
# watching = 3
# competing = 5

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=3, name=next(status)))


# Client Commands
@client.command()
@commands.has_guild_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f"{ctx.author} loaded {extension}")


@client.command()
@commands.has_guild_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    print(f"{ctx.author} unloaded {extension}")


@client.command()
@commands.has_guild_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f"{ctx.author} reloaded {extension}")


# Specific user permission check
def user_check(ctx):
    return ctx.author.id == 197757126611959808


@client.command()
@commands.check(user_check)
async def test(ctx):
    await ctx.send(f"This is a special case for {ctx.author}")


# Embed
@client.command()
async def display_embed(ctx, title, description):
    embed = discord.Embed(
        title=title,
        description=description,
        colour=discord.Colour.green()
    )

    await ctx.send(embed=embed)


# Error Handlers
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await display_embed(ctx, "Command Error!", "Command doesn't exist")


@load.error
@unload.error
@reload.error
async def load_error(ctx, error):
    await display_embed(ctx, "COG Error!", f"Error: {error}Incorrect COG selected or COG doesn't exist")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run()
