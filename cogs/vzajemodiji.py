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
        "https://static2.klipy.com/ii/e293a233a303a98e471f78d04e13a1b0/ba/1d/anJe7cZh.gif",
        "https://static2.klipy.com/ii/da290b156d64898341638f3c299e7478/ff/93/5sQUvdXu.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/08/b9/k84sjhgxKTXRUp.gif",
        "https://static2.klipy.com/ii/4e7bea9f7a3371424e6c16ebc93252fe/dd/91/vY7gLrEOuvxg.gif",
        "https://nekos.best/api/v2/hug/4619bde0-9f22-4010-a58a-d6a4cb8d12a4.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/a6/5b/024vVAokiCm3He.gif"


        ]

        rgif = random.choice(gifky)

        embed = discord.Embed(description=f"**{interaction.user.mention} обійняли {користувач.mention}**")
        embed.set_image(url=rgif)
        print(rgif)
        await interaction.response.send_message(content=користувач.mention, embed=embed)


    @app_commands.command(name="cuddle", description="Обійміть користувача")
    async def cuddle(self, interaction: discord.Interaction, користувач: discord.Member):

        gifky = [
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/a6/d3/pQbVOhjmY6IMAxxykA.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/24/83/RKNXaszfm6XL3.gif",
        "https://static2.klipy.com/ii/71b2873e478b9d8d0482ea3ec777ba7f/b0/f6/IBieSXmf.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/5d/29/Dw96Wd5mWMj6O9r.gif",
        "https://static2.klipy.com/ii/2f34308bfc69e8c858753b83566e3ab4/17/27/AzmHjRWrK2ebNswMa.gif"

        ]

        rgif = random.choice(gifky)

        embed = discord.Embed(description=f"**{interaction.user.mention} обійняли {користувач.mention}**")
        embed.set_image(url=rgif)
        print(rgif)
        await interaction.response.send_message(content=користувач.mention, embed=embed)


    @app_commands.command(name="pet", description="Погладьте користувача")
    async def pet(self, interaction: discord.Interaction, користувач: discord.Member):

        gifky = [
        "https://static2.klipy.com/ii/4e7bea9f7a3371424e6c16ebc93252fe/83/ac/KhlmotLP4bRD9.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/c1/58/BF2vY1vZXqt7.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/90/6f/Mil8duolhutj63Yy.gif",
        "https://static2.klipy.com/ii/e293a233a303a98e471f78d04e13a1b0/c2/b1/sDk1NZ06.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/0f/e3/QmKlFzi6M2brR.gif",
        "https://cdn.discordapp.com/attachments/1091441098829856949/1568512191735402546/X2Twitter.com_Pl6CClPx4G0tcE02_720p.gif",
        "https://cdn.discordapp.com/attachments/1259635449773818087/1371910998797320222/15CopyA4E794E-ezgif.com-video-to-gif-converter.gif",
        "https://cdn.discordapp.com/attachments/1447644388590092462/1455229605937156116/TlkNJDU.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/a4/6d/nH7q41KIrvdkMl0Y9ZOk.gif",
        "https://static2.klipy.com/ii/4493325008d34b7bf8cd6813cd5c1619/51/1d/Dfvpu8dfu7pCnJ.gif"


        ]

        rgif = random.choice(gifky)

        embed = discord.Embed(description=f"**{interaction.user.mention} погладили {користувач.mention}**")
        embed.set_image(url=rgif)
        print(rgif)
        await interaction.response.send_message(content=користувач.mention, embed=embed)


    @app_commands.command(name="kiss", description="Цьомніть користувача")
    async def kiss(self, interaction: discord.Interaction, користувач: discord.Member):

        gifky = [
        "https://tenor.com/view/furry-furry-kiss-leash-gif-5474272115302089942"


        ]

        rgif = random.choice(gifky)

        embed = discord.Embed(description=f"**{interaction.user.mention} поцілували {користувач.mention}**")
        embed.set_image(url=rgif)
        print(rgif)
        await interaction.response.send_message(content=користувач.mention, embed=embed)


async def setup(bot):
    await bot.add_cog(vzajemodiji(bot))