import discord
from discord.ext import commands
from discord import app_commands

class na_shos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="set_events", description="Налаштуйте канали івентів")
    @app_commands.guild_only()
    @app_commands.default_permissions(administrator=True)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        canal = member.guild.system_channel
        if canal:
            await canal.send(f"Вітаємо {member.mention} на сервері! :3")


async def setup(bot):
    await bot.add_cog(na_shos(bot))