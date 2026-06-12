import os
import asyncio
from dotenv import load_dotenv
import telethon
from telethon import events
import datetime

load_dotenv(override=True)
#Be sure to create a .env file and add your API ID & HASH there.
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
wantsHistorySearch = False

#CUSTOM - Add your keywords here, you can also change the session name which is purely cosmetic
session_name = "all_ears"
keywords = [
    "your keywords seperated by a , each"
]

client = telethon.TelegramClient(session_name, API_ID, API_HASH)
print(f"Connection successfull. Session name: {session_name}")
while True:
    try:
        answer = input("Do you want to scan past messages up to a certain date? [y][n]").lower()
        if answer == "n" or answer == "no":
            break
        answerDate = input("\nPlease enter the date up to which you want to scan messages for. Please make sure to strictly use the following format: day,month,year: ")    
        d, m, y = map(int, answerDate.replace(" ", "").split(","))
        targetDate = datetime.date(y, m, d)
        currentDate = datetime.date.today()
        print(targetDate)
        print(currentDate)
        if currentDate > targetDate:
             print("Date has NOT passed")
        else:
             print("Date has passed")
    except Exception as e:
         print("Error", e)



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


    
