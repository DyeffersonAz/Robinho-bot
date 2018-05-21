import discord
import asyncio

# Definindo o cliente aonde o bot comunicará com a API
client = discord.Client()


@client.event
async def on_ready():
    # Definições básicas de entrada do bot à rede
    print("BOT ON **")
    print("Nome= {}".format(client.user.name))
    print("------------")


@client.event
async def on_message(message):
    if message.content.startswith('!bot'):
       await client.send_message(message.channel, 'Me chamou!?')


client.run('NDQ4MjA0OTY0NzU4ODE0NzIw.DeSvkw.QayCBGlI0M5rBKR9iLk6hAXKEJE')
