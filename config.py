from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
SESSION = getenv("SESSION", "String-Session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
PLAYER_USERNAME = getenv("PLAYER_USERNAME")
OFFICIAL_CHANNEL = getenv("OFFICIAL_CHANNEL", "MiSERYOFFiCiAL")
SUPPORT = getenv("SUPPORT", "MiserySupport")
BOT_USERNAME = getenv("BOT_USERNAME")
PLAYING_PIC = getenv("PLAYING_PIC", "https://te.legra.ph/file/7b4c5c54d192a9d1f4ac3.jpg")
THUMBNAIL_PIC = getenv("THUMBNAIL_PIC", "https://telegra.ph/file/edfa46623756f59a7c531.png")
BOT_PIC = getenv("BOT_PIC", "https://te.legra.ph/file/b7d7910fc1ec434c92242.jpg")
AUDIO_PIC = getenv("AUDIO_PIC", "https://te.legra.ph/file/61eac55d5a627bb372b01.jpg")
QUEUE_PIC = getenv("QUEUE_PIC", "https://telegra.ph/file/f7c6222adf5ba114cca97.jpg")

admemes = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

OWNERID = int(getenv("OWNERID"))

MAXIMUM_DURATION = int(getenv("MAXIMUM_DURATION", "69"))

COMMAND_PANEL = list(getenv("COMMAND_PANEL", "/ !").split())

SUDO = list(map(int, getenv("SUDO").split()))
