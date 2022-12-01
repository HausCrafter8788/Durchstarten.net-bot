import nextcord
import os

from config import TOKEN
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix=',', intents=intents)

TOKEN = os.environ['TOKEN']

cogs = []

@bot.event
async def on_ready():
    print('Logget in as:')
    print(str(bot.user.name) + ' ' + str(bot.user.id))
    print("Loading Cogs . . .")
    for cog in cogs:
        cog_ = cog.split('.')
        if cog_[2] == 'commands':
            bot.load_extension(cog)
            print('Command ' + cog_[3] + ' was loaded')
        elif cog_[2] == 'events':
            bot.load_extension(cog)
            print('Event ' + cog_[3] + ' was loaded')
        elif cog_[2] == 'tasks':
            bot.load_extension(cog)
            print('Task ' + cog_[3] + ' was loaded')

bot.run(TOKEN)