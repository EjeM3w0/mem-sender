import discord
from discord.ext import commands
import os, random
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_pokemon_image_url():    
    url = 'https://pokeapi.co'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'Бот {bot.user} успешно запущен!')

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)



@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    '''По команде dog вызывает функцию get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command('pokemon')
async def pokemon(ctx):
    '''По команде pokemon вызывает функцию get_duck_image_url'''
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)

@bot.command('fox')
async def fox(ctx):
    '''По команде dog вызывает функцию get_duck_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

bot.run("")
