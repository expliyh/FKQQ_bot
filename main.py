import os
import database
import requests
import sys
import random
import asyncio
import platform
import psutil

if __name__ == '__main__':
    # print("Program started!")
    # database_name = os.environ['database']
    # username = os.environ['username']
    # if username == 'expli':
    #    username = os.environ['database']
    # password = os.environ['password']
    # address = os.environ['address']
    # print("Env finished!")
    # pixiv_name = os.environ['pixiv_username']
    # pixiv_pass = os.environ['pixiv_password']
    # refresh = os.environ['pixiv_refresh']
    # db = database.Database(database_name, username, address, password)
    # print("Db connected!")

    from botoy import *
    from botoy.async_decorators import *
    from botoy.sugar import Text

    bot = AsyncBotoy(
        host=jconfig.host,
        port=jconfig.port,
        log=True,
        # log=False,
        log_file=True,
        use_plugins=True,
    )


    @from_these_groups(760088301)
    @on_regexp(r'\d{17}[\d|x]|\d{15}')
    def undo_id_num(ctx: GroupMsg):
        action1 = Action()
        action1.revoke(ctx)
        S.text("请不要发送含隐私内容的消息！")


    @bot.on_group_msg
    @from_these_groups(760088301, 100867704)
    @equal_content("/sysinfo")
    async def sysinfo(ctx: GroupMsg):
        str1 = "[System Info]\n"
        str1 += "System: "
        str1 += platform.platform()
        str1 += "\nProcessor: "
        str1 += platform.processor()
        str1 += '\nArchitecture: '
        str1 += str(platform.architecture())
        mem = psutil.virtual_memory()
        str1 += "Memory: "
        str1 += str(float(mem.used / 1024 / 1024 / 1024))
        str1 += "/"
        str1 += str(int(mem.total / 1024 / 1024 / 1024))
        str1 += "GB"
        action = AsyncAction(ctx.CurrentQQ)
        await action.replyGroupMsg(
            group=ctx.FromGroupId,
            content=str1,
            msgSeq=ctx.MsgSeq,
            user=ctx.FromUserId,
            rawContent=ctx.Content,
        )
        await action.close()


    @bot.on_group_msg
    @from_these_groups(760088301, 100867704)
    @equal_content("/test")
    def test(ctx: GroupMsg):
        Action(ctx.CurrentQQ).revokeGroupMsg(
            group=ctx.FromGroupId,
            msgSeq=ctx.MsgSeq,
            msgRandom=ctx.MsgRandom,
        )
        S.text("ok")


    asyncio.run(bot.run())
