from os import path

from yt_dlp import YoutubeDL as Yt

from config import MAXIMUM_DURATION
from Helpers.Errors import DurationLimitError


ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
Xe = Yt(ydl_opts)


def download(url: str) -> str:
    info = Xe.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > MAXIMUM_DURATION:
        raise DurationLimitError(
            f"❌ • ɪ ᴄᴀɴɴᴏᴛ ᴘʟᴀʏ ᴠɪᴅᴇᴏs ʟᴏɴɢᴇʀ ᴛʜᴀɴ {MAXIMUM_DURATION} ᴍɪɴᴜᴛᴇs, ᴘʀᴏᴠɪᴅᴇᴅ ᴠɪᴅᴇᴏ ɪs {duration} ᴍɪɴᴜᴛᴇs"
        )

    Xe.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
