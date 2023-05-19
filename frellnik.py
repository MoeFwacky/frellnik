print("███████ ██████  ███████ ██      ██      ███    ██ ██ ██   ██")
import asyncio
import configparser
import discord
import openai
import os
from discord.ext import commands

if os.name == 'nt':
    delimeter = '\\'
else:
    delimeter = '/'
print("██      ██   ██ ██      ██      ██      ████   ██ ██ ██  ██ ")   
scriptPath = os.path.realpath(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read(scriptPath + delimeter + 'config.ini')

print("█████   ██████  █████   ██      ██      ██ ██  ██ ██ █████  ")   
openai.organization = config['default']['openai org key']
openai.api_key = config['default']['openai api key']
models = openai.Model.list()

print("██      ██   ██ ██      ██      ██      ██  ██ ██ ██ ██  ██ ")   
discord_token = config['default']['discord api key']
discord_intents=discord.Intents.default()
discord_intents.message_content=True
discord_bot=commands.Bot(intents=discord_intents, command_prefix='!')
general_channel_id = config['discord']['channel id']

print("██      ██   ██ ███████ ███████ ███████ ██   ████ ██ ██   ██")
frellnik_role = config['default']['base prompt']

@discord_bot.event
async def on_ready():
    print("[DISCORD]",end=" ")
    print(f'{discord_bot.user.name} has connected to Discord.')
    print("Generating greeting")
    reply = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-0301',
        messages=[
            {'role':'system','content':frellnik_role},
            {'role':'user','content':'You have just woken up after being knocked out. Say something short and funny'}
            ]
        )
    print(reply)
    general_channel = discord_bot.get_channel(general_channel_id)
    await general_channel.send(reply['choices'][0]['message']['content'])

@discord_bot.event 
async def on_message(message):
    print(message.content)
    if message.author.bot: return
    if discord_bot.user.mentioned_in(message):
        print("[DISCORD]",end=" ")
        print(f'{discord_bot.user.name} has been pinged. Generating reply...')
        reply = openai.ChatCompletion.create(
            model='gpt-3.5-turbo-0301',
            messages=[
                {'role':'system','content':frellnik_role},
                {'role':'user','content':'Give a wrong answer and make a funny comment about: '+message.content}
                ]
            )
        print(reply)
        await message.channel.send(reply['choices'][0]['message']['content'], reference=message)
            
discord_bot.run(discord_token, log_handler=None)