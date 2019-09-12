import discord

msgtable = {
		"hi": "Hello, world!",
		"ping": "Pong!",
		"about": "[Your about message here]",
		"customcmd": "Hey, why aren't you customizing me?"
		}


import discord

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message(self, message):
		# don't respond to ourselves
		if message.author == self.user:
			return
		if message.content[0] == '!':
			await message.channel.send(msgtable[message.content[1:]])

client = MyClient()
client.run('NjIxNjY4MjQ3NDI2NTY0MTE2.XXostQ.V2gEon-RGIAlmUUaO2YwobWm4tE')