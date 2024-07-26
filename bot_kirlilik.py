import discord
from discord.ext import commands
import cumleler

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def temizlik(ctx):
    await ctx.send(cumleler.atik())


bot.run("")