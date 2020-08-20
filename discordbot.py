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
    CHANNEL_ID = 738358135000924253
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(str(member.mention)+'さん！好奇心王国へようこそ！\nはじめまして。好奇心AIの「ロロたん」です。\nここにたどり着いたということは、きっとあなたは好奇心が旺盛な方ですね！\n\n好奇心王国は「テクノロジー」をテーマとした「アイデア発想」や「アイデアの実装」などの活動を通して一人ひとりの個性が混じり合う場所です。\nメインとなる活動は「テクノロジー大喜利」。\nテクノロジーの使い方に関するお題に対して、いかにくだらないアイデアを出すかを楽しむ遊びです。（まともなアイデアでもただのウケ狙いでも、どんなアイデアでもOK！）\n\nテクノロジー大喜利はオープンエリア（観光エリア）でのアクティビティなので誰でもご参加可能です。\n\nまずは「#②入国ルール」と「#③チャンネルの使い方」のご確認を。\n皆でワクワクと交流を楽しみましょう！'


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
