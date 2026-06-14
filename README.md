# 👂AllEars

## Live monitoring and history search for keywords using Telegram API

\*history search feature yet to be implemented
<br>

## Technologies used

<img align="left" width="30px" src="https://camo.githubusercontent.com/b024a703f6c1dc4fca503f2d8663b6c69e2f2b8473e6461c35ed1ebbb4d3eabc/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f64657669636f6e732f64657669636f6e406c61746573742f69636f6e732f707974686f6e2f707974686f6e2d6f726967696e616c2e737667" data-canonical-src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" style="max-width: 100%;">
<img align="left" src="https://api.iconify.design/logos:telegram.svg" alt="telegram" width="30" height="30" />
<br>
<br>

## Features

- Real-time Telegram message monitoring across channels and groups
- Historical message scanning (in development / experimental)
- Keyword-based alerts delivered directly to your Telegram Saved Messages (“Favorites”) chat
- Lightweight and self-hosted — runs on your own account using Telethon

<br>

## Description

**AllEars** is a Telegram monitoring tool that tracks messages across channels and groups based on user-defined keywords.

It can be used to:

- Monitor large amounts of Telegram channels without manually checking each one
- Track specific names, topics, or terms across public discussions
- Receive instant notifications when relevant messages appear
- Optionally scan historical messages to recover past matches (experimental feature)

Whether you're tracking information across communities or simply trying to avoid missing important mentions, AllEars automates the process of searching and alerting.

<br>

## Supported Platforms

- Windows ✔
- Linux ✔ (tested)
- macOS ⚠ (untested, likely functional but not verified)

Requires Python 3.9+ and Telethon-compatible environment.

<br>

## How to use

Firstly log in to your [Telegram core](https://my.telegram.org) and create a new application, remember the API_ID and the API_HASH.

<ul>
  <li>Clone the repo using <code>git clone https://github.com/OrthBoi/ImAllEars.git</code>.</li>
  <li>Go into the repo using <code>cd ImAllEars</code>.</li>
  <li>Create a new file named ".env" and add "API_ID=your custom api id" to line 1 and "API_HASH=your custom api hash" to line 2, do not put the numbers in "".</li>
  <li>Go into main.py and under the #CUSTOM section add your desired keywords and give your application a custom session name</li>
  <li>Rightclick the folder and click on "open in terminal"</li>
  <li>Create a virtual environment using <code>python -m venv venv</code> (if that doesnt work, try python3) </li>
  <li>Go into the virtual environment using <code>source venv/bin/activate</code></li>
  <li>Install the requirements usin <code>pip install -r requirements.txt</code></li>
  <li>Lastly, run <code>python main.py</code></li>
</ul>

You will get a notification in your private favorites chat if the programm detects any matched, it will tell you the channel name, the message id, the datetime and the content of the message.
