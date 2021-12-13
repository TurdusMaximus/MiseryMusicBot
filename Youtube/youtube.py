from os import path

from yt_dlp import YoutubeDL

from config import MAXIMUM_DURATION
from helpers.errors import DurationLimitError


ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > MAXIMUM_DURATION:
        raise DurationLimitError(
            f"❌ ɪ ᴄᴀɴɴᴏᴛ sᴛʀᴇᴀᴍ ᴠɪᴅᴇᴏs ʟᴏɴɢᴇʀ ᴛʜᴀɴ {MAXIMUM_DURATION} ᴍɪɴᴜᴛᴇᴅ, ᴘʀᴏᴠɪᴅᴇᴅ ᴠɪᴅᴇᴏ ɪs {duration} ᴍɪɴᴜᴛᴇs"
        )

    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
