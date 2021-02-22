# import discord
import random
from discord.ext import commands
from main import display_embed, img_embed


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["depression", "depressed", "sadened"])
    async def sad(self, ctx):
        response = ["Good", "Feels bad lmao", "kek", "Oof", "Sucks to suck", "R U HAVE DUMB?"]
        await display_embed(ctx, "You sad?", (random.choice(response)))

    @commands.command(aliases=["suicide", "endMe"])
    async def kill_self(self, ctx):
        response = ["Do Monki Flip", "Jump off a bridge -Yaseen"]
        res = random.choice(response)
        if "Monki" not in res:
            await display_embed(ctx, "You want dead?", res)
        else:
            await img_embed(ctx, "https://media1.tenor.com/images/f9393148519c3eeb55b3a89bf650b538/tenor.gif?itemid="
                                 "18149595", "You want dead?", res)

    @commands.command(aliases=["mf"])
    async def monki_flip(self, ctx):
        await img_embed(ctx, "https://media1.tenor.com/images/f9393148519c3eeb55b3a89bf650b538/tenor.gif?itemid"
                             "=18149595", "MONKI FLIP 🐵🐵🐵")

    @commands.command(aliases=["mm"])
    async def mole(self, ctx):
        await img_embed(ctx, "https://i.imgur.com/gpYbeWz.gif")

    @commands.command()
    async def cry(self, ctx):
        await img_embed(ctx, "https://i.pinimg.com/originals/3f/c0/35/3fc035bc5d869aaffbba6c659c7a2299.gif",
                        "Sad boy times...")

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx, *, question):
        response = ["As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now",
                    "Concentrate and ask again", "Don’t count on it", "It is certain", "It is decidedly so",
                    "Most likely", "My reply is no", "My sources say no", "Outlook good", "Outlook not so good",
                    "Reply hazy try again", "Signs point to yes", "Very doubtful", "Without a doubt", "Yes",
                    "Yes, definitely", "You may rely on it"]
        await display_embed(ctx, "The Magic 8 Ball", f"Question: {question}\nResponse: {random.choice(response)}")

    @commands.command(aliases=["mq"])
    async def mo_quote(self, ctx, is_tts=False):
        response = ["Rape builds character", "I'm a secret Al-Qaeda agent", "Yo, I'm down for a finger in the bum",
                    "I give him the Samsung spin sloppy toppy bang me upside down [missed some stuff] cycle swirly "
                    "twirly",
                    "9-11 is a national holiday", "I've never wanted to shoot up people as much as i want now",
                    "Imma beat that little girl up", "Racism is in my blood", "Blacks don't crack",
                    "I don't understand the black panther movie. Its just black people on a screen",
                    "Is it time to fuck a horse?", "I'd rather die my own way fucking children",
                    "suck a dick. suck a dick, swallow it whole, swallow it whole, beat a bitch, beat a bitch",
                    "Cum cum cum cum cum cum cum cum cum cum cum cum cum cum cum cum. Why didn't you guys cum?",
                    "I definitely fucked your cats", "Want me to jack off to girls in front of you?",
                    "She's in my shit", "I would sit on all of your faces", "He can jerk me off at mach 2 speed",
                    "Sometimes I just want to beat your ass, with my dick"]
        await display_embed(ctx, "Famous Out of Context Quotes From Mo", (random.choice(response)), is_tts)

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

    @commands.command(aliases=["r"])
    async def roll(self, ctx, rolls=1, roll_type=6, is_tts=False):
        roll_total = 0
        all_rolls = ""

        if rolls > 10:
            rolls = 10

        for x in range(rolls):
            temp = random.randrange(1, (roll_type + 1))
            all_rolls += f"{str(temp)} "
            roll_total += temp
        await display_embed(ctx, "Rolling Dice", f"Total: {roll_total}\n{all_rolls}", is_tts)


def setup(client):
    client.add_cog(Fun(client))
