import random
from re import I

import nonebot
from nonebot import on_command, on_regex, get_driver, require
from nonebot.adapters.onebot.v11 import (Bot, Event, Message,
                                         PrivateMessageEvent,
                                         GroupMessageEvent)
from nonebot.adapters.onebot.v11.permission import GROUP, PRIVATE_FRIEND
from nonebot.log import logger
from nonebot.typing import T_State
from nonebot.params import State
from .get_data import get_cat, get_dog
from .config import Config

global_config = get_driver().config
config: Config = Config.parse_obj(global_config.dict())
scheduler = require("nonebot_plugin_apscheduler").scheduler

rcat = on_regex(
    r"^(rcat|来点猫猫)(.*)?",
    flags=I,
    permission=PRIVATE_FRIEND | GROUP,
)


@rcat.handle()
async def rcat_handle(bot: Bot, event: Event, state: T_State = State()):
    if isinstance(
            event,
            GroupMessageEvent) and event.group_id not in config.enable_groups:
        return

    pic = await get_cat()
    if pic[0]:
        try:
            await rcat.send(message=Message(pic[2]))
            await rcat.send(
                message=Message("猫猫来啦"),
                at_sender=True,
            )
        except Exception as e:
            logger.warning(e)
            await rcat.finish(
                message=Message(f"消息被风控，图发不出来\n{pic[1]}\n这是链接\n{pic[3]}"),
                at_sender=True,
            )

    else:
        await rcat.finish(f"出错：{pic[1]}")


@scheduler.scheduled_job("cron", hour="9", args=['早间猫猫！'])
@scheduler.scheduled_job("cron", hour="12", args=['午间猫猫！'])
@scheduler.scheduled_job("cron", hour="18", args=['晚间猫猫！'])
async def rcat_task(text):
    pic = await get_cat()
    if pic[0]:
        try:
            for group_id in config.enable_groups:
                await nonebot.get_bot().send_group_msg(
                    group_id=group_id, message=f"{text}\n{pic[2]}")
        except Exception as e:
            logger.warning(e)


rdog = on_regex(
    r"^(rdog|来点狗狗)(.*)?",
    flags=I,
    permission=PRIVATE_FRIEND | GROUP,
)


@rdog.handle()
async def rdog_handle(bot: Bot, event: Event, state: T_State = State()):
    if isinstance(
            event,
            GroupMessageEvent) and event.group_id not in config.enable_groups:
        return

    pic = await get_dog()
    if pic[0]:
        try:
            await rcat.send(message=Message(pic[2]))
            await rcat.send(
                message=Message("狗狗来啦"),
                at_sender=True,
            )
        except Exception as e:
            logger.warning(e)
            await rcat.finish(
                message=Message(f"消息被风控，图发不出来\n{pic[1]}\n这是链接\n{pic[3]}"),
                at_sender=True,
            )

    else:
        await rcat.finish(f"出错：{pic[1]}")