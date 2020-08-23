from discord.ext import commands
import os
import traceback
import re

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']




@bot.event
async def on_error(ctx, error):
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
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    # 「王国のルール」が返る処理
    if re.search("好奇心王国の憲法を教えて", message.content):
        await message.channel.send('はい！好奇心王国への入国にあたり、\n下記を守ることを約束して欲しいロロ！\n\n－－－－好奇心憲章－－－－\n♪自分の好奇心を信じよう\n♪相手の好奇心を尊重しよう\n♪変なことも、一度受け入れて面白がろう\n♪ロジハラ、知識マウント、常識の強要はNG\n♪子供心を大切に、くだらなさを楽しもう\n♪「はじめまして」を大切にしよう\n♪くすぐったくても褒め合いましょう\n－－－－－－－－－－－－－\n\n    何より大切なのは、一人ひとりの\n興味やこだわり、そして何でも\n能動的に面白がる気持ちだロロ〜')
    if re.search("プロジェクト立ち上げのルールってある", message.content):
        await message.channel.send('はい！前提としてはレジデンス(居住区)の活動となるけど、\nプロジェクトリーダーにはこんな心構えを持っていて欲しいロロ！\n\n－－－－－－－－－－－－－\n♪「好奇心ドリブン」で始めてみよう\n♪目的はビジネス/アート/趣味、何でもOK\n♪多数決じゃなくリーダーが決定しよう\n♪メンバーをリスペクトしよう\n♪アイデアを出した人や貢献者には何か還元を\n♪もし失敗しても「ネタになる」と思おう\n♪少しの責任と覚悟を持とう\n－－－－－－－－－－－－－')
    if re.search("好奇心王国の未来像を教えて", message.content):
        await message.channel.send('わんわん')


    if re.search("こんにちは", message.content): #もし、こんにちはを含むメッセージで、
        if message.channel.id == 746579828693794926:#かつ、もし、神社チャンネルなら
            guild = bot.get_guild()
            member = bot.get_member()
            role = bot.get_role(738998001976082503)#レジデンスのロール
                await member.add_roles(role)  
                await message.channel.send("Good afternoon")
        else:
            await message.channel.send("ここではコマンドは実施できません") #あるいは、もし神社チャンネルでないなら


bot.run(token)
