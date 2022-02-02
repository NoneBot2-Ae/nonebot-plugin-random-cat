# nonebot-plugin-random-cat
- 随机发送猫猫图片
- 随机发送狗狗图片
- 仅支持 NoneBot beta1 以上
- 指定群启用
- 代理使用**SOCKS5**模式

# 安装配置
```
pip install -U nonebot-plugin-random-cat
```

## .env

```ini
SUPERUSERS=<list[str]>

ENABLE_GROUPS=<list[int]>
PROXIES_SOCKS5=<str>
```
- `SUPERUSERS` NoneBot超级管理员
- `ENABLE_GROUPS` 启用群号列表
- `PROXIES_SOCKS5` 代理地址

## bot.py

```
nonebot.load_plugin("nonebot_plugin_random_cat")
```

# 使用

- 指令 `(rcat|来点猫猫)(.*)?`
- 指令 `(rdog|来点狗狗)(.*)?`
- 例子
  - `来点猫猫`
  - `rdog`

# 特别感谢

- [Mrs4s / go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [nonebot / nonebot2](https://github.com/nonebot/nonebot2)
- [kexue-z / nonebot-plugin-setu-now](https://github.com/kexue-z/nonebot-plugin-setu-now)
