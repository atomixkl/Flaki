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



    @app_commands.command(name="nyav", description="Флакі скаже няв, мяв чи мур :3")
    async def nyav(self, interaction: discord.Interaction):

        frazy = ["Няв", "Няв ^^", "Няв :3", "Нявк", "Нявк :3", "Нявк ^^", "Няяв", "Няяв OwO", "Няяв :3", "Няяв ^^", "Няяяв >:3с",
                "Ня :3", "Мур <:aww:1518327799264575590>", "Мур няв :3", "Мяр","Мяр~ :3", "Мяр ^^", "Мяв (˶>⩊<˶)", "Мяв :3"]
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
                "https://klipy.com/gifs/floragato-meowscarada",
                "https://klipy.com/gifs/meowscarada-mini-meowscarada",
                "https://klipy.com/gifs/pokemon-umbreon-7",
                "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cHo4NWMyOWh6b2pyNHJ1M2YwemFqNnpsMzVlNjcyMzZmN3U4N2QwNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/by9WL85LSZI2rz5dqI/giphy.gif",
                "https://klipy.com/gifs/furry-wypher-sleepy-paw-wiggle",
                "https://klipy.com/gifs/furry-wypher-appear",
                "https://klipy.com/gifs/wypher-furry-nuzzles-plushy",
                "https://klipy.com/gifs/umbreon-espeon-7",
                "https://klipy.com/gifs/get-tailed-idiot",
                "https://klipy.com/gifs/furry-wypher-fidget-spinner",
                "https://cdn.discordapp.com/attachments/1091441098829856949/1568514127125684245/attachment-127-1.gif",
                "https://tenor.com/view/girl-meow-cute-meme-funny-gif-16874634335787195581",
                "https://klipy.com/gifs/catboy-11",
                "https://cdn.discordapp.com/attachments/1395759462115049545/1397624584672645193/speechmemified_20241109_125929.gif",
                "https://cdn.discordapp.com/attachments/1091441098829856949/1539426194334818405/attachm1ent.gif",
                "https://cdn.discordapp.com/attachments/1441428937543778435/1516442827117039636/attachment.gif",
                "https://tenor.com/view/ugh-no-one-cares-kicks-paws-gif-9571080713961946033",
                "https://cdn.discordapp.com/attachments/1360999127642673175/1564705396441092166/togif.gif",
                "https://cdn.discordapp.com/attachments/1436816598911680583/1445002078266200138/attachment1.gif",
                "https://cdn.discordapp.com/attachments/1337987701428846603/1499232057836961914/attachment.gif",
                "https://gif.fxtwitter.com/tweet_video/HQMB3ZWa8AAa718.webp",
                "https://cdn.discordapp.com/attachments/919335494473621564/1281771287722852392/gosleep.gif",
                "https://cdn.discordapp.com/attachments/493156996644864001/1301571752744321124/stimky.gif",
                "https://cdn.discordapp.com/attachments/1350594975993167983/1368082448554135612/speechmemified_pasteimage_-_2025-05-03T004927.734.gif",
                "https://cdn.discordapp.com/attachments/1333252994141130876/1430038543786447002/stoopid.gif",
                "https://klipy.com/gifs/furr-de5",
                "https://cdn.discordapp.com/attachments/1477542053637263360/1494364931498311680/attachment-3-1.gif",
                "https://cdn.discordapp.com/attachments/1548629794176901170/1568238809617797160/attachment.gif",
                "https://cdn.discordapp.com/attachments/919989946188709888/1520274272919224512/gay_boy_on_the_internet.gif",
                "https://cdn.discordapp.com/attachments/1219787817257799753/1366293705643917322/67.gif",
                "https://cdn.discordapp.com/attachments/1119075068748771399/1463309972786909366/attachment-17.gif",
                "https://cdn.discordapp.com/attachments/1091441098829856949/1568340302102798387/image0.gif",
                "https://media.discordapp.net/attachments/995905426971447306/1024700422788747314/5AB8387F-E4AE-4174-AB8F-DC5C60F8A8D5.gif",
                "https://klipy.com/gifs/boykisser-46",
                "https://cdn.discordapp.com/attachments/1091441098829856949/1568382338545488053/915F8F57-AC4D-41F6-A00E-D2A00225FE20-1.gif",
                "https://cdn.discordapp.com/attachments/1091441098829856949/1568405296848703700/togif.gif",
                "https://cdn.discordapp.com/attachments/1386262631513591858/1386267979511238737/ab8f245ff30a2f0ee34da6e772961b7e_720p.gif",
                "https://klipy.com/gifs/wypher-cute",
                "https://cdn.discordapp.com/attachments/1503701055240671234/1568341235217862766/blahblahblah.gif",
                "https://cdn.discordapp.com/attachments/1110665701452157072/1360566276057075752/attachment.gif",
                "https://cdn.discordapp.com/attachments/1530205949372006541/1556916458594762782/togif.gif?backend=b2",
                "https://klipy.com/gifs/3-414",
                "https://cdn.discordapp.com/attachments/1305201294872674348/1412049391472218182/image0.gif",
                "https://cdn.discordapp.com/attachments/551911984149299220/1321542559603888158/furry_worry_speech.gif",
                "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnF1b2l1cHVoYjZ1YTZxaW5mMTY5OGRzb2t1bnR4djY1ZzZ5b2x6YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QBRAwQKQzTl9lScCOj/giphy.gif"

        
        ]
        obrgif = random.choice(gifs)

        await interaction.response.send_message(obrgif)


async def setup(bot):
    await bot.add_cog(bya(bot))