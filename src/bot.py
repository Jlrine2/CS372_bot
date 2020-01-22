import discord
import os
import re
from logger import update_log

client = discord.Client()

BotID 


# on every message
@client.event
async def on_message(message):

    # Do not reply to self

    if message.author == client.user:
        return
    
    if message.content.startswith('!help'):
        await message.channel.send('Log time in minutes spent on continuous learning. use !log \
        followed by a number... ex `!log 50 minutes watching a kubecon firetalk.`')
        return
    if message.content.startswith('!log'):
        try:
        parsed_message = re.match(r'\!log\ (?P<value>\d+) (minutes|^$)(?P<message>.*)', message.content)
        update_log(message.author.display_name, 
                parsed_message.group('value'),
                parsed_message.group('message')
                )
        except Exception as e:
            message.channel.send(f"error while logging {e}")
    return


# on initialization
@client.event
async def on_ready():
    print ('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run(BotID)