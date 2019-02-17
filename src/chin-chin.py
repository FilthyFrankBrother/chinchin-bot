import discord
from localsettings import token


class MyClient(discord.Client):

    def __init__(self):
        super().__init__()

        self.rampage = False

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        
        if message.author == client.user:
            return

        channel = message.channel
        
        if '+' in message.content:
            f = discord.File('../images/CHIN_CHIN_IS_NOT_PLEASED_fix.webp')
            await channel.send('\'Chu say {.name}?, fite me BITCH'.format(message.author),
                               file=f)



client = MyClient()
client.run(token)

