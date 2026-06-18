# 👂 AllEars

**Live Telegram keyword monitoring and historical message search using Telethon**



## 🧠 Overview

AllEars is a lightweight Telegram monitoring tool that scans channels and groups for user-defined keywords.

It runs on your own Telegram account using the Telethon API and delivers alerts directly to your “Saved Messages” chat.



## ⚙️ Features

- 🔴 Real-time monitoring of Telegram channels and groups  
- 📜 Historical message scanning (beta)  
- 🔑 Keyword-based detection system  
- 📩 Instant notifications via Telegram “Saved Messages”
- 📜 Logfile for each alert
- 💻 Fully self-hosted (runs locally on your machine)



## 🧰 Tech Stack

- Python 3.9+
- Telethon
- python-dotenv



## 📦 Supported Platforms

- Windows ✔ (tested) 
- Linux ✔ (tested)  
- macOS ⚠ (untested, likely compatible)



## INSTALLATION & SETUP

### Create a Telegram API App

Go to https://my.telegram.org

Create a new application

Copy your API_ID and API_HASH


### Clone the repository

git clone https://github.com/OrthBoi/ImAllEars.git

<code>cd ImAllEars</code>

Create a file named .env in the project folder

Inside it write:

API_ID=your_api_id

API_HASH=your_api_hash

### Create virtual environment
<code>python -m venv venv</code>

Activate it:

Windows:
<code>venv\Scripts\activate</code>

Linux / macOS:
<code>source venv/bin/activate</code>

Install dependencies and run the programm
<code>pip install -r requirements.txt</code>
Run the program <code>python main.py</code>
