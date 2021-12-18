from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice
from pytgcalls.types.input_stream import InputAudioStream
from Misery import callsmusic, queues

import converter
from Youtube import youtube

from config import BOT_NAME as bn, MAXIMUM_DURATION, OFFICIAL_CHANNEL, AUDIO_PIC, QUEUE_PIC, SUPPORT
from Helpers.Filters import command, other_filters
from Helpers.Decos import errors
from Helpers.Errors import DurationLimitError
from Plugs.Get import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ACTV_CALLS = []

@Client.on_message(command("music") & other_filters)
@errors
async def stream(_, message: Message):
    chat_id = message.chat.id


    Xe = await message.reply("🔁 ᴘʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ ᴍᴜsɪᴄ...")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="sᴜᴘᴘᴏʀᴛ",
                        url=f"https://t.me/MISERYSupport"),
                    InlineKeyboardButton(
                        text="ᴏғғɪᴄɪᴀʟ",
                        url=f"https://t.me/{OFFICIAL_CHANNEL}"),
                    
                InlineKeyboardButton(
                        text="x-ᴠᴇʀsɪᴏɴs",
                        url=f"https://t.me/MISERYHOMEBASE")
                    ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > MAXIMUM_DURATION:
            raise DurationLimitError(
                f"ᴍɪsᴇʀʏ ᴄᴀɴɴᴏᴛ ᴘʟᴀʏ sᴏɴɢs ʟᴏɴɢᴇʀ ᴛʜᴀɴ {MAXIMUM_DURATION} ᴍɪɴᴜᴛᴇs!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await Xe.edit_text("! ɢɪᴠᴇ ᴀ ғɪʟᴇ ᴏʀ ʏᴛ ʟɪɴᴋ ᴛᴏ sᴛʀᴇᴀᴍ!")
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))    
    if int(chat_id) in ACTV_CALLS:
        Post = await queues.put(chat_id, file=file_path)
        await message.reply_photo(
        photo=f"{QUEUE_PIC}",
        reply_markup=keyboard,
        caption=f"ʏᴏᴜʀ ʀᴇϙᴜsᴛᴇᴅ ᴍᴏᴏsɪᴄ ɪs ᴀᴅᴅᴇᴅ ᴛᴏ ᴘᴏsɪᴛɪᴏɴ {Post}!\n\n © @MiSERYOFFiCiAL 2022")
        return await Xe.delete()
    else:
        await callsmusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            ) 
        MF = message.from_user.mention
        await message.reply_photo(
        photo=f"{AUDIO_PIC}",
        reply_markup=keyboard,
        caption=f"🎧  ɴᴏᴡ sᴛʀᴇᴀᴍɪɴɢ ʀᴇϙᴜᴇsᴛᴇᴅ sᴏɴɢ ʙʏ  {MF}!\n\n © @MiSERYOFFiCiAL 2022"
        )
        return await Xe.delete()
