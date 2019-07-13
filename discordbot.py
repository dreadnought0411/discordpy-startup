from discord.ext import commands
import os
import traceback

# command_prefixはコマンドの最初の文字として使うもの。e.g. $ping
bot = commands.Bot(command_prefix='$')

# 実行環境のDISCORD_BOT_TOKENという環境変数からbotのトークンを取得する。今はHerokuにトークンを記入してHerokuで実行してる。
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
