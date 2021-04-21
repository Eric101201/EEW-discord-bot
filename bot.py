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
    
    ggg = jdate1["1"]
    sec = jdate1["2"]
    
    if ggg == "0":
        await message_channel.send(f"地震速報，預估震度{ggg}級，{sec}秒後抵達")
    elif ggg == "1":
        await message_channel.send(f"地震速報，預估震度{ggg}級，{sec}秒後抵達")
    elif ggg == "2":
        await message_channel.send(f"地震速報，預估震度{ggg}級，{sec}秒後抵達")
    elif ggg == "3":
        await message_channel.send(f"地震速報，預估震度{ggg}級，{sec}秒後抵達")
    elif ggg == "4":
        await message_channel.send(f"地震速報，預估震度{ggg}級，{sec}秒後抵達")
    
    elif ggg == "5-":
        await message_channel.send(f"地震速報，預估震度5弱，{sec}秒後抵達")
        
    elif ggg == "5+":
        await message_channel.send(f"地震速報，預估震度5強，{sec}秒後抵達")
        
    elif ggg == "6-":
        await message_channel.send(f"地震速報，預估震度6弱，{sec}秒後抵達")
        
    elif ggg == "6+":
        await message_channel.send(f"地震速報，預估震度6強，{sec}秒後抵達")
        
    elif ggg == "7":
        await message_channel.send(f"地震速報，預估震度{ggg}級，{sec}秒後抵達")

    await asyncio.sleep(5)
    await bot.close()

bot.run("TOKEN")