import httpx
from typing import Optional
from nonebot import logger


async def get_url() -> Optional[str]:
    """
    :return: 早报图片链接
    """
    url="https://api.iyk0.com/60s"
    async with httpx.AsyncClient() as client:
        r = (await client.get(url=url)).json()
        return r