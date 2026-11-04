import discord
from discord.ext import commands
from discord import app_commands

class moderacijaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Видає бан")
    async def ban(self, interaction: discord.Interaction, користувач: discord.Member, причина: str | None = None):
        embed = discord.Embed(description=f"{користувач.mention} був забанений", color=discord.Color.from_str("#e32412"))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="tempban", description="Видає тимчасовий бан")
    async def tempban(self, interaction: discord.Interaction, користувач: discord.Member, час: str, причина: str | None = None):
        embed = discord.Embed(description=f"{користувач.mention} отримав тимчасовий бан", color=discord.Color.from_str("#e32412"))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="timeout", description="Видає таймаут")
    async def timeout(self, interaction: discord.Interaction, користувач: discord.Member, час: str, причина: str | None = None):
        embed = discord.Embed(description=f"{користувач.mention} отримав таймаут", color=discord.Color.from_str("#e67a2e"))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="kick", description="Викидає користувача зі сервера")
    async def kick(self, interaction: discord.Interaction, користувач: discord.Member, причина: str | None = None):
        embed = discord.Embed(description=f"{користувач.mention} було викинуто зі серверу", color=discord.Color.from_str("#e67a2e"))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="warn", description="Видає попередження")
    async def warn(self, interaction: discord.Interaction, користувач: discord.Member, причина: str | None = None):
        embed = discord.Embed(description=f"{користувач.mention} отримав попередження", color=discord.Color.from_str("#e67a2e"))
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(moderacijaCog(bot))