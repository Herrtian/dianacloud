import asyncio
import re

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment, escape

moyu = on_command('moyu', aliases={'摸鱼'})


@moyu.handle()
async def _handle(matcher: Matcher, city: Message = CommandArg()):
    if city.extract_plain_text() and city.extract_plain_text()[0] != '_':
        matcher.set_arg('min', city)


@moyu.got('min', prompt='主人想摸多久捏？')
async def _(city: str = ArgPlainText('min')):
    await asyncio.sleep(int(city))
    await moyu.send("主人快去学习，不许再摸鱼了")

