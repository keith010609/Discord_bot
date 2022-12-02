import discord
import responses
from discord.ext import commands

async def send_msg(msg, user_msg):
    try: 
        response = responses.handle_response(user_msg)
        await msg.channel.send(response) 
    except Exception as e:
        print(e)

def run_bot(token):
    TOKEN = token
    intents = discord.Intents.all()
    intents.message_content = True
    bot = commands.Bot(command_prefix = ">",intents = intents, help_command = None)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is ready')
    
    @bot.command()
    async def hello(msg):
        if msg.author == bot.user:
            return 
        await send_msg(msg,f'Hi {msg.author}')
    
    @bot.command()
    async def join(msg):
        if msg.author.voice:
            channel = msg.message.author.voice.channel
            await channel.connect()
        else:
            await send_msg(msg,f'{msg.author} is not in any voice channel.')
    
    @bot.command()
    async def leave(msg):
        if msg.voice_client:
            await msg.guild.voice_client.disconnect()
            await send_msg(msg,f'Bye bye.')
        else:
            await send_msg(msg,f'I am not in any voice channel.')
    
    @bot.command()
    async def mua(msg):
        await send_msg(msg,f'😘')
    

    bot.run(TOKEN)