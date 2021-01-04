# import discord
import random
from discord.ext import commands
from main import display_embed


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["depression", "depressed", "sadened"])
    async def sad(self, ctx):
        response = ["Good", "Feels bad lmao", "kek", "Oof", "Sucks to suck", "R U HAVE DUMB?"]
        await display_embed(ctx, "You sad?", (random.choice(response)))

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx, *, question):
        response = ["As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now",
                    "Concentrate and ask again", "Don’t count on it", "It is certain", "It is decidedly so",
                    "Most likely", "My reply is no", "My sources say no", "Outlook good", "Outlook not so good",
                    "Reply hazy try again", "Signs point to yes", "Very doubtful", "Without a doubt", "Yes",
                    "Yes, definitely", "You may rely on it"]
        await display_embed(ctx, "The Magic 8 Ball", f"Question: {question}\nResponse: {random.choice(response)}")

    @commands.command()
    async def flip(self, ctx, flips=1):
        heads = 0
        tails = 0
        winner = ""

        if flips > 10:
            flips = 10

        for x in range(flips):
            flip_res = random.randint(0, 1)
            if flip_res == 0:
                heads += 1
            else:
                tails += 1

        if heads > tails:
            winner += f"Heads Wins!\nHeads: {heads}\nTails: {tails}"
        elif heads < tails:
            winner += f"Tails Wins!\nHeads: {heads}\nTails: {tails}"
        else:
            winner += f"Its a tie!\nHeads: {heads}\nTails: {tails}"

        await display_embed(ctx, "Coin Flip", winner)


def setup(client):
    client.add_cog(Fun(client))
