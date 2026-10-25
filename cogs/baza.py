import discord
from discord.ext import commands
from discord import app_commands

class bya(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Повертає пінґ бота")
    async def ping(self, interaction: discord.Interaction):

        pingms = round(self.bot.latency * 1000)

        await interaction.response.send_message(f"Понґ! *{pingms} мс*")

        

async def setup(bot):
    await bot.add_cog(bya(bot))