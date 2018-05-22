import discord
import asyncio

# Defining the client that the bot will log in
client = discord.Client()


@client.event
async def on_ready():
    # Basic definitions to the entrance of the robot to the network
    print("BOT ON **")
    print("Name= {}".format(client.user.name))
    print("------------")


@client.event
async def on_message(message):
    dublador = discord.utils.get(message.server.roles, name="Dublador")
    dubladora = discord.utils.get(message.server.roles, name="Dubladora")

    if message.content.startswith('!bot'):
       await client.send_message(message.channel, 'Me chamou, <@{}>!?'.format(message.author.id))


    if message.content == '!iamdublador':
        await client.add_roles(message.author, dublador)
        await client.send_message(message.channel, "<@{}> Setei seu cargo como \"Dublador\"!".format(message.author.id))

    if message.content == '!iamdubladora':
        await client.add_roles(message.author, dubladora)
        await client.send_message(message.channel, "<@{}> Setei seu cargo como \"Dubladora\"!".format(message.author.id))

client.run('Token')
