import discord
import settingmanager
import time
import datetime
from colorama import Fore, Style, Back
from discord.ext import commands

client = discord.Client()

def __init__():
    this.client = client

@client.event
async def on_ready():
    print("Selfbot ready.")

    time.sleep(1)

    await client.change_presence(activity=discord.Game(name="Discord Toolkit v0.01", type=3))

@client.event
async def on_message(message):
    now = datetime.datetime.now()
    # Workaround around selfbots being prevented from reading message content not sent by themselves.
    # Instead of accessing .content from the message object, this checks the latest message in message.channel, which results in the same result as message.content
    # This is slightly slower, but works for now.
    async for message in message.channel.history(limit=1):
        print(f"{Fore.BLACK}{Back.CYAN}" + "[{}:{}:{}] {}: {} | Server: {}".format(now.hour, now.minute, now.second, message.author, message.content, message.guild.name) + Back.RESET)



def start():
    token = settingmanager.get_setting("tokens", "main")

    if(token == ""):

        print("No token found. Exiting...")

        exit()
    else:
        client.run(token, bot=False)