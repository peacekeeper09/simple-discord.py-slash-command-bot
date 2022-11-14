import discord

bot = discord.Bot()

@bot.slash_command()
async def hello(ctx, name: str = None):

    await ctx.respond(f"Hello!")

bot.run("bot token here")
