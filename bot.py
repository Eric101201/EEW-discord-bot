import discord
from discord.ext import commands
import json
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!!!")

@bot.event
async def on_ready():
    message_channel = bot.get_channel(808976065984200732)
    
    with open('file.json', mode='r', encoding='UTF8') as jfile:
        jdate1 = json.load(jfile)
    
    ggg = re.sub(r"(\d)$", "\\1級", jdate1["1"]).replace("-", "弱").replace("+", "強")
    sec = jdate1["2"]
    
    await message_channel.send(f"地震速報，預估震度{ggg}，{sec}秒後抵達")
    await asyncio.sleep(5)
    await bot.close()

bot.run("TOKEN")