from discord.ext import commands
import os
import traceback
import re

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


# コマンドに対応するリストデータを取得する関数を定義
async def get_data(message):
    command = message.content
    data_table = {
        '/members': message.guild.members, # メンバーのリスト
        '/roles': message.guild.roles, # 役職のリスト
        '/text_channels': message.guild.text_channels, # テキストチャンネルのリスト
        '/voice_channels': message.guild.voice_channels, # ボイスチャンネルのリスト
        '/category_channels': message.guild.categories, # カテゴリチャンネルのリスト
    }
    return data_table.get(command, '無効なコマンドです')



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
    await channel1.send(str(member.mention)+'さん！好奇心王国へようこそ！\n好奇心AIの「ロロたん」です。\nここにたどり着いたということは、きっとあなたは好奇心の旺盛な方ですね！\n\n好奇心王国は、「好奇心」「個性」「子供心」が混じり合う場所。\n一人ひとりの興味や関心が交流へと繋がるよう設計されています。\n軸となる活動は『テクノロジーの使い方のアイデア発想と、それを実装する”プロジェクト”』。これは招待制のレジデンスエリア(居住区)で行われます。\n\nOPENエリア(観光エリア)でも交流を楽しめるチャンネルがありますよ。\nまずは「<#745860737062273045>」と「<#738358135470817290>」のご確認を。\nワクワクする活動と交流を楽しむロロ♪')

# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):
    guild = message.guild
    role = guild.get_role(738998001976082503)#レジデンスのロールID

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    # 「王国のルール」が返る処理
    if re.search("入国する際の「注意事項」", message.content):
        await message.channel.send('好奇心王国への入国にあたり、\n下記を守ることを約束して欲しいロロ！\n\n－－－－好奇心憲章－－－－\n♪自分の好奇心を信じよう\n♪相手の好奇心を尊重しよう\n♪変なことも、一度受け入れて面白がろう\n♪ロジハラ、知識マウント、常識の強要はNG\n♪子供心を大切に、くだらなさを楽しもう\n♪「はじめまして」を大切にしよう\n♪くすぐったくても褒め合いましょう\n－－－－－－－－－－－－－\n\n何より大切なのは、一人ひとりの\n興味やこだわり、そして何でも\n能動的に面白がる気持ちだロロ〜')
    if re.search("プロジェクトってどんな風にスタートするの？", message.content):
        await message.channel.send('それは「このアイデアを形にしてみたい」と\n誰かがリーダーに名乗り出て始まるロロ。\n\nそしてプロジェクトリーダーにはこんな心構えを持っていて欲しいロロ！\n\n－－－－－－－－－－－－－\n♪「好奇心ドリブン」で始めてみよう\n♪目的はビジネス/アート/趣味、何でもOK\n♪多数決じゃなくリーダーが決定しよう\n♪メンバーをリスペクトしよう\n♪アイデアを出した人や貢献者には何か還元を\n♪もし失敗しても「ネタになる」と思おう\n♪少しの責任と覚悟を持とう\n－－－－－－－－－－－－－')
    if re.search("好奇心王国の未来像を教えて", message.content):
        await message.channel.send('わんわん')

    if re.search("ロロたんとワクワクの冒険", message.content): #もし、こんにちはを含むメッセージで、
        if message.channel.id == 746579828693794926:#かつ、もし、神社チャンネルなら
            await message.author.add_roles(role)
        else:#あるいは、もし神社チャンネルでないなら
            await message.channel.send("ここではコマンドは実施できません") 

    if message.channel.id == 746579828693794926:#神社チャンネルのメッセージは基本的に全て削除
        await message.delete()

bot.run(token)
