import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7115403757:AAHyzfrieb-faOXDW5lxSdQjM-NKHp9uULg")
    APP_ID = int(os.environ.get("APP_ID", 23163380)
    API_HASH = os.environ.get("API_HASH", "2dca155e786c7db2d295e5b4ab10783b")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
