<div align='center'>

# JAK-Telegram-Bot
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg?style=for-the-badge)](https://github.com/psf/black)

</div>

- 	Note: [Formatting](#format-code) the Code before Pushing is Important!!

## Use it
To use the bot, go to [Telegram](https://web.telegram.org/) and search for `JAK-Telegram-Bot`
you can use the bot from there.

## Steps

### Clone the Repository
To Clone this Repository, open a terminal in a empty folder and type 
```bash
git clone https://github.com/Jonak-Adipta-Kalita/JAK-Telegram-Bot.git
```

### Installing The Required Modules
To install the required modules, just open a terminal in the directory where this project is cloned. Now type: 
```bash
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
```
and hit enter.

### Starting the Bot:
Create `.env`. Now go to [Telegram](https://web.telegram.org/) and search for `BotFather`. 
In the Chat press `Start` or type `/start`. Then give your bot a name and then a username
Now copy the Token given by the `BotFather` and paste it in the `.env` file 
```env
TOKEN=<YOUR_BOT_TOKEN>
```
like this. After you added the bot, open any terminal in the directory and type 
```bash
python main.py
```
and hit Enter.

## Format Code
In a terminal, type
```bash
.\venv\Scripts\activate
black .
deactivate
```
and press Enter.

## Contributors
<a href = "https://github.com/Jonak-Adipta-Kalita/JAK-Telegram-Bot/graphs/contributors">
	<img src = "https://contrib.rocks/image?repo=Jonak-Adipta-Kalita/JAK-Telegram-Bot"/>
</a
