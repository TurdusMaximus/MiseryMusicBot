from typing import List
from pyrogram.types import Chat, User
from xD.admeme import get as Goat
from xD.admeme import set
#Cache as xD

async def get_administrators(chat: Chat) -> List[User]:
    get = Goat(chat.id)

    if get:
        return get
    administrators = await chat.get_members(filter="administrators")
    to_set = [administrator.user.id for administrator in administrators]

    set(chat.id, to_set)
    return await get_administrators(chat)
#©Xeborn
