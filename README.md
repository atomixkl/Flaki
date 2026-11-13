# Flaki
### Flaki can be used for:

**1. Moderation:**

*    1.1 Ban
    
*    1.2 Temp ban

*    1.3 Kick

*    1.4 Warn (with customizability) and soft warn

*    1.5 Timeout

*    1.6 Purge

**2. Fun:**

*   People can interact with each other with commands 

**3. Counting game:**

*   You can add a counting game to make server more interesting

**4. Levels:**

*   Have good leveling system for slow progression

**5. Reminder:**

*   You can make bot send your message at any time of day you want

**6. Markov chain:**

*   Remembers chat messages and generates his messages based on them

**7. AI:**

* You can ask anything AI with its own personality 


## How to try:
1. Create a bot in Discord Developer Portal and copy his token
2. In Discord Developer Portal add bot to your server in Installation with administrator permission
3. Go to https://aistudio.google.com/api-keys and create api key
4. Git clone project:
```
git clone https://github.com/atomixkl/Flaki
```
5. Download required libraries:
```
discord.py openai python-dotenv
``` 
6. Create .env file and paste your bot token and Gemini api key:
```
DS_TOKEN="Your Discord bot token"
GMN_KEY="Your Gemini api key"
```
7. Launch it!:
```
python Flaki.py
```

(You should reload Discord with Ctrl + R if you don't have any commands)