import discord
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

bot.run("Secret Bot Code")
