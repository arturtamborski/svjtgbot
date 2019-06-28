import os
import sys
import json

HOME = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(HOME, 'deps'))

import requests

TOKEN = os.environ['TOKEN']
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
SEND_URL = f'{BASE_URL}/sendMessage'
NOOP_CMD = lambda: {'statusCode': 200}
COMMANDS = {}


def cmd_pong(context, message):
    return 'pong'


def cmd_hi(context, message):
    return 'Hi, ' + message['chat']['first_name']


def main(event, context):
    # load all commands
    if not COMMANDS:
        for name, func in dict(globals()).items():
            if name.startswith('cmd_'):
                COMMANDS[f'/{name}'] = func

    # handle request
    try:
        message = json.loads(event['body'])['message']
        command = message.split(' ')[0]
        chat_id = message['chat']['id']

        function = COMMANDS.get(command, NOOP_CMD)
        response = function(context, message)

        requests.post(SEND_URL, {
            'chat_id': chat_id,
            'text': response.encode('utf8'),
        })

    except Exception as e:
        print(e)

    return NOOP_CMD()
