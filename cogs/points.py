import discord
import json
from discord.ext import commands
from main import display_embed


# Specific user permission check
def user_check(ctx):
    return ctx.author.id == 167416077322682368


class Points(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(user_check)
    async def give_points(self, ctx, member: discord.Member, points=1):
        with open("./text/points.json", 'r') as f:
            point_list = json.load(f)

        member_id = member.mention.replace('!', '')
        if member_id in point_list:
            temp = int(point_list[member_id])
            point_list[member_id] = str(temp + points)
        else:
            point_list[member_id] = str(points)

        with open("./text/points.json", 'w') as f:
            json.dump(point_list, f, indent=4)

        await display_embed(ctx, "Points Awarded", f"{points} awarded to {member.display_name}")

    @commands.command()
    @commands.check(user_check)
    async def take_points(self, ctx, member: discord.Member, points=1):
        with open("./text/points.json", 'r') as f:
            point_list = json.load(f)

        member_id = member.mention.replace('!', '')
        if member_id not in point_list:
            await display_embed(ctx, "Points Taken", f"{member.display_name} isn't on the list")
            return

        temp = int(point_list[member_id])
        if temp < points:
            point_list[member_id] = "0"
        else:
            point_list[member_id] = str(temp-points)

        with open("./text/points.json", 'w') as f:
            json.dump(point_list, f, indent=4)

        await display_embed(ctx, "Points Taken", f"{points} taken from {member.display_name}")

    @commands.command()
    async def show_points(self, ctx):
        temp = ""
        with open("./text/points.json", 'r') as f:
            lines = f.readlines()

        for i in lines:
            temp += i

        await display_embed(ctx, "Points List", temp)


def setup(client):
    client.add_cog(Points(client))
