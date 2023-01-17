import discord
from discord.ext import commands
import dpyhr
import logging
from dotenv import load_dotenv
load_dotenv()
import os
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
log = logging.getLogger("dpyhr.test_case")
logging.basicConfig(level=logging.DEBUG)

@bot.event
async def on_ready():
    print("Ready!")
    await bot.load_extension("cogs.hello_world")

dpyhr.run(bot, "cogs", selection=dpyhr.Selection.polling)

bot.run(os.getenv("TOKEN"))