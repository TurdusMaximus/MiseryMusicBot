import asyncio
from pyrogram import Client
print("Enter Your Telegram-API Information.")
async def main():
    async with Client(":memory:", API_ID=int(input("•API ID:")), API_HASH=input("•API HASH:")) as bot:
        print(await bot.export_session_string())

#©Copyright To @XeBorn (2021-2022).
