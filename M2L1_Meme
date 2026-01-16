import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot. My name is {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Goodbye!')

@bot.command()
async def emoji(ctx):
    await ctx.send(f'\U0001F600')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

print(os.listdir('images'))

@bot.command()
async def animal(ctx):
    images = os.listdir('images/animal_memes')
    image_name = random.choice(images)
    with open(f'images/animal_memes/{image_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def popculture(ctx):
    images = os.listdir('images/pop_culture_memes')
    image_name = random.choice(images)
    with open(f'images/pop_culture_memes/{image_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("Secret Bot Token")
