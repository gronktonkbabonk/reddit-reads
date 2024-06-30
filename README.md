# Reddit Reads
### A highly customizable way to create *those* videos (you know the ones i'm talking about). Pick and choose features that you want for your video. the subreddit, sort by, and more (you can see the full list when you run it.)

DISCLAIMER: i don't post this kinda content myself, i just picked this up as a fun project.

### ❗🚨 WARNING: DO NOT RUN ANY OF THE PYTHON FILES YOURSELF, PLEASE USE THE BATCH/SHELL FILES PROVIDED INSTEAD. 🚨❗ 

# Requirements

### Need manual install:
- [Python version 3.4+](https://www.python.org/downloads/)

### These will all be installed in the initial running of the project:
- The python libraries [python-dotenv](https://pypi.org/project/python-dotenv/) and [moviepy](https://pypi.org/project/moviepy/)

- [Imagemagick](https://imagemagick.org/)

## Needed to get the reddit api working:
- Reddit username and password

- Reddit client ID

- Reddit bot secret

- The last two can be obtained by following the [tutorial below](#how-to-create-a-reddit-bot-and-get-the-needed-info).

## Installation and usage

### Install and first time running:
All you need to do is clone this repository, and run the appropriate run file. .bat for windows, and .sh for linux or mac.

upon running for the first time, simply follow the instructions given to you by the tool. Please don't worry about entering your username and password, there's no possible way that i, or anyone else can access it through this.

### To actually use the tool, upload one or multiple video files into the "videos" directory, and run the tool. Please report any bugs or errors to me and i'll do my best to rectify them.

## How to create a Reddit bot and get the needed info

### Step 1: Go to (reddit.com/prefs/apps)[https://www.reddit.com/prefs/apps], and click "create an app"
### Step 2: Fill in the form:
- For the name, make it anything you want.
- For the next option, select "script"
- Fill in the description
- For the about url, you can fill in any valid web address. i'd suggest making it the link to this repo or a registered domain of your own.
### Step 3: Click "create app". DO NOT CLOSE THIS PAGE UNTIL YOU HAVE THE SECRET SETUP
- copy the random **bolded** text located directly underneath the name of the bot, and save enter it when the script asks for the Client ID
- copy the secret, and enter it when the script asks for the secret