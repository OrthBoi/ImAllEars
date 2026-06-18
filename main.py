import os
from dotenv import load_dotenv
import telethon
from telethon import events
from telethon.tl.types import User
import datetime
import asyncio
from pathlib import Path

load_dotenv(override=True)

#Be sure to create a .env file and add your API ID & HASH there.
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

#CUSTOM - Add your keywords here, you can also change the session name which is purely cosmetic
session_name = "Developement"


client = telethon.TelegramClient(session_name, API_ID, API_HASH)

def logResult(result):
    date = getDateTime()
    log = Path("log.txt")
    try:
        with open(log, "a", encoding="utf-8") as l:
            l.write(f"\n{date}\n{result}\n")
    except Exception as e:
         print(f"ERROR: {e}")

#TODO Add function to keep out duplicates
def enterKeywords(passedValue=None):
    keywords = Path("keywords.txt")
    if passedValue is None:
        userInput = input("Enter keywords seperated by commas (,): ").strip().lower().split(",")
    else:
        keyfile = Path("keywords.txt")
        with open(keyfile, "w", encoding="utf-8") as k: 
            k.write("")
        userInput = passedValue
    with open (keywords, "a+", encoding="utf-8") as k:
        keywordsFile = k.read()
        for entry in userInput:
            if entry.strip() not in keywordsFile:
                k.write(f"{entry.strip()}\n")

def readKeywords():
    keywords = []
    keyfile = Path("keywords.txt")
    with open(keyfile, "r", encoding="utf-8") as k: 
        for line in k:
            if line.strip():
                keywords.append(line.strip())
    return keywords

def editKeyfile():
    choice = input("Delete all [1], or certain keywords [2]?: ").strip()
    if choice.strip() == "1":
        keyfile = Path("keywords.txt")
        with open(keyfile, "w", encoding="utf-8") as k: 
            k.write("")
        enterKeywords()
    elif choice.strip() == "2":
        
        #TODO fix comparison logic
        keywordsToDelete = input("Enter the keywords to delete seperated by a comma (,): ").lower().split(",")
        oldKeywords = readKeywords()
        newKeywords = []
        for entry in oldKeywords:
            if entry not in keywordsToDelete:
                    newKeywords.append(entry)
        enterKeywords(newKeywords)
                
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

async def searchPastHistory(targetDate):
    #as of right now, if a message contains more than 1 keyword it will send a message for each keyword, this will send the message only once using the message id
    alreadyScannedResults = set()
    foundResults = 0
    async for chat in client.iter_dialogs():
        chatIdentifier = chat.entity
      
        if isinstance(chat.entity, User):
            continue
        keywords = readKeywords()
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
                        result = (f"Connection found!\nKeyword: {entries}\nMessage origin: {name}\nMessage ID: {textID}\n Message time: {textDate}\nMessage: {text}\n")
                        print(result)
                        await asyncio.sleep(1)
                        logResult(result)
                        
            except Exception as e:
                print(f"\nERROR: {e}\n")
    print(f"{foundResults} matches found.")
    
@client.on(events.NewMessage)   
async def handler(event):
    if event.is_private:
         return
    
    try:
        
        keywords = readKeywords()
        channel = await event.get_chat()
        name = channel.title
        text = (event.raw_text or "").lower()
        textID = event.id
        textDate = event.date

        for entries in keywords:
            if entries in text:
                    result = (f"Connection found!\nKeyword: {entries}\nMessage origin: {name}\nMessage ID: {textID}\n Message time: {textDate}\nMessage: {text}\n")
                    await client.send_message("me", f"{result}")
                    logResult(result)
            
       
    except Exception as e:
        print(f"\nERROR: {e}\n")
     
async def main():
    print(f"Connection successfull. Session name: {session_name}")
    if not Path("keywords.txt").exists() or Path("keywords.txt").stat().st_size == 0:
        enterKeywords()
    else: 
        adjustKeywords = input("Do you want to adjust or delete keywords?: [y][n]")
        if adjustKeywords.lower().strip() == "y" or adjustKeywords.lower().strip() == "yes":
            keyfileEditMode = input("Add [1] or delete [2] keywords?").strip()
            if keyfileEditMode == "1":
                enterKeywords()
            elif keyfileEditMode == "2":
                editKeyfile()



    historyScan = doesUserWantToScanHistory()
    if historyScan:
        desiredDate = histroyScanUserInput()
    await client.start()
    await client.send_message("me", "Connection successfull.")
    print("Connection succesfull.")
    if historyScan:
         await searchPastHistory(desiredDate)
         print("History scan completed, starting live monitoring.\n")
         await client.send_message("me", "History scan completed, starting live monitoring.")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())  