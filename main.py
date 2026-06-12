import os
from dotenv import load_dotenv
import telethon
from telethon import events
import datetime

load_dotenv(override=True)

#Global environments, do not change
wantsHistorySearch = False

#Be sure to create a .env file and add your API ID & HASH there.
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

#CUSTOM - Add your keywords here, you can also change the session name which is purely cosmetic
session_name = "Developement"
keywords = [
    "banana", "apple", "fruit"
]

client = telethon.TelegramClient(session_name, API_ID, API_HASH)

def getDate():
    currentDate = datetime.date.today()
    return currentDate

async def searchPastHistory():
    currentDate = getDate()
    async for chat in client.iter_dialogs():
        chatIdentifier = chat.entity
        if chat.is_private:
             continue
        async for msg in client.iter_messages(chatIdentifier):
             name = chat.title
             text = msg.raw_text.lower()
             textID = msg.id
             textDate = msg.date
             textOrigin = msg.chat_id

             if textDate < currentDate:
                  break

             for entries in keywords:
                if entries.lower() in text:
                    await client.send_message("me", f"Connection found!\nKeyword: {entries}\nMessage origin: {name}\nMessage ID: {textID}\n Message time: {textDate}\nMessage: {text}")
    


@client.on(events.NewMessage)   
async def handler(event):
    if event.is_private:
         return
    channel = await event.get_chat()
    name = channel.title
    text = event.raw_text.lower()
    textID = event.id
    textDate = event.date
    textOrigin = event.chat_id

    for entries in keywords:
        if entries.lower() in text:
                await client.send_message("me", f"Connection found!\nKeyword: {entries}\nMessage origin: {name}\nMessage ID: {textID}\n Message time: {textDate}\nMessage: {text}")
            
            
        
async def main():
    print(f"Connection successfull. Session name: {session_name}")
    while True:
        try:
            answer = input("Do you want to scan past messages up to a certain date? [y][n]").lower()
            if answer == "n" or answer == "no":
                break
            wantsHistorySearch = True
            answerDate = input("\nPlease enter the date up to which you want to scan messages for. Please make sure to strictly use the following format: day,month,year: ")    
            d, m, y = map(int, answerDate.replace(" ", "").split(","))
            targetDate = datetime.date(y, m, d)
            currentDate = getDate()
            print(f"Searching all public channels from {targetDate} to {currentDate}\n")
            break
        except Exception as e:
            print("Error", e)

    await client.start()
    await client.send_message("me", "Connection successfull")
    if wantsHistorySearch == True:
         searchPastHistory()
    await client.run_until_disconnected()

client.loop.run_until_complete(main())


    
