import discord
import asyncio

from discord import Server
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

    if message.content.lower() == '!iamajudante' or message.content.lower() == '!iamguardiao':
        await client.send_message(message.server.get_member("235128888458477568"), "Um usuário chamado <@{}> pediu para ser guardião, o ideal é que ele se torne ajudante, mas se quiser pode analisar o perfil dele, para conversar com ele ou quaisquer atitudes que você queira tomar!".format(message.author.id))
        await client.send_message(message.server.get_member("284114889235103745"), "Um usuário chamado <@{}> pediu para ser guardião, o ideal é que ele se torne ajudante, mas se quiser pode analisar o perfil dele, para conversar com ele ou quaisquer atitudes que você queira tomar!".format(message.author.id))

    if message.content.lower().startswith('!diga'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "{}".format(" ".join(args[1:])))


client.run('Token')
