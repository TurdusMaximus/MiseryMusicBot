import json
import logging

from Helpers.Filters import command 
from pyrogram import Client
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from youtube_search import YoutubeSearch

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
Logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(command(["search", f"yts"]))
async def ytsearch(_, message: Message):
    
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "ᴄʟᴏsᴇ", callback_data="close",
               
                )
                InlineKeyboardButton("ᴍɪsᴇʀʏ ᴏғғɪᴄɪᴀʟ" , url="T.me/MiSERYOFFiCiAL"

)
            ]
        ]
    )
    
    try:
        if len(message.command) < 2:
            await message.reply_text("/search ɴᴇᴇᴅs ᴀɴ ᴀʀɢᴜᴍᴇɴᴛ!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("sᴇᴀʀᴄʜɪɴɢ....")
        results = YoutubeSearch(query, max_results=5).to_dict()
        Moosic = ""
        for i in range(5):
            Moosic += f"•ᴛɪᴛʟᴇ - {results[i]['title']}\n"
            Moosic += f"•ᴅᴜʀᴀᴛɪᴏɴ - {results[i]['duration']}\n"
            Moosic += f"•ᴠɪᴇᴡs - {results[i]['views']}\n"
            Moosic += f"•ᴄʜᴀɴɴᴇʟ - {results[i]['channel']}\n"
            Moosic += f"https://youtube.com{results[i]['url_suffix']}\n\n"
        await m.edit(Moosic, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
