import os


class Config(object):
    API_HASH =("b36c5dc986f77eedd4bbf356b65eab19")
    BOT_TOKEN = ("6408919661:AAGorbLd42BMvN93nUL1ehidDkgukGo5XAY")
    TELEGRAM_API = ("21027612")
    OWNER = ("1966867320")
    OWNER_USERNAME = ("Salazar5000")
    PASSWORD = ("iam_roku")
    DATABASE_URL = ("mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = ("-1001560632964")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = ("BABjxmKpuUjsTZywrQaUn9Dbv-K8S3vNsMBkFHtGD3iD5A33Ehyfh2jv_6Ui0yf_UAM6hmiFGpS805QPcYJwU5yCbKOhrPM6lUsAXeacmyqxlhtHRfP_rOGPQWQ_g9tc9RgdRq9L6Y1CJGC9tok0FXYbhbpcrqNX9lPPhaAoUAO-y2X_4kVqdBYvtW7VBuhBbqmf-yxulQRT4O2ZoYEZGKWisp7e4w_3iIHXQrnbe-cjipvUVW3Hk5DFzo1WPw3jrZyxiL00sIQIgycb15CemQI_HuoJCf6IN1OP3pZj89t05Ijh6V0yLH4h2-cs7j2c4dSMRKvRnJ_JJ3LpqBRXoVKkAAAAAS_eymEA")
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
