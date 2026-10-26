import discord
import os 
from discord.ext import commands
from discord import app_commands
from openai import AsyncOpenAI
from datetime import datetime
from zoneinfo import ZoneInfo

modeli = ("gemini-3.5-flash-lite", "gemini-3.1-flash-lite", "gemini-3.6-flash")


class AICog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.aiclient = AsyncOpenAI(api_key=os.getenv("GMN_TOKEN"), base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

    @app_commands.command(name="ai", description="Запитайте будь-що у ШІ!")
    async def aicmd(self, interaction: discord.Interaction, промпт: str):
        await interaction.response.defer()

        try:
            now = datetime.now(ZoneInfo("Europe/Kyiv")).strftime("%d.%m.%Y, %H:%M")

            contentgmn = (
                "Ти мило спілкуєшся з людьми, використовуєш :3."
                "Ніколи не розмовляєш російською."
                "Тебе звати Флакі, ти фурі фембойчик."
                f"Зараз поточний час: {now}"
                )

            for model_name in modeli:
                vidpovid = await self.aiclient.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": contentgmn},
                        {"role": "user", "content": промпт} 
                    ]
                )

            vidpovidabs = vidpovid.choices[0].message.content

            
            await interaction.followup.send(vidpovidabs)

        except Exception as e:
            print(f"Виникла помилка при звернені до ШІ: {e}")

async def setup(bot):
    await bot.add_cog(AICog(bot))