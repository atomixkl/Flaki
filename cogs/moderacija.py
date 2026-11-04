import discord
from discord.ext import commands
from discord import app_commands

class moderacija(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Видає бан")
    @app_commands.guild_only()
    @app_commands.default_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, користувач: discord.User, причина: str | None = None):

        if not interaction.user.guild_permissions.ban_members:
            return await interaction.response.send_message("Ви не маєте прав, щоб банити цю людину", ephemeral=True)

        if користувач.id == interaction.user.id:
            return await interaction.response.send_message("Не можна банити самого себе", ephemeral=True)

        if not interaction.guild.me.guild_permissions.ban_members:
            return await interaction.response.send_message("У мене не достантьо прав, щоб видавати бан", ephemeral=True)

        try:
            людина = interaction.guild.get_member(користувач.id) or await interaction.guild.fetch_member(користувач.id)
        except discord.NotFound:
            людина = None
        if людина is not None:
            if (людина.top_role >= interaction.user.top_role and interaction.user != interaction.guild.owner):
                return await interaction.response.send_message("Не можна банити людину, що має роль на тому ж рівні або вище ніж у вас", ephemeral=True)
        
            if людина.top_role >= interaction.guild.me.top_role:
                return await interaction.response.send_message("Я не можу забанити цю людину, бо її роль на рівні моєї або вища", ephemeral=True,)
        
        try:
            await interaction.guild.ban(користувач, reason=причина)
            embed = discord.Embed(description=f"{користувач.mention} був забанений", color=discord.Color.from_str("#e32412"))
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"Не вдалося забанити користувача {e}", ephemeral=True)


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
    await bot.add_cog(moderacija(bot))