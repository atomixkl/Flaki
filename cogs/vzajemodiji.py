import discord
import random
from discord.ext import commands
from discord import app_commands

class vzajemodiji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hug", description="Обійміть користувача")
    async def hug(self, interaction: discord.Interaction, користувач: discord.Member):

        gifky = [
        "https://nekos.best/api/v2/hug/46115641-beef-4ad4-841f-dd2687b1d9e0.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/a6/d3/pQbVOhjmY6IMAxxykA.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/24/83/RKNXaszfm6XL3.gif",
        "https://static2.klipy.com/ii/e293a233a303a98e471f78d04e13a1b0/ba/1d/anJe7cZh.gif",
        "https://static2.klipy.com/ii/6b3a6ab13999af763b4db87b91ee67d0/95/a3/f44Xb7Z8qPTBCOa.mp4",
        "https://static2.klipy.com/ii/da290b156d64898341638f3c299e7478/ff/93/5sQUvdXu.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/08/b9/k84sjhgxKTXRUp.gif",
        "https://static2.klipy.com/ii/4e7bea9f7a3371424e6c16ebc93252fe/9c/af/wEF9YGGwYrDtpLG9344q.gif",
        "https://static2.klipy.com/ii/4e7bea9f7a3371424e6c16ebc93252fe/dd/91/vY7gLrEOuvxg.gif"


        ]

        rgif = random.choice(gifky)

        embed = discord.Embed(description=f"**{interaction.user.mention} обійняли {користувач.mention}!**")
        embed.set_image(url=rgif)
        print(rgif)
        await interaction.response.send_message(content=користувач.mention, embed=embed)


async def setup(bot):
    await bot.add_cog(vzajemodiji(bot))