# import discord
import random
from discord.ext import commands
from main import displayEmbed, imgEmbed

"""
All the commands that don't have any specific purpose other than to play with.
"""


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    """ Images and Gifs """

    # Sends a gif of monki flip
    @commands.command(aliases=["mf"])
    async def monki_flip(self, ctx):
        await imgEmbed(ctx, "https://media1.tenor.com/images/f9393148519c3eeb55b3a89bf650b538/tenor.gif?itemid"
                            "=18149595", "MONKI FLIP 🐵🐵🐵")

    # Sends a gif of monty mole smacking his tummy
    @commands.command(aliases=["mm"])
    async def mole(self, ctx):
        await imgEmbed(ctx, "https://i.imgur.com/gpYbeWz.gif")

    # Sends a gif of monty mole smacking his tummy
    @commands.command(aliases=["afil"])
    async def afilDance(self, ctx):
        await imgEmbed(ctx, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1192ddd2-b4a9-46dd-a462-2303ff2eb4c4/db03cn7-ee4ec2bb-df61-45b4-9596-eba0684a0f77.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMTE5MmRkZDItYjRhOS00NmRkLWE0NjItMjMwM2ZmMmViNGM0XC9kYjAzY243LWVlNGVjMmJiLWRmNjEtNDViNC05NTk2LWViYTA2ODRhMGY3Ny5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.2-u4A34II8yzpgVp9ao667cS7Vk2qKAIO7JDMg-Oq14")

    # Sends a gif of a sad buy
    @commands.command(aliases=["sad"])
    async def cry(self, ctx):
        await imgEmbed(ctx, "https://i.pinimg.com/originals/3f/c0/35/3fc035bc5d869aaffbba6c659c7a2299.gif",
                       "Sad boy times...")

    """ Text Commands """

    # Responds to a yes/no question with a random response
    # *: takes the rest of the text into the question argument
    # question: the question the user asked
    @commands.command(aliases=["8ball"])
    async def eightBall(self, ctx, *, question):
        response = ["As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now",
                    "Concentrate and ask again", "Don’t count on it", "It is certain", "It is decidedly so",
                    "Most likely", "My reply is no", "My sources say no", "Outlook good", "Outlook not so good",
                    "Reply hazy try again", "Signs point to yes", "Very doubtful", "Without a doubt", "Yes",
                    "Yes, definitely", "You may rely on it"]
        await displayEmbed(ctx, "The Magic 8 Ball", f"Question: {question}\nResponse: {random.choice(response)}")

    # Sends a random quote from Mo
    # isTts: a boolean to turn on text to speech
    @commands.command(aliases=["mq"])
    async def moQuote(self, ctx, isTts=False):
        response = ["Rape builds character", "I'm a secret Al-Qaeda agent", "Yo, I'm down for a finger in the bum",
                    "I give him the Samsung spin sloppy toppy bang me upside down [missed some stuff] cycle swirly "
                    "twirly", "9-11 is a national holiday", "I've never wanted to shoot up people as much as i want "
                                                            "now", "Imma beat that little girl up",
                    "Racism is in my blood", "Blacks don't crack",
                    "I don't understand the black panther movie. Its just black people on a screen",
                    "Is it time to fuck a horse?", "I'd rather die my own way fucking children",
                    "suck a dick. suck a dick, swallow it whole, swallow it whole, beat a bitch, beat a bitch",
                    "Cum cum cum cum cum cum cum cum cum cum cum cum cum cum cum cum. Why didn't you guys cum?",
                    "I definitely fucked your cats", "Want me to jack off to girls in front of you?",
                    "She's in my shit", "I would sit on all of your faces", "He can jerk me off at mach 2 speed",
                    "Sometimes I just want to beat your ass, with my dick"]
        await displayEmbed(ctx, "Famous Out of Context Quotes From Mo", (random.choice(response)), isTts)

    """ Random Chances """
    # Flips a number of coins (max 10) and sends the number of heads and tails made
    # flips: the number of times we are flipping a coin default to 1
    @commands.command()
    async def flip(self, ctx, flips=1):
        heads = 0
        tails = 0
        winner = ""

        # cap the number of coins to 10 max
        if flips > 10:
            flips = 10

        # repeat the flip until the specified number is reached
        for x in range(flips):
            # random number either 0 or 1
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

        await displayEmbed(ctx, "Coin Flip", winner)

    # Rolls a number of dice of some value
    # rolls: the number of times to roll the dice default to 1
    # rollType: the type of "dice" we are rolling
    @commands.command(aliases=["r"])
    async def roll(self, ctx, rolls=1, rollType=6):
        roll_total = 0
        all_rolls = ""

        # cap the number of rolls to 10
        if rolls > 10:
            rolls = 10

        # repeat the roll until the specified number is reached
        for x in range(rolls):
            # random number between 1 - the roll type
            temp = random.randrange(1, (rollType + 1))
            all_rolls += f"{str(temp)} "
            roll_total += temp
        await displayEmbed(ctx, "Rolling Dice", f"Total: {roll_total}\n{all_rolls}", False)


def setup(client):
    client.add_cog(Fun(client))
