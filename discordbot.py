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
    channel = bot.get_channel(745875403482071085)
    # 起動時にメッセージの送信
    await channel.send('今日も働いているロロ〜')


@bot.event
async def on_member_join(member):
    CHANNEL_ID1 = 745875403482071085
    CHANNEL_ID2 = 745860737062273045
    CHANNEL_ID3 = 738358135470817290
    channel1 = bot.get_channel(CHANNEL_ID1)
    channel2 = bot.get_channel(CHANNEL_ID2)
    channel3 = bot.get_channel(CHANNEL_ID3)
    await channel1.send(str(member.mention)+'さん！好奇心王国へようこそ！\n好奇心AIの「ロロたん」です。\nここにたどり着いたということは、きっとあなたは好奇心の旺盛な方ですね！\n\n好奇心王国は、一人ひとりの好奇心から生まれる活動を通して個性が混じり合う場所です。\nメインとなる活動は「テクノロジーを使ったくだらないアイデアの実装」です。\n\nOPENエリア(観光エリア)でも楽しめることはあると思いますが、より能動的に何か活動に参加したい方は、是非レジデンス(居住区)まで辿り着いてください。\n\nまずは「<#745860737062273045>」と「<#738358135470817290>」のご確認を。\nワクワクする活動と交流を楽しむロロ〜！')


# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content.in == '/neko':
        await message.channel.send('にゃーん')
    # 「、好奇心王国の憲法」と発言したら「好奇心憲章」が返る処理
    if message.content.in == '憲法':
        await message.channel.send('わんわん')


bot.run(token)
