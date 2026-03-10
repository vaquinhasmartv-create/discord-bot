import discord
from discord.ext import commands
import asyncio
import random
import os

TOKEN = os.getenv("TOKEN")

CHANNEL_ID = 123456789012345678

gifs = [
"https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif",
"https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif",
"https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"
]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot online")

    canal = bot.get_channel(1479224288342048849)

    while True:
        await canal.send(random.choice(gifs))
        await asyncio.sleep(30)

@bot.command()
async def entrar(ctx):
    if ctx.author.voice:
        canal = ctx.author.voice.channel
        await canal.connect()
        await ctx.send("augusto mama rola.")
    else:
        await ctx.send("Entre em uma call primeiro.")

@bot.command()
async def sair(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Saí da call.")

bot.run(TOKEN)