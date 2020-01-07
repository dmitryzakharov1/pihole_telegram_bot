 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
#
# THIS EXAMPLE HAS BEEN UPDATED TO WORK WITH THE BETA VERSION 12 OF PYTHON-TELEGRAM-BOT.
# If you're still using version 11.1.0, please see the examples at
# https://github.com/python-telegram-bot/python-telegram-bot/tree/v11.1.0/examples

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage: 
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from gpiozero import CPUTemperature, LoadAverage, DiskUsage

import pihole as ph

pihole = ph.PiHole("192.168.1.13")

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    bot.send_message(chat_id=update.message.chat_id, text='Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    bot.send_message(chat_id=update.message.chat_id, text='/start')
    bot.send_message(chat_id=update.message.chat_id, text='/sysstat')

def sysstat(bot, update):
    """ Print system status"""
    cpu = CPUTemperature()
    txt = 'CPU temperature is '+ str(cpu.temperature)
    bot.send_message(chat_id=update.message.chat_id, text=txt)

    la = LoadAverage(min_load_average=0, max_load_average=2)
    txt = 'Load average is '+str(la.value)
    bot.send_message(chat_id=update.message.chat_id, text=txt)

    disk = DiskUsage()
    txt = 'Current disk usage: {}%'.format(disk.usage)
    bot.send_message(chat_id=update.message.chat_id, text=txt)

    #pihole stats

    txt = 'Domains in blocklists: '+str(pihole.domain_count)
    bot.send_message(chat_id=update.message.chat_id, text=txt)

    txt = 'Percent of blocked queries: '+ str(pihole.ads_percentage)
    bot.send_message(chat_id=update.message.chat_id, text=txt)

def echo(bot, update):
    """Echo the user message."""
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', bot, update.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary


    

    REQUEST_KWARGS={
    'proxy_url': 'socks5://127.0.0.1:9100',
#    'urllib3_proxy_kwargs': {
#        'username': 'login',
#        'password': 'password',
#    }
    }

    updater = Updater("TOKENHERE", request_kwargs=REQUEST_KWARGS)
    #updater = Updater("TOKENHERE")


    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("sysstat", sysstat))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
