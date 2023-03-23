# Chadow the Chadgehog
-----
*Chadow* is a Discord bot written in Python that spits out a random quote from Snapcube's Sonic the Hedgehog Fandubs!

The bot is currently being hosted on [railway.app](https://railway.app). 

[Invite link](https://discord.com/api/oauth2/authorize?client_id=1032925984976011264&permissions=8&scope=bot%20applications.commands)

## Demo

![Demo](https://cdn.discordapp.com/attachments/1032086244559179807/1037594165812404234/chadow_demo.gif)

## Current Features
`/quote` - Generate a random quote!

## Installation
1. Download this repo
2. Navigate to the bot directory via Terminal
3. Create a virtual environment: 
- Mac: `python3 -m venv bot-env`
- Windows: `py -3 -m venv bot-env` 
4. Activate the virtual environment: 
- Mac: `source bot-env/bin/activate`
- Windows: `bot-env\Scripts\activate.bat`
5. Install the needed libraries: 
- Mac: `pip install -r requirements.txt`
- Windows: `py -3 -m pip install -r requirements.txt`
6. Create a `.env` file with:
- `DISCORD_BOT_TOKEN = ''`
- `DISCORD_BOT_APP_ID = ''`
7. Run `main.py`

## Process
1. Grab scripts from [here](https://realtimefandub.fandom.com/wiki/Category:SnapCube%27s_Real-Time_Fandub_episode_transcripts)
2. Clean scripts getting rid of non-spoken lines
3. Create Discord Bot

## TODO

- [x] Initial commit
- [ ] Add list of characters embed
- [ ] Filter by character
- [ ] Filter by Fandub
- [ ] Show list of lines by [character]
- [ ] Show number of lines by [character]
