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

    if message.content.lower().startswith('!bot'):
       await client.send_message(message.channel, 'Me chamou, <@{}>!?'.format(message.author.id))


    if message.content.lower() == '!iamdublador':
        await client.add_roles(message.author, discord.utils.get(message.server.roles, name="Dublador"))
        await client.send_message(message.channel, "<@{}> Setei seu cargo como \"Dublador\"!".format(message.author.id))

    if message.content.lower() == '!iamdubladora':
        await client.add_roles(message.author, discord.utils.get(message.server.roles, name="Dubladora"))
        await client.send_message(message.channel, "<@{}> Setei seu cargo como \"Dubladora\"!".format(message.author.id))

<<<<<<< HEAD
    if message.content.lower().startswith('!diga'):
=======
    if message.content.startswith('!diga'):
>>>>>>> ab7764a921bc1a38141f0157265313ff333d11ab
        args = message.content.split(" ")
        await client.send_message(message.channel, "{}".format(" ".join(args[1:])))


<<<<<<< HEAD
client.run('NDQ4MjA0OTY0NzU4ODE0NzIw.DeXhSA.PHanRBCS8J4cIZrKsnck5sAMesU')
=======
client.run('Token')
>>>>>>> ab7764a921bc1a38141f0157265313ff333d11ab
