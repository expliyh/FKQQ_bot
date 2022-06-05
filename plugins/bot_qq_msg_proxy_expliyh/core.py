from botoy import GroupMsg
from botoy.parser import group as gp
import requests
import base64

def say_hello(name):
    return f"Hello, {name}!"


def download(url: str):
    r = requests.get(url)
    with open('./image/img2.png', 'wb+') as f:
        f.write(r.content)
    pic_bs64 = base64.b64encode(r.content)  # 图片Base64
    return pic_bs64


def resolve_group_pic(ctx: GroupMsg):
    pic_data = gp.pic(ctx)
    if pic_data is not None:
        for pic in pic_data.GroupPic:
            return str(download(pic.Url), encoding='utf-8')


