import asyncio

from nonebot import on_command, logger
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment, Message

course = on_command("课表", priority=3, block=True)
code = on_command("cdr", priority=3, block=True)

@code.handle()
async def _(bot: Bot, event: MessageEvent):

    await asyncio.sleep(3)
    msg = '主人, 你今天一共写了 \n' \
          '79 行代码 \n ' \
          '真的好弱嗷'

    await code.send(
        message=msg)

    msg = MessageSegment.image('file:///E:\Source Files\Jetbrains\PyCharm\DianaCloud\diana\media\laugh.png')

    await code.send(
        message=msg)


@course.handle()
async def _(bot: Bot, event: MessageEvent):

    await asyncio.sleep(3)
    msg = '今天是星期二 \n' \
          '主人你今天有 \n' \
          'Web工程[01] @B-532'

    await course.send(
        message=msg)
