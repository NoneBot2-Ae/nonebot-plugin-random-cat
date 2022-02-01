import base64
from re import findall
from sys import exc_info
import httpx
from httpx import AsyncClient
from httpx_socks import AsyncProxyTransport
from nonebot import logger, get_driver
from .config import Config

global_config = get_driver().config
config: Config = Config.parse_obj(global_config.dict())
transport = AsyncProxyTransport.from_url(config.proxies_socks5)


async def get_cat():
    try:
        async with AsyncClient(transport=transport) as client:
            req_url = "https://aws.random.cat/meow"
            try:
                res = await client.get(req_url, timeout=120)
                logger.info(res.json())
            except httpx.HTTPError as e:
                logger.warning(e)
                return [False, f"API异常 {e}", '', '']
            try:
                img_url = res.json()['file']
                content = await down_pic(img_url)
                base64 = convert_b64(content)
                if type(base64) == str:
                    pic = "[CQ:image,file=base64://" + base64 + "]"
                return [True, '', pic, img_url]
            except:
                logger.warning(f"{exc_info()[0]}, {exc_info()[1]}")
                return [False, f"{exc_info()[0]} {exc_info()[1]}。", '', '']
    except httpx.ProxyError as e:
        logger.warning(e)
        return [False, f"代理错误: {e}", '', '']


async def get_dog():
    try:
        async with AsyncClient(transport=transport) as client:
            req_url = "https://random.dog/woof.json"
            try:
                res = await client.get(req_url, timeout=120)
                while str(res.json()).find('.mp4') != -1:
                    res = await client.get(req_url, timeout=120)
                logger.info(res.json())
            except httpx.HTTPError as e:
                logger.warning(e)
                return [False, f"API异常 {e}", '', '']
            try:
                img_url = res.json()['url']
                content = await down_pic(img_url)
                base64 = convert_b64(content)
                if type(base64) == str:
                    pic = "[CQ:image,file=base64://" + base64 + "]"
                return [True, '', pic, img_url]
            except:
                logger.warning(f"{exc_info()[0]}, {exc_info()[1]}")
                return [False, f"{exc_info()[0]} {exc_info()[1]}。", '', '']
    except httpx.ProxyError as e:
        logger.warning(e)
        return [False, f"代理错误: {e}", '', '']


async def down_pic(url):
    async with AsyncClient(transport=transport) as client:
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        }
        re = await client.get(url=url, headers=headers, timeout=120)
        if re.status_code == 200:
            logger.success("成功获取图片")
            return re.content
        else:
            logger.error(f"获取图片失败: {re.status_code}")
            return re.status_code


def convert_b64(content) -> str:
    ba = str(base64.b64encode(content))
    pic = findall(r"\'([^\"]*)\'", ba)[0].replace("'", "")
    return pic