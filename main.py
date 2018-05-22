import discord
import asyncio

# Defining the client that the bot will log in
client = discord.Client()


@client.event
async def on_ready():
    # Basic definitions to the entrance of the robot to the network
    print("BOT ON **")
    print("Name= {}".format(client.user.name))
    print("------------")s


@client.event
async def on_message(message):
    if message.content.startswith('!bot'):
       await client.send_message(message.channel, 'Me chamou!?')
    if message.content.startswith('!iamdublador'):
        #WRONG!!
        await client.add_roles(member=message.author, *"Dublador")
    if message.content.startswith('!iamdubladora'):
        #WRONG!!
        await client.add_roles(member=message.author, *"Dubladora")


client.run('BOT TOKEN')
