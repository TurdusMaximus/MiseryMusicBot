#Code By INUKA
#Edited By @XeBorn.
#© @MiSERYOFFiCiAl
#2021-2022



import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import SUDO
from Client.callsmusic import client as Peer

@Client.on_message(filters.command(["GeassCast"]))
async def broadcast(_, message: Message):
    sent = 0
    failed = 0
    if message.from_user.id not in SUDO:
        return
    else:
        XnXX = await message.reply("**sᴛᴀʀᴛɪɴɢ ᴍɪsᴇʀʏ ɢᴇᴀssᴄᴀsᴛ!!**")
        if not message.replytomessage:
            await XnXX.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴄᴀsᴛ!")
            return
        Xe = message.replytomessage.text
        async for dialog in Peer.iter_dialogs():
            try:
                await Peer.send_message(dialog.chat.id, Xe)
                sent = sent + 1
                await XnXX.edit(
                    f"ɢᴇᴀssᴄᴀsᴛɪɴɢ... \n\n*sᴍᴇxᴇᴅ ᴛᴏ: {sent} ᴄʜᴀᴛs \n•ғᴀɪʟᴇᴅ ɪɴ: {failed} ᴄʜᴀᴛs"
                )
                await asyncio.sleep(3)
            except:
                failed = failed + 1
                # await wtf.edit(f"broadcasting... \n\nSent to: {sent} Chats \nFailed in:* {failed} Chats")

    await message.reply_text(
        f"ɢᴇᴀssᴄᴀsᴛɪɴɢ...\n\n****•sᴇɴᴛ:**** {sent} ᴄʜᴀᴛs. \n****•ғᴀɪʟᴇᴅ:**** {failed} ᴄʜᴀᴛs**\n © @MiSERYOFFiCiAL 2022"
    )
