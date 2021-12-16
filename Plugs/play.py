#© @XeBorn Wholly Edited Basic Code.
import os
from os import path
from typing import Callable
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from Misery import callsmusic , queues

from Misery.callsmusic import client as Peer
from Helpers.admeme import get_administrators
import requests
import aiohttp
import yt_dlp
from youtube_search import YoutubeSearch
import converter
from Youtube import youtube
from config import MAXIMUM_DURATION, que, SUDO , PLAYER_USERNAME
from xD.admeme import admins as a
from Helpers.Filters import command
from Helpers.Decos import errors, authorized_users_only
from Helpers.Errors import DurationLimitError
from Plugs.Get import get_url, get_file_name
from Helpers.ChannelMoosic import get_chat_id
import aiofiles
import ffmpeg
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream

# Also Bamby
chat_id = None
DISABLED_GROUPS = []
useer = "NaN"
ACTV_CALLS = []


def cb_admin_check(func: Callable) -> Callable:
    async def decorator(client, cb):
        admemes = a.get(cb.message.chat.id)
        if cb.from_user.id in admemes or cb.from_user.id in SUDO:
            return await func(client, cb)
        await cb.answer("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅᴏ ᴛʜᴀᴛ!", show_alert=True)
        return

    return decorator


def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(filename)


# Converting seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Converting hh:mm:ss to seconds.
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


# Image Function (Old one)
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    return image.resize((newWidth, newHeight))


async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open("Trash/MiseryXnXX.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("XeFuck.png")
    img = Image.open("XeFuck.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Trash/MiseryJuly.otf", 32)
    draw.text((200, 554), f"Somng: {title}", (269, 269, 269), font=font)
    draw.text((200, 554), f"Length: {duration}", (269, 269, 269), font=font)
    draw.text((200, 645), f"Views: {views}", (269, 269, 269), font=font)
    draw.text(
        (190, 670),
        f"Req By: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("Senkuu.png")
    os.remove("XeFuck.png")
    os.remove("background.png")


@Client.on_message(
    command("Geass") & ~filters.edited & ~filters.bot & ~filters.private
)
@authorized_users_only
async def hfmm(_, message):
    global DISABLED_GROUPS
    try:
        user_id = message.from_user.id
    except:
        return
    if len(message.command) != 2:
        await message.reply_text(
            "ɪ ᴏɴʟʏ ᴋɴᴏᴡ `/Geass ACT` and `/Geass DCT` "
        )
        return
    status = message.text.split(None, 1)[1]
    message.chat.id
    if status in ["DCT", "Dct", "dct" , "DcT"]:
        lel = await message.reply("`ᴘʀᴏᴄᴇssɪɴɢ...`")
        if message.chat.id not in DISABLED_GROUPS:
            await lel.edit("This Chat is not In maintainence mode")
            return
        DISABLED_GROUPS.remove(message.chat.id)
        await lel.edit(
            f"ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ ᴍᴏᴅᴇ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ɪɴ **{message.chat.title}**"
        )

    elif status in ["ACR", "Act", "act"]:
        lel = await message.reply("`ᴘʀᴏᴄᴇssɪɴɢ ɪᴛ!`")

        if message.chat.id in DISABLED_GROUPS:
            await lel.edit("ᴍᴀɪɴᴛᴀɪɴᴇɴᴄᴇ ᴍᴏᴅᴇ ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ!")
            return
        DISABLED_GROUPS.append(message.chat.id)
        await lel.edit(
            f"✅ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ ᴍᴏᴅᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ɪɴ **{message.chat.title}**"
        )
    else:
        await message.reply_text(
            "ɪ ᴏɴʟʏ ᴋɴᴏᴡ `/Geass ACT` ~ `/Geass DCT` "
        )


@Client.on_callback_query(filters.regex(pattern=r"^(cls)$"))
@cb_admin_check
@authorized_users_only
async def m_cb(b, cb):
    global que
    qeue = que.get(cb.message.chat.id)
    type_ = cb.matches[0].group(1)
    chat_id = cb.message.chat.id
    m_chat = cb.message.chat

    if type_ == "cls":
        await cb.answer("Closed menu")
        await cb.message.delete()


# Somg Play-Func - Emdited By © @XeBorn
@Client.on_message(
    command("play")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    chat_id = message.chat.id
    global que
    global useer
    if message.chat.id in DISABLED_GROUPS:
        await message.reply("**ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ ᴍᴏᴅᴇ! , ᴀsᴋ ᴀᴅᴍɪɴ ᴛᴏ ᴅɪsᴀʙʟᴇ**")
        return
    lel = await message.reply("🔄 **ᴘʀᴏᴄᴇssɪɴɢ...**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await Peer.get_me()
    except:
        user.first_name = "MiseryMusicPlayer"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                await lel.edit(
                    "ᴅᴏɴ'ᴛ ғᴏʀɢᴇᴛ ᴛᴏ ᴄᴀʟʟ ᴛʜᴇ ᴘʟᴀʏᴇʀ ʜᴇʀᴇ",
                )
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ғɪʀsᴛ!",
                    )
                    return

                try:
                    await Peer.join_chat(invitelink)
                    await Peer.send_message(
                        message.chat.id,
                        "✅ ᴍɪsᴇʀʏ ᴘʟᴀʏᴇʀ ʜᴇʀᴇ!",
                    )
                    await lel.edit(
                        "✅ ᴍɪsᴇʀʏ-ᴘʟᴀʏᴇʀ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴄʜᴀᴛ",
                    )

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"ғʟᴏᴏᴅ-ᴡᴀɪᴛ ᴇʀʀᴏʀ \n •ʜᴏʟᴀ {user.first_name}, ᴍɪsᴇʀʏ ᴘʟᴀʏᴇʀ ᴄᴀɴɴᴏᴛ ᴊᴏɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ!"
                    )
    try:
        await Peer.get_chat(chid)
        # lmoa = await client.get_chat_member(chid,wew)
    except:
        await lel.edit(
            f"ᴄɪᴀᴏ! {user.first_name}, {PLAYER_USERNAME} ɪs ɴᴏᴛ ɪɴ ᴄʜᴀᴛ.\n\n •ᴀsᴋ ᴀɴʏ ᴀᴅᴍᴇᴍᴇ ᴛᴏ sᴇɴᴅ /play ᴄᴍᴅ ғᴏʀ ғɪʀsᴛ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ɪᴛ!"
                    )
        
        return

    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > MAXIMUM_DURATION:
            raise DurationLimitError(
                f"❌ •ɪ ᴄᴀɴɴᴏᴛ ᴘʟᴀʏ sᴏɴɢs ʟᴏɴɢᴇʀ ᴛʜᴀɴ {MAXIMUM_DURATION} ᴍɪɴᴜᴛᴇs!"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/57e3495d7c0307018b640.png"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="t.me/MISERYSUPPORT"),
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="t.me/MISERYOFFICIAL"),
                    InlineKeyboardButton("x-ᴠᴇʀsɪᴏɴs", url="t.me/MISERYHOMEBASE"),
                ],
                [InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="cls")],
            ]
        )

        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="t.me/MISERYSUPPORT"),
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="t.me/MISERYOFFICIAL"),
                    ],
                    [InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="cls")],
                ]
            )

        except Exception as e:
            title = "NaN"
            thumb_name = "https://telegra.ph/file/57e3495d7c0307018b640.png"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="YouTube 🎬", url="https://youtube.com")]]
            )

        if (dur / 60) > MAXIMUM_DURATION:
            await lel.edit(
                f"❌ ɪ ᴄᴀɴɴᴏᴛ ᴘʟᴀʏ ᴛʜᴇ sᴏɴɢs ʟᴏɴɢᴇʀ ᴛʜᴀɴ {MAXIMUM_DURATION} ᴍɪɴᴜᴛᴇs!"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit(
                " **ᴄᴀɴɴᴏᴛ ғɪɴᴅ ᴛʜᴇ sᴏɴɢ. sᴘᴇʟʟ ɪᴛ ᴘʀᴏᴘᴇʀʟʏ!\n•ɪ.ᴇ - • /Play JOKER BGM \n\n  ® @MISERYOFFICIAL 21-22**"
            )
        await lel.edit("🔎 **ғɪɴᴅɪɴɢ...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        await lel.edit("🎵 **•ᴘʀᴏᴄᴇssɪɴɢ...**")
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "❌ •ᴄᴀɴɴᴏᴛ ғɪɴᴅ ᴛʜᴇ sᴏɴɢ.\n\n•sᴘᴇʟʟ ɪᴛ ᴘʀᴏᴘᴇʀʟʏ!."
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="t.me/MISERYSUPPORT"),
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="t.me/MISERYOFFICIAL"),
                ],
                [InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="cls")],
            ]
        )

        if (dur / 60) > MAXIMUM_DURATION:
            await lel.edit(
                f"❌ ᴠɪᴅᴇᴏs ʟᴏɴɢᴇʀ ᴛʜᴀɴ {MAXIMUM_DURATION} ᴍɪɴᴜᴛᴇs ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴘʟᴀʏ!"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_photo(
            photo="Senkuu.png",
            caption="**•sᴏɴɢ:** {}\n**•ᴅᴜʀᴀᴛɪᴏɴ:** {} min\n**•ϙᴜᴇᴜᴇᴅ ʙʏ:** {}\n\n**•ϙᴜᴇᴜᴇᴅ ᴘᴏsɪᴛɪᴏɴ:** {}".format(
                title,
                duration,
                message.from_user.mention(),
                position,
            ),
            reply_markup=keyboard,
        )
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
        await message.reply_photo(
            photo="Senkuu.png",
            reply_markup=keyboard,
            caption="**•sᴏɴɢ:** {}\n**•ᴅᴜʀᴀᴛɪᴏɴ:** {} ᴍɪɴᴜᴛᴇs\n**•ϙᴜᴇᴜᴇᴅ ʙʏ:** {}\n\n**•ᴘʟᴀʏɪɴɢ ᴀᴛ `{}`**".format(
                title, duration, message.from_user.mention(), message.chat.title
            ),
        )

    os.remove("Senkuu.png")
    return await lel.delete()
