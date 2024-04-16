import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6608265446:AAFEghuTU_2nt6UascMnPtgTmd6XWqY5PuE")
    APP_ID = int(os.environ.get("APP_ID", 12606917)
    API_HASH = os.environ.get("API_HASH", "f25113b8c17dca6fa7abda53a86bd4f7")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
