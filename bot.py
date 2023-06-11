import discord
import Player
from priv import TOKEN


async def send_message(message, user_message, dm_only):
    try: 
        response = Player.handle_command(message)
        await message.author.send(response) if dm_only else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # so we don't have infinite loops referencing themself
        if message.author == client.user: 
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if user_message.startswith('?') == False:
            return

        # TODO
        # construct a way to verify if the person is already has a player object, 
        # and if not create a new one
        await send_message(message, user_message, dm_only=False)

    client.run(TOKEN)