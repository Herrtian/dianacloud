import nonebot

from nonebot import on_command, logger
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment, Message

voice = on_command("OP", priority=3, block=True)
morning = on_command("早安", priority=3, block=True)
night = on_command("晚安", priority=3, block=True)

@night.handle()
async def _(bot: Bot, event: MessageEvent):
    msg = MessageSegment.record('file:///E:\Source Files\Jetbrains\PyCharm\DianaCloud\diana\media\\night.mp3')

    await night.send(
        message=msg)


@morning.handle()
async def _(bot: Bot, event: MessageEvent):
    msg = MessageSegment.record('file:///E:\Source Files\Jetbrains\PyCharm\DianaCloud\diana\media\morning.mp3')

    await morning.send(
        message=msg)


@voice.handle()
async def _(bot: Bot, event: MessageEvent):
    msg = MessageSegment.record('file:///E:\Source Files\Jetbrains\PyCharm\DianaCloud\diana\media\OP.wav')

    await voice.send(
        message=msg)


