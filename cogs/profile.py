import discord
from discord.ext import commands

"""
All the stuff that have to do with other profiles on the discord channel. 
Thus far they include kick, ban, and unban.
"""


class Profile(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Kicks the member from the server
    # Needs to have permission to kick members
    # member: the discord member that is being kicked
    # *: Takes all the following text
    # reason: the reason for the kick
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}")

    # Kicks the member from the server
    # Needs to have permission to ban members
    # member: the discord member that is being banned
    # *: Takes all the following text
    # reason: the reason for the ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}")

    # Unbans a member from the server
    # Needs to have permission to ban members
    # member: the discord member that is being unbanned
    # *: Takes all the following text
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        # Loops through all the banned members
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')


def setup(client):
    client.add_cog(Profile(client))
