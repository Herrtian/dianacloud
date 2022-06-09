import asyncio

import nonebot
from nonebot import on_command, logger
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment, Message

setu = on_command("来份色图", priority=3, block=True)
setu2 = on_command("我就要看", priority=3, block=True)


@setu.handle()
async def _(bot: Bot, event: MessageEvent):
    msg1 = Message('不要看那些奇奇怪怪的东西 , 看我')
    msg2 = MessageSegment.image('file:///E:\Source Files\Jetbrains\PyCharm\DianaCloud\diana\media\jr.png')
    msg = msg1 + msg2

    await setu.send(
        message=msg)

    await asyncio.sleep(2)

    msg = MessageSegment.record('file:///E:\Source Files\Jetbrains\PyCharm\DianaCloud\diana\media\ssd.mp3')
    await setu.send(
        message=msg)



@setu2.handle()
async def _(bot: Bot, event: MessageEvent):
    msg1 = Message('满意了吗')
    msg2 = MessageSegment.image('file:///E:\Source Files\Jetbrains\PyCharm\DianaCloud\diana\media\setu.png')

    msg = msg1 + msg2

    await setu2.send(
        message=msg)
