# frellnik
A Discord chat bot and ai meme generator using the openai api for images and chat.

## Installation
* Drop the files in the desired location
* Install packages with pip
```$ pip install -r requirements.txt```
* Follow these instrucitons to set up a discord bot account: https://discordpy.readthedocs.io/en/stable/discord.html
* Edit the config.ini file to include the following:
** Open AI Org and API Keys
** Discord API Key
** Channel ID in the server to send reconnection message to
** Discord Name of the admin user
** Discord Name of the Bot
** The Base Prompt, a brief description in plain language of who the bot is to help define its personality on the server.

## Usage
* Run frellnik.py with python
* Roll dice with `!roll` command
  * Example: `!roll 2d6` rolls 2 six sided dice
  * Separate multiple dice types with a comma `!roll 1d4, 2d6, 1d20`
* Add a keyphrase to the list that will trigger the bot at the rate defined in config.ini with `!keyword` command
* Add to the list of prompt modifiers with the `!prompt` command
  * the bot will choose a random one from the list with each reply trigger and append it to the prompt when generating reply text
* Use `!draw` to generate an image and post it to the channel
  * use the text following the command as a prompt that will define the image
  * Limited by the Image Rate Limit value in the config
* Use `!meme` to generate an image with meme text and post it to the channel
  * use the text following the command as a prompt to define the image and trigger a response as meme text
  * Also limited by the Image Rate Limit value, but each is only counted against other uses of their own commands
* Other than the commands above, replies are generated based on the rates defined in the config.



