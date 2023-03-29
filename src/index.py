import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
from discord import app_commands
guildid = discord.Object(id =  PUT_YOUR_GUILD_ID_HERE)

class Client(discord.Client):
    async def on_ready(self):
        await tree.sync(guild = discord.Object(id = guildid))
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
client = Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = 'ping', guild=discord.Object(id = guildid))
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('**Pong!**')


client.run('DISCORD_APPLICATION_TOKEN')


