import discord
import random
from discord.ext import commands
from discord import app_commands

class bya(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Повертає пінґ бота")
    async def ping(self, interaction: discord.Interaction):

        pingms = round(self.bot.latency * 1000)

        await interaction.response.send_message(f"Понґ! *{pingms} мс*")

    @app_commands.command(name="nyav", description="Флакі скаже няв і не тільки :3")
    async def nyav(self, interaction: discord.Interaction):

        frazy = ["Няв", "Няв :3", "Нявк", "Нявк ^^", "Няяв", "Няяв OwO", "Няяв :3", "Няяяв >:3с",
                "Ня :3", "Мур <:aww:1518327799264575590>", "Мяр (,,•᷄﹏•᷅,,)", "Мяв (˶>⩊<˶)"]
        obrfraza = random.choice(frazy)

        await interaction.response.send_message(obrfraza)
        

async def setup(bot):
    await bot.add_cog(bya(bot))