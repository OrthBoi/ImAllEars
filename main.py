import os
from dotenv import load_dotenv
import telethon
from telethon import events
from telethon.tl.types import User
import datetime
import asyncio

load_dotenv(override=True)

#Be sure to create a .env file and add your API ID & HASH there.
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

#CUSTOM - Add your keywords here, you can also change the session name which is purely cosmetic
session_name = "Developement"
keywords = [
    ""
]

client = telethon.TelegramClient(session_name, API_ID, API_HASH)

def enterKeywords():
    keywords = input("Enter keywords seperated by commas (,): ").split(",")
    return keywords

def getDateTime():
    Date = datetime.datetime.now()
    return Date

def doesUserWantToScanHistory():
    answer = input("Do you want to scan past messages up to a certain date? [y][n]").lower()
    if answer == "n" or answer == "no":
        return False
    elif answer == "y" or answer == "yes":
        return True
    else:
        pass

def histroyScanUserInput():
    while True:
        try:
            answer = input("\nPlease enter the date up to which you want to scan messages for. Please make sure to strictly use the following format: day,month,year: ")    
            d, m, y = map(int, answer.replace(" ", "").split(","))
            desiredDate = datetime.datetime(y, m, d, tzinfo=datetime.timezone.utc)
            currentDate = getDateTime()
            print(f"Searching all public channels from {desiredDate} to {currentDate}\n")
            break
        except Exception as e:
            print("Error", e)
    return desiredDate

async def searchPastHistory(targetDate, keywords):
    #as of right now, if a message contains more than 1 keyword it will send a message for each keyword, this will send the message only once using the message id
    alreadyScannedResults = set()
    foundResults = 0
    async for chat in client.iter_dialogs():
        chatIdentifier = chat.entity
      
        if isinstance(chat.entity, User):
            continue
        async for msg in client.iter_messages(chatIdentifier, limit=10000):
            try:
                 name = chat.title
                 text = (msg.raw_text or "").lower()
                 textID = msg.id
                 textDate = msg.date
                 
                 if textDate < targetDate:
                      break

                 for entries in keywords:
                    if entries.lower() in text:
                        if textID in alreadyScannedResults:
                            continue
                        alreadyScannedResults.add(textID)
                        print("Connection found!")
                        foundResults = foundResults + 1
                        await client.send_message("me", f"Connection found!\nKeyword: {entries}\nMessage origin: {name}\nMessage ID: {textID}\n Message time: {textDate}\nMessage: {text}\n")
                        await asyncio.sleep(2)
                        
            except Exception as e:
                print(f"\nERROR: {e}\n")
    print(f"{foundResults} matches found.")
    
@client.on(events.NewMessage)   
async def handler(event):
    if event.is_private:
         return
    
    try:
        channel = await event.get_chat()
        name = channel.title
        text = (event.raw_text or "").lower()
        textID = event.id
        textDate = event.date

        for entries in keywords:
            if entries.lower() in text:
                    await client.send_message("me", f"Connection found!\nKeyword: {entries}\nMessage origin: {name}\nMessage ID: {textID}\n Message time: {textDate}\nMessage: {text}")
            
       
    except Exception as e:
        print(f"\nERROR: {e}\n")
     
async def main():
    print(f"Connection successfull. Session name: {session_name}")
    keywords = enterKeywords()
    historyScan = doesUserWantToScanHistory()
    if historyScan:
        desiredDate = histroyScanUserInput()
    await client.start()
    await client.send_message("me", "Connection successfull.")
    print("Connection succesfull.")
    if historyScan:
         await searchPastHistory(desiredDate, keywords)
         print("History scan completed, starting live monitoring.\n")
         await client.send_message("me", "History scan completed, starting live monitoring.")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())  