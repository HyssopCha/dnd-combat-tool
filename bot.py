import discord
import player
from priv import TOKEN

async def send_message(message, user_message, dm_only):
    try: 
        response = player.handle_command(message)
        await message.author.send(response) if dm_only else await message.channel.send(response)
    except Exception as e: 
        print(e)
        # TODO
        # later add stuff to say what error is


def run_discord_bot():
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print('f{client.user} is now running!')

    client.run(TOKEN)