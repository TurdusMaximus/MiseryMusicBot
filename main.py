import requests
from pytgcalls import idle
from pyrogram import Client as Misery

from Client.callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

response = requests.get(PLAYING_PIC)
with open("./Trash/MiseryXnXX.png", "wb") as f:
    f.write(response.content)


Moosic = Misery(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

Moosic.start()
run()
idle()
