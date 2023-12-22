import os


class Config(object):
    API_HASH =("b36c5dc986f77eedd4bbf356b65eab19")
    BOT_TOKEN = ("6702684341:AAFqjTr8dw4UJsie1Kk_-UqC0Ao87UaEKJs")
    TELEGRAM_API = ("21027612")
    OWNER = ("5098097249")
    OWNER_USERNAME = ("Salazar5000")
    PASSWORD = ("iam_roku")
    DATABASE_URL = ("mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = ("-1001621207300")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = ("")
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
