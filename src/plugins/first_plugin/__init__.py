import nonebot
from nonebot import on_command, logger
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
from . import askjson

sixty = on_command("60s", aliases={"早报", "六十"}, priority=2, block=True)

lovene = on_command("我永远喜欢嘉然小姐", aliases={"嘉然"}, priority=2, block=True)
ultimate_number = on_command("嘉然小姐告诉我宇宙的最终数字", priority=2, block=True)
Reserve = on_command("我要看嘉然小姐", priority=2, block=True)


@Reserve.handle()
async def _(bot: Bot, event: MessageEvent):
    await Reserve.send(
        message=r"关注嘉然 顿顿解馋 https://space.bilibili.com/672328094?from=search&seid=8279194557345987141&spm_id_from=333.337.0.0")


@ultimate_number.handle()
async def _(bot: Bot, event: MessageEvent):
    await ultimate_number.send(message="是42捏")


@lovene.handle()
async def _(bot: Bot, event: MessageEvent):
    await lovene.send(message="可爱捏")


@sixty.handle()
async def _(bot: Bot, event: MessageEvent):
    img_url = (await askjson.get_url())
    if img_url:
        await sixty.send(message=MessageSegment.image(img_url["imageUrl"]))
    else:
        logger.info('获取时出现错误')
