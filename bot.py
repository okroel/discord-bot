# bot.py
import os
import requests

import discord
from discord.ext import commands
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db import Wallet

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

@bot.command()
async def add_wallet(ctx, address, name, chain='ETH',
                    help="Enter a valid address as address name [chain]"):

    with Session(engine) as session:

        # Add check if address already exists

        wallet = Wallet(address=address,
                        name=name,
                        chain=chain)

        session.add(wallet)
        session.commit()

bot.run(TOKEN)
