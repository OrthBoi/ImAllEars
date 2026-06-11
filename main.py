import os
import asyncio
from dotenv import load_dotenv
import telethon
from telethon import events

load_dotenv(override=True)
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

session_name = "all_ears_session"
keywords = [
    "test", "anotherone"
]

client = telethon.TelegramClient(session_name, API_ID, API_HASH)
print(f"Connection successfull. Session name: {session_name}")


@client.on(events.NewMessage)   
async def handler(event):
    if event.is_private:
         return
    chat = await event.get_chat()
    name = chat.title
    text = event.raw_text.lower()
    textID = event.id
    textDate = event.date
    textOrigin = event.chat_id

    for entries in keywords:
        if entries.lower() in text:
                await client.send_message("me", f"Connection found!\nKeyword: {entries}\nMessage origin: {name}\nMessage ID: {textID}\n Message time: {textDate}\nMessage: {text}")
            
            
        
async def main():
    await client.start()
    await client.send_message("me", "Connection successfull")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())


    