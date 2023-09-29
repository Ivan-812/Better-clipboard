import discord

TOKEN = 'MTE0OTY3NjIwNTE4MDcyMzI5MA.G-CgDw.xkk6lcc-em_4EF6uF_eh7LVk5ymUZ3tXpVbgR8'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author).split('#')[0]
    msg = str(message.content)
    ch = str(message.channel.name)
    print(f'{username}: {msg} ({ch})')
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


if __name__ == '__main__':
    client.run(TOKEN)
