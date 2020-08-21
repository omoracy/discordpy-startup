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


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_member_join(member):
    CHANNEL_ID1 = 745875403482071085
    CHANNEL_ID2 = 745860737062273045
    CHANNEL_ID3 = 738358135470817290
    channel1 = bot.get_channel(CHANNEL_ID1)
    channel2 = bot.get_channel(CHANNEL_ID2)
    channel3 = bot.get_channel(CHANNEL_ID3)
    await channel1.send(str(member.mention)+'さん！好奇心王国へようこそ！\n好奇心AIの「ロロたん」です。\nここにたどり着いたということは、きっとあなたは好奇心の旺盛な方ですね！\n\n好奇心王国は「テクノロジー」をテーマとした「アイデア発想」や「アイデアの実装」などの活動を通して一人ひとりの個性が混じり合う場所です。\nメインとなる活動は「テクノロジー大喜利」。テクノロジーの使い方に関するお題に対して、いかにくだらないアイデアを出すかを楽しむ遊びです。（まともなアイデアでもただのウケ狙いでも、どんなアイデアでもOK！）\nOPENエリア（観光エリア）でのアクティビティなので誰でもご参加可能です。\n\nまずは「`#str(channel2)`」と「`#③王国のルール`」のご確認を。\nワクワクする活動と交流を楽しむロロ〜！')


# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

bot.run(token)
