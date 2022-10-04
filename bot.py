# bot.py
import os
import random
import requests

import discord
from discord.ext import commands
from dotenv import load_dotenv

from sqlalchemy import create_engine

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DATABASE = os.getenv('DATABASE')

engine = create_engine(DATABASE)

intents=discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name='floor_price')
async def get_floor_price(ctx, slug):

    response =  requests.get(f"https://api.opensea.io/api/v1/collection/{slug}/stats")

    content = response.json()

    floor_price = f"{slug} - Floor price: {content['stats']['floor_price']}"

    await ctx.send(floor_price)

bot.run(TOKEN)
