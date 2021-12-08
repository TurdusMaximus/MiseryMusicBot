from Plugins import check_heroku
from Helpers.Filters import command
from pyrogram import Client, filters
from pyrogram import Client, filters
from Helpers.Decos import sudo_users_only
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery


@Client.on_message(command(["restart", "reboot"]) & ~filters.edited)
@sudo_users_only
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_photo(
        photo="https://te.legra.ph/file/7f4d440ac9b8240ac13ac.jpg", 
        caption="***ʀᴇsᴛᴀʀᴛɪɴɢ...*\n**ᴡᴀɪᴛ ᴘʟᴏx...**"
    )
    hap.restart()
