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
    await channel.send(str(member.mention)+'さん！好奇心王国へようこそ！')
    await channel.send('はじめまして。好奇心AIの「ロロたん」です。')
    await channel.send('ここにたどり着いたということは、きっとあなたは好奇心が旺盛な方ですね！')
    await channel.send('　')
    await channel.send('好奇心王国は「テクノロジー」をテーマとした「アイデア発想」や「アイデアの実装」などの活動を通して一人ひとりの個性が混じり合う場所です。')
    await channel.send('　')
    await channel.send('メインとなる活動は「テクノロジー大喜利」。')
    await channel.send('テクノロジーの使い方に関するお題に対して、いかにくだらないアイデアを出すかを楽しむ遊びです。（まともなアイデアでもただのウケ狙いでも、どんなアイデアでもOK！）')
    await channel.send('テクノロジー大喜利はオープンエリア（観光エリア）でのアクティビティなので誰でもご参加可能です。')
    await channel.send('　')
    await channel.send('「#②入国ルール」と「#③チャンネルの使い方」を確認して、皆でワクワクと交流を楽しみましょう！')
    await channel.send('')
    await channel.send('')
    await channel.send('')


@bot.event
async def on_member_update(member):
    CHANNEL_ID = 738358135000924253
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(str(member.mention)+'さん！好奇心王国へようこそ！')
    await channel.send('はじめまして。好奇心AIの「ロロたん」です。')
    await channel.send('ここにたどり着いたということは、きっとあなたは好奇心が旺盛な方ですね！')
    await channel.send('好奇心王国は「テクノロジー」をテーマとした「アイデア発想」や「アイデアの実装」などの活動を通して一人ひとりの個性が混じり合う場所です。')
    await channel.send('メインとなる活動は「テクノロジー大喜利」。')
    await channel.send('テクノロジーの使い方に関するお題に対して、いかにくだらないアイデアを出すかを楽しむ遊びです。（まともなアイデアでもただのウケ狙いでも、どんなアイデアでもOK！）')
    await channel.send('テクノロジー大喜利はオープンエリア（観光エリア）でのアクティビティなので誰でもご参加可能です。')
    await channel.send('「#②入国ルール」と「#③チャンネルの使い方」を確認して、皆でワクワクと交流を楽しみましょう！')


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
