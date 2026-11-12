import discord
from discord.ext import commands
from discord import app_commands

class sendik(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="say", description="Скажіть будь-що від ім'я бота")
    @app_commands.default_permissions(administrator=True)
    async def say(self, interaction: discord.Interaction, повідомлення: str):
        try:
            await interaction.channel.send(повідомлення)
            embed = discord.Embed(description="✅ Успішно надіслано повідомлення", color=discord.Color.from_str("#3feb45"))
            await interaction.response.send_message(embed=embed, ephemeral=True)

        except discord.Forbidden:
            await interaction.response.send_message("У мене немає прав, щоб насилати повідомлення, або канал має обмежений доступ для мене", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message("Щось пішло не так", ephemeral=True)



    @app_commands.command(name="send_embed", description="Надішліть ембед від ім'я бота")
    @app_commands.default_permissions(administrator=True)
    async def send_embed(self, interaction: discord.Interaction, повідомлення: str):
        try:

            sembed = discord.Embed(description="✅ Успішно надіслано ембед", color=discord.Color.from_str("#3feb45"))
            await interaction.response.send_message(embed=sembed, ephemeral=True)

            embed = discord.Embed(description=повідомлення, color=discord.Color.from_str("#3feb45"))
            await interaction.response.send_message(embed=embed)

        except discord.Forbidden:
            await interaction.response.send_message("У мене немає прав, щоб насилати повідомлення, або канал має обмежений доступ для мене", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message("Щось пішло не так", ephemeral=True)


async def setup(bot):
    await bot.add_cog(sendik(bot))