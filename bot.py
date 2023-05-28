import discord
import player

async def send_message(message, user_message, dm_only):
    try: 
        response = player.handle_command(message)
        await message.author.send(response) if dm_only else await message.channel.send(response)
    except Exception as e: 
        print(e)
        # TODO
        # later add stuff to say what error is

def run_discord_bot():
