import os


class Config(object):
    API_HASH =("108df940118cde6c5f524f4d439a19d3")
    BOT_TOKEN = ("7057424985:AAHg9VPGpVrVS_-oeSTCOz50R5CJRvsLgD8")
    TELEGRAM_API = ("26545740")
    OWNER = ("6820572640")
    OWNER_USERNAME = ("None")
    PASSWORD = ("mysterydemon")
    DATABASE_URL = ("mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = ("-1001560632964")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = True
    START_PIC = ("https://telegra.ph/file/bb0690bfacfdc008ff788.jpg")
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
