import discord
import re
import datetime
from discord.ext import commands
from discord import app_commands

class moderacija(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Видає бан")
    @app_commands.guild_only()
    @app_commands.default_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, користувач: discord.User, причина: str | None = None, приховано: bool = False):

        if not interaction.user.guild_permissions.ban_members:
            return await interaction.response.send_message("Ви не маєте прав, щоб забанити цього користувача", ephemeral=True)

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
                return await interaction.response.send_message("Не можна банити користувача, що має роль на тому ж рівні або вище ніж у вас", ephemeral=True)
        
            if людина.top_role >= interaction.guild.me.top_role:
                return await interaction.response.send_message("Я не можу забанити цю людину, бо її роль на рівні моєї або вища", ephemeral=True)
            
            if людина == interaction.guild.owner or людина.guild_permissions.administrator:
                return await interaction.response.send_message("Я не можу видати бан власнику чи адміністратору сервера", ephemeral=True)
        
        try:
            await interaction.guild.ban(користувач, reason=причина)
            embed = discord.Embed(description=f"{користувач.mention} були забанені.", color=discord.Color.from_str("#f51d1d"))

            await interaction.response.send_message(embed=embed, ephemeral=приховано)
        except Exception as e:
            await interaction.response.send_message(f"Не вдалося забанити користувача: {e}", ephemeral=True)



    @app_commands.command(name="unban", description="Знімає бан з користувача")
    @app_commands.guild_only()
    @app_commands.default_permissions(ban_members=True)
    async def unban(self, interaction: discord.Interaction, користувач: discord.Member, час: str, причина: str | None = None, приховано: bool = False):
        embed = discord.Embed(description=f"Успішно знято бан з {користувач.mention}.", color=discord.Color.from_str("#18f2a6"))
        await interaction.response.send_message(embed=embed, ephemeral=приховано)



    @app_commands.command(name="fakeban", description="Фейковий бан користувача")
    async def fakeban(self, interaction: discord.Interaction, користувач: discord.Member, причина: str | None = None):
        embed = discord.Embed(description=f"{користувач.mention} було забанено.", color=discord.Color.from_str("#f51d1d"))
        await interaction.response.send_message(embed=embed)



    @app_commands.command(name="tempban", description="Видає тимчасовий бан")
    @app_commands.guild_only()
    @app_commands.default_permissions(ban_members=True)
    async def tempban(self, interaction: discord.Interaction, користувач: discord.Member, час: str, причина: str | None = None, приховано: bool = False):
        embed = discord.Embed(description=f"{користувач.mention} отримали тимчасовий бан.", color=discord.Color.from_str("#f51d1d"))
        await interaction.response.send_message(embed=embed, ephemeral=приховано)



    @app_commands.command(name="timeout", description="Видає таймаут")
    @app_commands.guild_only()
    @app_commands.default_permissions(moderate_members=True)
    async def timeout(self, interaction: discord.Interaction, користувач: discord.User, час: str, причина: str | None = None, приховано: bool = False):

        if not interaction.user.guild_permissions.moderate_members:
            return await interaction.response.send_message("Ви не маєте прав, щоб видати таймаут цьому користувачу", ephemeral=True)

        if користувач.id == interaction.user.id:
            return await interaction.response.send_message("Не можна видати таймаут самому собі", ephemeral=True)

        if not interaction.guild.me.guild_permissions.moderate_members:
            return await interaction.response.send_message("У мене не достатньо прав, щоб видавати таймаут", ephemeral=True)

        try:
            людина = interaction.guild.get_member(користувач.id) or await interaction.guild.fetch_member(користувач.id)
        except discord.NotFound:
            людина = None

        if людина is None:
            return await interaction.response.send_message("Цього користувача немає на сервері", ephemeral=True)

        if людина.top_role >= interaction.user.top_role and interaction.user != interaction.guild.owner:
            return await interaction.response.send_message("Не можна видати таймаут користувачу, що має роль на тому ж рівні або вище ніж у вас", ephemeral=True)
        
        if людина.top_role >= interaction.guild.me.top_role:
            return await interaction.response.send_message("Я не можу видати таймаут користувачу, бо її роль на рівні моєї або вища", ephemeral=True)
        
        if людина == interaction.guild.owner or людина.guild_permissions.administrator:
            return await interaction.response.send_message("Я не можу видати таймаут власнику чи адміністратору сервера", ephemeral=True)

        match = re.match(r"^(\d+)([smhd])$", час.lower())
        if not match:
            return await interaction.response.send_message("Неправильний формат часу. Формати: 30s, 10m, 1h, 1d", ephemeral=True)

        amount, unit = match.groups()
        seconds = int(amount) * {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}[unit]

        if seconds <= 0:
            return await interaction.response.send_message("Час має бути більшим за 0", ephemeral=True)
        if seconds > 28 * 86400:
            return await interaction.response.send_message("Таймаут не може перевищувати 28 днів", ephemeral=True)

        тривалість = datetime.timedelta(seconds=seconds)

        try:
            await людина.timeout(тривалість, reason=причина)
            embed = discord.Embed(description=f"{користувач.mention} отримали таймаут.", color=discord.Color.from_str("#f51d1d"))
            await interaction.response.send_message(embed=embed, ephemeral=приховано)
        except Exception as e:
            await interaction.response.send_message(f"Не вдалося видати таймаут: {e}", ephemeral=True)



    @app_commands.command(name="kick", description="Викидає користувача зі сервера")
    @app_commands.guild_only()
    @app_commands.default_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, користувач: discord.User, причина: str | None = None, приховано: bool = False):

        if not interaction.user.guild_permissions.kick_members:
            return await interaction.response.send_message("Ви не маєте прав, щоб викинути цю людину", ephemeral=True)

        if користувач.id == interaction.user.id:
            return await interaction.response.send_message("Не можна викинути самого себе", ephemeral=True)

        if not interaction.guild.me.guild_permissions.kick_members:
            return await interaction.response.send_message("У мене не достантьо прав, щоб викидати користувачів", ephemeral=True)

        try:
            людина = interaction.guild.get_member(користувач.id) or await interaction.guild.fetch_member(користувач.id)
        except discord.NotFound:
            людина = None

        if людина is None:
            return await interaction.response.send_message("Цього користувача немає на сервері", ephemeral=True)

        if людина.top_role >= interaction.user.top_role and interaction.user != interaction.guild.owner:
                return await interaction.response.send_message("Не можна викинути користувача, що має роль на тому ж рівні або вище ніж у вас", ephemeral=True)
        
        if людина.top_role >= interaction.guild.me.top_role:
                return await interaction.response.send_message("Я не можу викинути цього користувача, бо її роль на рівні моєї або вища", ephemeral=True)
        
        if людина == interaction.guild.owner or людина.guild_permissions.administrator:
            return await interaction.response.send_message("Я не можу викинути власника чи адміністратора сервера", ephemeral=True)

        try:
            await interaction.guild.kick(користувач, reason=причина)
            embed = discord.Embed(description=f"{користувач.mention} були викинуті зі серверу.", color=discord.Color.from_str("#f51d1d"))
            await interaction.response.send_message(embed=embed, ephemeral=приховано)
        except Exception as e:
            await interaction.response.send_message(f"Не вдалося викинути користувача: {e}", ephemeral=True)



    @app_commands.command(name="warn", description="Видає попередження")
    @app_commands.guild_only()
    @app_commands.default_permissions(moderate_members=True)
    async def warn(self, interaction: discord.Interaction, користувач: discord.Member, причина: str | None = None):
        embed = discord.Embed(description=f"{користувач.mention} отримали попередження.", color=discord.Color.from_str("#edcf37"))
        await interaction.response.send_message(embed=embed)



    @app_commands.command(name="softwarn", description="Видає попередження")
    @app_commands.guild_only()
    @app_commands.default_permissions(moderate_members=True)
    async def softwarn(self, interaction: discord.Interaction, користувач: discord.Member, причина: str | None = None):
        embed = discord.Embed(description=f"{користувач.mention} отримали попередження.", color=discord.Color.from_str("#edcf37"))
        await interaction.response.send_message(embed=embed)


# #edcf37 Жовтий
# #f51d1d Червоний
# #e67a2e Помаранчевий
# #18f2a6 Бюрюзовий

async def setup(bot):
    await bot.add_cog(moderacija(bot))