# DiscordBotPython
A simple python bot.
Want a demo? https://discordapp.com/oauth2/authorize?client_id=621668247426564116&permissions=2147483135&scope=bot

Installation instructions (macos):
Create a new folder for the bot.
Download the bot and insert your client secret from the discord developer portal.
Invite your bot to your server.
Open the folder in terminal.
Run the following commands in bash (without the dollar sign):
$ python3 -m venv bot-env
$ source bot-env/bin/activate
$ pip install -U discord.py
Go to applications/python-3.7 or whatever version you have and run InstallCertificates.command (macOS default is outdated, blame Apple for this extra step.)
Go back to terminal, and run python3 bot.py (if you are already in the correct directory. Otherwise first cd/ to the correct directory.)
Log on to your discord server, and say !hi. The bot should return "Hello, world!"


Code borrowed from the following sources:
https://github.com/Rapptz/discord.py
https://discordpy.readthedocs.io/en/latest/api.html
