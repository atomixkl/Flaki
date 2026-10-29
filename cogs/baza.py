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

    @app_commands.command(name="nyav", description="Флакі скаже няв, і не тільки :3")
    async def nyav(self, interaction: discord.Interaction):

        frazy = ["Няв", "Няв :3", "Нявк", "Нявк ^^", "Няяв", "Няяв OwO", "Няяв :3", "Няяяв >:3с",
                "Ня :3", "Мур <:aww:1518327799264575590>", "Мяр (,,•᷄﹏•᷅,,)", "Мяв (˶>⩊<˶)"]
        obrfraza = random.choice(frazy)

        await interaction.response.send_message(obrfraza)
    
    @app_commands.command(name="rgif", description="Надсилає рандомну милу ґіфку :3")
    async def cutegif(self, interaction: discord.Interaction):
        
        gifs = ["https://cdn.discordapp.com/attachments/1109528336004284546/1248019112001798264/attachment-11.gif",
                "https://cdn.discordapp.com/attachments/1478738180386586777/1501989657888428113/emotion_download_1778172516363.gif",
                "https://cdn.discordapp.com/attachments/1003811310980575314/1411421299271667852/watermark.gif",
                "https://cdn.discordapp.com/attachments/1447644388590092462/1455229605937156116/TlkNJDU.gif",
                "https://cdn.discordapp.com/attachments/1062851552584413287/1349497231878914068/femhaj.gif",
                "https://cdn.discordapp.com/attachments/1363181535792205886/1413549139987533915/doc_2025-09-05_22-38-40.gif",
                "https://cdn.discordapp.com/attachments/1265636854431219772/1297946528643809385/silly.gif",
                "https://cdn.discordapp.com/attachments/1175744427411652608/1389668599555293284/togif.gif",
                "https://cdn.discordapp.com/attachments/1038805905053065292/1368416492080730213/IMG_3639.gif",
                ""
        
        
        
        ]
        obrgif = random.choice(gifs)

        await interaction.response.send_message(obrgif)


async def setup(bot):
    await bot.add_cog(bya(bot))