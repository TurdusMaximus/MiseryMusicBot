from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME as BON
from Helpers.Filters import other_filters2
from time import time
from datetime import datetime
from Helpers.Decos import authorized_users_only
from config import BOT_USERNAME, PLAYER_USERNAME

ST = datetime.utcnow()
ST_ISO = ST.replace(microsecond=0).isoformat()
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
        f"""**[🍓](https://telegra.ph/file/b2b2b734b7d7a0b11f58f.jpg)ᴄɪᴀᴏ! {BON} ʜᴇʀᴇ!**
💌•ᴀ ᴘʀᴏɢᴇɴ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ғᴏʀ ᴘʀᴏɢᴇɴ ᴄʜᴀᴛs. \n•🍡ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [xᴇʙᴏʀɴ](T.me/TurdusMaximus).
        """,
        reply_markup=InlineKeyboardMarkup(
            
                [
                  [
                    InlineKeyboardButton(
                       "sᴜᴘᴘᴏʀᴛ", url="https://t.me/MiserySupport"
                    ),
                    InlineKeyboardButton(
                        "ᴍɪsᴇʀʏ ᴏғғɪᴄɪᴀʟ", url="https://t.me/MiSERYOFFiCiAL"
                    )
                ],[
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴍɪsᴇʀʏ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )
