# Flaki
### Flaki can be used for:

**1. Moderation:**

*    1.1 Ban
    
*    1.2 Temp ban

*    1.3 Kick

*    1.4 Warn (with customizability)

*    1.5 Timeout

*    1.6 Purge

**2. Fun:**

*   People can interact with each other with commands 

**3. Counting game:**

*   You can add a counting game to make server more interesting


**4. Levels:**

*   Have good leveling system for slow progression

**5. Markov chain:**

*   Remembers chat messages and generates his messages based on them

**6. AI:**

* You can ask anything AI with its own personality 


## How to try:
1. Create a bot in Discord Developer Portal and copy his token
2. Go to https://aistudio.google.com/api-keys and create api key
3. git clone https://github.com/atomixkl/Flaki
4. Download required libraries:
```
discord.py
openai
python-dotenv
``` 
5. Create .env file and paste your bot token and Gemini api key:
```
DS_TOKEN="Your Discord bot token"
GMN_KEY="Your Gemini api key"
```
6. Launch it!:
```
python Flaki.py
```