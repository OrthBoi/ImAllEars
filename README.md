# 👂AllEars

## Live monitoring and history search for keywords using Telegram API

<br>

## Technologies used
<img align="left" width="30px" src="https://camo.githubusercontent.com/b024a703f6c1dc4fca503f2d8663b6c69e2f2b8473e6461c35ed1ebbb4d3eabc/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f64657669636f6e732f64657669636f6e406c61746573742f69636f6e732f707974686f6e2f707974686f6e2d6f726967696e616c2e737667" data-canonical-src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" style="max-width: 100%;">
<img align="left" src="https://api.iconify.design/logos:telegram.svg" alt="telegram" width="30" height="30" />
<br>
<br>

## Features

- Live monitoring
- History search
- Personal notification in the "favorite" chat of the Telegram user
<br>

## Description
Do you need to search a ton of Telegram channels for a specific keyword? Maybe you lost a close relative and want to search his name in search and rescue groups? Maybe you are interested in a specific topic and want to be notified?<br>
Then you can use AllEars to monitor for your keywords and even search past chat messages to not miss out!
<br>

## Supported plattforms
The application works on Windows and on Linux as long as all dependencies are installed (tested), mac remains untested, but should work just fine.

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


