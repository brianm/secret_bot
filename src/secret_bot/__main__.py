import os
import discord
import secret_bot

intents = discord.Intents.default()
intents.message_content = True
client = secret_bot.MyClient(intents=intents)
token = os.getenv('DISCORD_TOKEN')
if token is None:
    raise ValueError('DISCORD_TOKEN env var must be set to run the bot.')
client.run(token)