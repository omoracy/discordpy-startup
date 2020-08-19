from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)



@bot.command(pass_context=True)
@bot.event
async def on_member_join(ctx, member):
    print(f'{member} has joined a server.')
    await ctx.send(f"Hello {member}!")
    await ctx.member.send(f"Welcome to the server!")


bot.run(token)
