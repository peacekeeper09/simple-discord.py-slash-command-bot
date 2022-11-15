
# Simple slash command bot using discord.py(pycord)

Hello everyone, hope you all are doing good. Here I will show you all how to create a simple slash command bot using pycord.



These are some resources that you need to install.
Since am using windows I will have to install them on terminal.

# Prerequisite

You must have [Python](https://www.python.org/downloads/) installed on your respective device.

After making sure that you have python installed, make sure you have a good idle, developers across the world recommend [VSCODE](https://code.visualstudio.com/download).


## Installation
Copy these and paste it in terminal if you are using windows. For linux you will have to search it up on internet.

```bash
 # Linux/macOS
python3 -m pip install -U py-cord

# Windows
py -3 -m pip install -U py-cord
```
Otherwise to get voice support you should run the following command:
```bash
# Linux/macOS
python3 -m pip install -U "py-cord[voice]"

# Windows
py -3 -m pip install -U py-cord[voice]
```

To install additional packages for speedup, run the following command:
```bash
# Linux/macOS
python3 -m pip install -U "py-cord[speed]"
# Windows
py -3 -m pip install -U py-cord[speed]
```

or if you do not want to clone the repository:
```bash
# Linux/macOS
python3 -m pip install git+https://github.com/Pycord-Development/pycord
# Windows
py -3 -m pip install git+https://github.com/Pycord-Development/pycord
```
## Setup

![App Screenshot](https://cdn.discordapp.com/attachments/883097731667750954/1041846462973231154/image.png)

# Creating a discord bot

For making your own discord bot, you will have to visit:- https://discord.com/developers/applications 



- New application
- Choose a name for your bot.
- Scroll down to Bot 
- From there you will have to select Add Bot
- Select Yes do it!
Congrats you have successfully made your bot!

- You can copy your bot token by clicking on Reset Token under Bot tab. It will be needed for running the bot.
![App Screenshot](https://cdn.discordapp.com/attachments/883097731667750954/1041853793345749014/image.png)
Don't get happy hackers, I have already reset the token.
# Also you can enable 
- [Presence intent](https://discord.com/developers/docs/topics/gateway#presence-update)
- [Server intent](https://discord.com/developers/docs/topics/gateway#list-of-intents)
- [Message intent](https://support-dev.discord.com/hc/en-us/articles/4404772028055)

# Code
```bash
import discord

bot = discord.Bot()

@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")

@bot.user_command(name="Bot will greet you back!")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

bot.run("bot token here")

```

![App Screenshot](https://cdn.discordapp.com/attachments/883097731667750954/1041851821167222854/image.png)
