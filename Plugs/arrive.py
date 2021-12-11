# ©XeBorn
#Base Code By DaisyX
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from Helpers.Decos import authorized_users_only, errors
from Client.callsmusic import client as Peer
from config import SUDO


@Client.on_message(filters.command(["playerjoin", "join"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "ᴀᴅᴅ ᴍɪsᴇʀʏ ᴀs ᴀᴅᴍɪɴ ғɪʀsᴛ.",
        )
        return

    try:
        user = await Peer.get_me()
    except:
        user.first_name = "@MiseryMusicPlayer"

    try:
        await Peer.join_chat(invitelink)
    except UserAlreadyParticipant:
        await message.reply_text(
            f"{user.first_name}  ɪs ᴀʟʀᴇᴀᴅʏ ʜᴇʀᴇ!</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"ғʟᴏᴏᴅ-ᴡᴀɪᴛ ᴇʀʀᴏʀ!\n • {user.first_name} ᴍɪsᴇʀʏ ᴄᴀɴɴᴏᴛ ᴊᴏɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ ᴅᴜᴇ ᴛᴏ ʜᴇᴀᴠʏ ʀᴇϙᴜᴇsᴛs\n ᴏʀ ᴍᴀʏʙᴇ ɪ ᴀᴍ ʙᴀɴɴᴇᴅ!?."
            "\n\n © @MiSERYOFFiCiAL 21-22.",
        )
        return
    await message.reply_text(
        f"✅{user.first_name} ᴊᴏɪɴᴇᴅ sᴜᴄᴋsᴇxғᴜʟʟʏ!",
    )


@Peer.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(Peer,):
    try:
        await Peer.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "• ɪ ᴛʜɪɴᴋ ɪ ᴄᴀɴɴᴏᴛ ʟᴇᴀᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ ᴅᴜᴇ ᴛᴏ ғʟᴏᴏᴅ-ᴡᴀɪᴛs , ᴋɪᴄᴋ ᴍᴇ ᴍᴀɴᴜᴀʟʟʏ!</b>"
        )

        return


@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id not in SUDO:
        return

    left = 0
    failed = 0
    lol = await message.reply("**ᴍɪsᴇʀʏ ɪs ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs**")
    async for dialog in Peer.iter_dialogs():
        try:
            await Peer.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"ᴍɪsᴇʀʏ ɪs ʟᴇᴀᴠɪɴɢ •ʟᴇғᴛ: {left} ᴄʜᴀᴛs. •ғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
            )
        except:
            failed += 1
            await lol.edit(
                f"ᴍɪsᴇʀʏ ɪs ʟᴇᴀᴠɪɴɢ •ʟᴇғᴛ: {left} ᴄʜᴀᴛs. •ғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"•ʟᴇғᴛ {left} ᴄʜᴀᴛs. •ғᴀɪʟᴇᴅ {failed} ᴄʜᴀᴛs."
    )
