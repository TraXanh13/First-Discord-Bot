# import discord
from discord.ext import commands


"""
All the text based commands.
"""


class Text(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Deletes the specified number of messages in the discord channel
    # Needs to have the manage messages permission to use this command
    # Maximum of 10 messages allowed to be deleted at a time and will delete the command call
    # amount: the number of messages to be deleted
    @commands.command(aliases=["c"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        if amount > 10:
            amount = 10
        await ctx.channel.purge(limit=amount + 1)

    """Error Handling"""

    # Clear error: no number specified
    @clear.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Input total amount of messages to be cleared (max 10)")


def setup(client):
    client.add_cog(Text(client))
