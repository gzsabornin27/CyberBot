print("VS Code funcionando c:")

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
from datetime import datetime

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

@bot.command()
async def usuario(ctx):
    embed = discord.Embed(
        title="👤 Información del usuario",
        color=discord.Color.green()
    )

@bot.command()
async def moneda(ctx):
    resultado = random.choice(["🪙 Cara", "🪙 Cruz"])

    embed = discord.Embed(
        title="Lanzamiento de moneda",
        description=f"*Resultado:* {resultado}",
        color=discord.Color.gold()
    )

    embed.set_footer(text="CyberBot 🤖")

    await ctx.send(embed=embed)

    embed.set_thumbnail(url=ctx.author.display_avatar.url)
    embed.add_field(name="Nombre", value=ctx.author.name, inline=False)
    embed.add_field(name="Nombre en el servidor", value=ctx.author.display_name, inline=False)
    embed.add_field(name="ID", value=ctx.author.id, inline=False)
    embed.add_field(
        name="Se unió al servidor",
        value=ctx.author.joined_at.strftime("%d/%m/%Y"),
        inline=False
    )

    embed.set_footer(text="CyberBot 🤖")

    await ctx.send(embed=embed)

@bot.command()
async def ball8(ctx):
    respuestas = [
        "🟢 Sí.",
        "🔴 No.",
        "🟡 Tal vez.",
        "🤔 Es muy probable.",
        "❌ No cuentes con ello.",
        "✨ Definitivamente.",
        "⏳ Pregunta de nuevo más tarde.",
        "😅 Mejor no responder ahora."
    ]

    embed = discord.Embed(
        title="🎱 Bola Mágica 8",
        description=random.choice(respuestas),
        color=discord.Color.purple()
    )

    embed.set_footer(text=f"Pregunta de {ctx.author.display_name}")

    await ctx.send(embed=embed)

@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)

    embed = discord.Embed(
        title="🎲 Lanzamiento de dado",
        description=f"¡Salió un *{numero}*!",
        color=discord.Color.orange()
    )

    embed.set_footer(text="CyberBot 🤖")

    await ctx.send(embed=embed)

@bot.command()
async def fecha(ctx):
    ahora = datetime.now()

    embed = discord.Embed(
        title="📅 Fecha y hora",
        color=discord.Color.teal()
    )

    embed.add_field(
        name="Ahora mismo",
        value=ahora.strftime("%d/%m/%Y - %H:%M:%S"),
        inline=False
    )

    embed.set_footer(text="CyberBot 🤖")

    await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))