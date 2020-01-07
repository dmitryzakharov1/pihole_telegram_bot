[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![Python](https://img.shields.io/badge/Python-2--3-green)](https://www.python.org/downloads/release/python-360/)

# pihole_telegram_bot

This is a simple statistics bot. Bot launched at Raspberry Pi 2B. 

## Getting Started

Just clone repo. Install systemd unit. 

### Prerequisites

You need:
- Raspberry Pi
- Python 2 or 3 installed
- GIT
- Created telegram bot with TOKEN (get it on [@BotFather](https://tele.gs/botfather "@BotFather"))
- Installed requirements.txt
- local tor socks5 proxy. Proxy needs if you cannot ping to api.telegram.org

```
pip install -r requirements.txt --no-index
```

### Installing

I use /opt directory to store binary and other stuff. Clone repo.

```
sudo su
mkdir /opt/
cd /opt
git clone https://github.com/dmitryzakharov1/pihole_telegram_bot.git
```

Install systemd unit

```
cd pihole_telegram_bot
cp parabot_service.service /lib/systemd/system
```

Update parabot.py with you telegram bot token and IP-adresses of Raspberry Pi.
INFO: I use local tor node as socks5 proxy. If you no need proxy. Just comment/uncomment updater = Updater(.... line

```
    REQUEST_KWARGS={
    'proxy_url': 'socks5://127.0.0.1:9100',
#    'urllib3_proxy_kwargs': {
#        'username': 'telebot',
#        'password': 'ksdafjlk3wart',
#    }
    }

    updater = Updater("TOKEN", request_kwargs=REQUEST_KWARGS)
    #updater = Updater("TOKEN")
```

## Check how it works
Start dialog with [parabot](https://tglink.ru/parabot "parabot")
Type `/systat` and get answer


## Built With

* [nano](https://www.nano-editor.org/) - GNU text editor

## License

This project is not licenced. Do all what you won.

## Special thanks
[python-telegram-bot](http://https://github.com/python-telegram-bot/python-telegram-bot "python-telegram-bot") and [PiHole-api](https://github.com/Ewpratten/PiHole-api "PiHole-api")

