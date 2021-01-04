# import discord
from discord.ext import commands


class Text(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        if amount > 20:
            amount = 20
        await ctx.channel.purge(limit=amount + 1)

    # Error Handling
    @clear.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Input total amount of lines to be cleared (max 20)")


def setup(client):
    client.add_cog(Text(client))
