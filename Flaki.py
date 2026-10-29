import discord
import os
import asyncio
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

GUILD_ID = os.getenv("DS_GUILD")

TOKEN = os.getenv("DS_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

class Flaki(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        try:
            guild = discord.Object(id=GUILD_ID)
            self.tree.copy_global_to(guild=guild)

            syncedcmds = await self.tree.sync()
            print(f"Успішно синхронізовано команд: {len(syncedcmds)}")
        except Exception as e:
            print(f"Помилка синхронізації команд: {e}")

        print(f"Успішло запустилося як {self.user}")



    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
    
async def main():
    discord.utils.setup_logging()
    bot = Flaki()
    async with bot:
        await bot.start(TOKEN)


asyncio.run(main())