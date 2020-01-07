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
mkdir /opt/
cd /opt
git clone https://github.com/dmitryzakharov1/pihole_telegram_bot.git
cd pihole_telegram_bot
```

Install systemd unit

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [nano](https://www.nano-editor.org/) - GNU text editor

## License

This project is not licenced. Do all what you won.
