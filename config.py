import os


class Config(object):
    API_HASH =("b36c5dc986f77eedd4bbf356b65eab19")
    BOT_TOKEN = ("6926658380:AAEpfUlnnYwUVA-J2QsBuFxhL4v46VKISKE")
    TELEGRAM_API = ("21027612")
    OWNER = ("5098097249")
    OWNER_USERNAME = ("Salazar5000")
    PASSWORD = ("iam_roku")
    DATABASE_URL = ("mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = ("-1001621207300")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = ("BAHHO64AHHWBWQBH6vuhTTbrUBRzQX9oMonfyjflQV6tcGcPIJzvQTe21pa_85kWZteBsFzUwaMlVSMAabJ7mefSKf_tnyF6Rj9wkgzt9apibMpipIVxlzgU32G7YbK1-8xTep9w8ItMckqbxFihjN3R6B0mSEw7zk2vTXDR5QiNMGB-uyiehF5UTcQYI8vFFNjSPSHebunljTj7W3Yj7kbX6rnQ7zuOEHk_e67717WA7FmhX94mnAORG-0bCEovYukIQb6IgPj-9bZRnDQvm4hAab4c0Tmd_P7UgZy81jaVacsw1zk9FLpTUKhTFpPgU0w2uRL-C1p2ikHe-kjkPOTuLfEPggAAAAEv3sphAA")
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
