print("VS Code funcionando c:")

from dotenv import load_dotenv import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send("Hola!")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

bot.run(os.getenv("TOKEN"))