'''This python file contains the code to run a bot on a discord server whose
only function is to post a sakurafish image everyday until you like it.'''

import discord
from discord.ext import commands, tasks


client = commands.Bot(command_prefix='!')
count = 0

@client.event
async def on_ready():
    print('Ready')

#sending the sakurafish image every 24 hours. keeps count of
#how many have been sent
@tasks.loop(hours=24)
async def sendImage():
    global count
    count+=1
    message_channel = client.get_channel('DISCORD CHANNEL ID HERE')
    image = discord.Embed()
    image.set_image(url='https://cdn.discordapp.com/attachments/' +
                    '738140134184058935/738284093380231198/sakurafish.jpg')
    await message_channel.send(f'#{count}', embed=image)


@sendImage.before_loop
async def before():
    await client.wait_until_ready()

sendImage.start()

client.run('DISCORD BOT TOKEN HERE')
