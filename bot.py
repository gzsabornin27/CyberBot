print("VS Code funcionando c:")

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

@bot.command()
async def info(ctx):
    await ctx.send(
        "🤖 *CyberBot*\n"
        "Versión: 1.0\n"
        "Creado por: GZsabornin27\n"
        "Lenguaje: Python 🐍"
    )

@bot.command()
async def server(ctx):
    await ctx.send(
        f"🌍 Servidor: {ctx.guild.name}\n"
        f"👥 Miembros: {ctx.guild.member_count}"
    )

@bot.command()
async def avatar(ctx):
    embed = discord.Embed(
        title=f"Avatar de {ctx.author.display_name}",
        color=discord.Color.blue()
    )

    embed.set_image(url=ctx.author.display_avatar.url)
    embed.set_footer(text="CyberBot 🤖")

    await ctx.send(embed=embed)

@bot.command()
async def ayuda(ctx):
    await ctx.send(
        "📋 *Comandos de CyberBot*\n"
        "\n"
        "👋 !hola - Saluda.\n"
        "🏓 !ping - Comprueba si el bot responde.\n"
        "ℹ️ !info - Información del bot.\n"
        "🌍 !server - Muestra información del servidor.\n"
        "🖼️ !avatar - Muestra tu foto de perfil."
    )

bot.run(os.getenv("TOKEN"))