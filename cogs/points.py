import discord
import json
from discord.ext import commands
from main import displayEmbed


# Specific user permission check
# def userCheck(ctx):
#    return ctx.author.id == 645987661051592735


# Checks for a specific role
def roleCheck(ctx):
    hasPerm = False
    role = discord.utils.get(ctx.guild.roles, name="Al-Mujadila")
    if role in ctx.author.roles:
        hasPerm = True

    return hasPerm


# Method to replace multiple chars in a string
# text: the string that we are looking through
# charsToReplace: the characters you are looking for
# replacement: the characters you will replace it with
def replaceMultiple(text, charsToReplace, replacement):
    for c in charsToReplace:
        if c in text:
            text = text.replace(c, replacement)

    return text


"""
All the stuff to keep track of points for the club server
"""


class Points(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Gives point(s) to a specified user
    # Needs to be specific user(s) to use command
    # member: the member that is getting point(s)
    # points: the number of points given to the member. Default set to 1 point
    @commands.command()
    @commands.check(roleCheck)
    async def givePoints(self, ctx, member: discord.Member, points=1):
        # open and reads the json file with all the points
        with open("./text/points.json", 'r') as f:
            point_list = json.load(f)

        # replaces the '!' in the user ID
        member_id = member.mention.replace('!', '')
        # if the mentioned member is already in the file
        if member_id in point_list:
            temp = int(point_list[member_id])
            point_list[member_id] = str(temp + points)
        else:
            point_list[member_id] = str(points)

        # open and write into the json file
        with open("./text/points.json", 'w') as f:
            json.dump(point_list, f, indent=4)

        await displayEmbed(ctx, "Points Awarded", f"{points} awarded to {member.display_name}")

    # Takes point(s) to a specified user
    # Needs to be specific user(s) to use command
    # member: the member that is losing point(s)
    # points: the number of points taken from the member. Default set to 1 point
    @commands.command()
    @commands.check(roleCheck)
    async def takePoints(self, ctx, member: discord.Member, points=1):
        # open and reads the json file with all the points
        with open("./text/points.json", 'r') as f:
            point_list = json.load(f)

        # replaces the '!' in the user ID
        member_id = member.mention.replace('!', '')
        # if the mentioned member is not in the file
        if member_id not in point_list:
            await displayEmbed(ctx, "Points Taken", f"{member.display_name} isn't on the list")
            return

        temp = int(point_list[member_id])
        if temp < points:
            point_list[member_id] = "0"
        else:
            point_list[member_id] = str(temp - points)

        # open and write into the json file
        with open("./text/points.json", 'w') as f:
            json.dump(point_list, f, indent=4)

        await displayEmbed(ctx, "Points Taken", f"{points} taken from {member.display_name}")

    # Display all the users and their points in the file
    @commands.command()
    async def showPoints(self, ctx):
        temp = ""
        # open and reads the json file with all the points
        with open("./text/points.json", 'r') as f:
            lines = f.readlines()

        # Loops through each line of the file
        for i in lines:
            # Removes any of the specified characters
            temp += replaceMultiple(i, ['{', '"', ',', '}'], '')

        await displayEmbed(ctx, "Points List", temp)


def setup(client):
    client.add_cog(Points(client))
