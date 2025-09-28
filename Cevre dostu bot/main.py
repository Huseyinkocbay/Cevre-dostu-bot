import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="#", intents=intents)

@bot.event
async def on_ready():
    print(f'Merhaba! {bot.user}')
    
@bot.command()
async def cop(ctx):

    text = "Cöpler cevreye zararlidir. Özelilkle plastikler ve mikro plastikler"
    await ctx.send(text)
    return

@bot.command()
async def plastic(ctx):

    text = "Plastikler yuz yillar boyunca kaybolmadan durabiliyor, ve bu cevreye cok zarar veriyor."
    await ctx.send(text)
    return

@bot.command()
async def video(ctx):
    url = 'https://www.youtube.com/shorts/SqrC17jbcys?feature=share'
    await ctx.send(url)
    




bot.run("token")
    