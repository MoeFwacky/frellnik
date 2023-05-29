# frellnik
frellnik is a versatile Discord chat bot and AI meme generator that utilizes the OpenAI API for image and chat functionalities. It offers various commands to enhance your Discord server experience.

## Installation
Follow these steps to set up and run frellnik:
* Clone or download the repository and place the files in your desired location.
* Install the required packages using pip:
```$ pip install -r requirements.txt```
* Follow these instrucitons to set up a discord bot account: https://discordpy.readthedocs.io/en/stable/discord.html
* Edit the config.ini file and provide the necessary information:
  * Open AI Org and API Keys
  * Discord API Key
  * Channel ID in the server to send reconnection message to
  * Discord Name of the admin user
  * Discord Name of the Bot
  * The Base Prompt: A concise plain-language description of the bot, defining its personality on the server.

## Usage
To use frellnik, follow these instructions:
* Run frellnik.py with python
* Roll dice with `!roll` command
  * Example: `!roll 2d6` rolls 2 six sided dice
  * Separate multiple dice types with a comma `!roll 1d4, 2d6, 1d20`
* Add a keyphrase to the list that will trigger the bot at the rate defined in config.ini with `!keyword` command
* Modify the list of prompt modifiers with the `!prompt` command. The bot randomly selects one from the list with each reply trigger, appending it to the prompt when generating the reply text.
* Generate an image and post it to the channel using the `!draw` command:
  * Use the text following the command as a prompt to define the image
  * Note: This command is limited by the Image Rate Limit value specified in config.ini.
* Generate an image with meme text and post it to the channel using the `!meme` command:
  * Use the text following the command as a prompt to define the image and trigger a response as meme text.
  * Note: This command is also limited by the Image Rate Limit value, but each usage is only counted against other uses of the same command.
* Apart from the specific commands mentioned above, replies are generated based on the rates defined in the config.ini file.



