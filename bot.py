print("VS Code funcionando c:")

import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
from datetime import datetime

load_dotenv()

WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")
print(WEATHER_API_KEY)

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

@bot.command()
async def serverinfo(ctx):
    servidor = ctx.guild

    embed = discord.Embed(
        title="🌍 Información del servidor",
        color=discord.Color.dark_blue()
    )

    embed.set_thumbnail(url=servidor.icon.url if servidor.icon else None)

    embed.add_field(name="Nombre", value=servidor.name, inline=False)
    embed.add_field(name="Dueño", value=servidor.owner, inline=False)
    embed.add_field(name="Miembros", value=servidor.member_count, inline=False)
    embed.add_field(
        name="Creado el",
        value=servidor.created_at.strftime("%d/%m/%Y"),
        inline=False
    )

    embed.set_footer(text="CyberBot 🤖")

    await ctx.send(embed=embed)

@bot.command()
async def clima(ctx, *, ciudad):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={ciudad}&appid={WEATHER_API_KEY}&units=metric&lang=es"
    )

    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        await ctx.send("❌ No pude encontrar esa ciudad.")
        return

    datos = respuesta.json()

    embed = discord.Embed(
        title=f"🌦️ Clima en {datos['name']}",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="🌡️ Temperatura",
        value=f"{datos['main']['temp']} °C",
        inline=True
    )

    embed.add_field(
        name="☁️ Estado",
        value=datos["weather"][0]["description"].capitalize(),
        inline=True
    )

    embed.add_field(
        name="💧 Humedad",
        value=f"{datos['main']['humidity']}%",
        inline=True
    )

    embed.set_footer(text="Datos: OpenWeather")

    await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))