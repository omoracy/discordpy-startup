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


    
@commands.Cog.listener()
    async def on_member_join(self, member):
        ment = member.mention
        await self.client.get_channel(channel id).send(f"{ment} has joined the server.")
        print(f"{member} has joined the server.")


bot.run(token)
