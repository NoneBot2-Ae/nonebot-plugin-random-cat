from pydantic import Extra, BaseSettings


class Config(BaseSettings):
    superusers: list[str]
    enable_groups: list[int]
    proxies_socks5: str

    class Config:
        extra = Extra.ignore
        case_sensitive = False