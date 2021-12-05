from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME as BON
from helpers.filters import other_filters2
from time import time
from datetime import datetime
from Helpers.Decos import authorized_users_only
from config import BOT_USERNAME, PLAYER_USERNAME

ST = datetime.utcnow()
ST_ISO = START_TIME.replace(microsecond=0).isoformat()
DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**🍓Ciao! {BON} Here!**
💌•I Am A Program Telegram Voice Chat Music Player. Developed and Maintained By [XeBorn](T.me/TurdusMaximus).
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [   #Have To Fill Command Panel
                    InlineKeyboardButton(
                        "Command Panel", url="")
                  ],[
                    InlineKeyboardButton(
                       "Support", url="https://t.me/MiserySupport"
                    ),
                    InlineKeyboardButton(
                        "Updates", url="https://t.me/MiSERYOFFiCiAL"
                    )
                ],[
                    InlineKeyboardButton(
                        "Add Me In Your Group",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
