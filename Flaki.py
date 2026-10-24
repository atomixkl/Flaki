import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

GUILD_ID = os.getenv("DISCORD_GUILD")

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

class Flaki(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f"Запущенно як {self.user}")






bot = Flaki()
bot.run(TOKEN)