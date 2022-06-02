"""插件帮助信息"""
from botoy import Action, GroupMsg, S
from botoy import decorators as deco
from botoy.contrib import plugin_receiver

try:
    # 如果需要用到单独插件测试运行，请这样处理项目中所有的导入操作
    from .core import say_hello
    from .core import resolve_group_pic
except ImportError:
    from core import say_hello
    from core import resolve_group_pic

to_group = 100867704


@plugin_receiver.group
@deco.from_these_groups(558995206, 760088301)
@deco.from_these_users(277319875, 9786177)
@deco.ignore_botself
def msg_proxy(ctx: GroupMsg):
    action = Action(qq=ctx.CurrentQQ)
    action.sendGroupText(group=to_group, content="转发来自辅导员或测试人员的消息：")
    if ctx.MsgType == 'TextMsg':
        action.sendGroupText(group=to_group, content=ctx.Content)
    elif ctx.MsgType == 'PicMsg':
        b644 = resolve_group_pic(ctx)
        action.sendGroupPic(group=to_group, picBase64Buf=b644, content='')
