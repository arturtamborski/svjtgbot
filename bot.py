import json
from os import environ
from random import randint
from botocore.vendored import requests

import names


BASE_URL = 'https://api.telegram.org/bot' + environ['TG_TOKEN']
SEND_URL = BASE_URL + '/sendMessage'


def main(event, context):
    message = json.loads(event['body'])['message']
    chat_id = message['chat']['id']
    command = message['text']

    if command:
        special_n = randint(0, len(names.special))
        first_n = randint(0, len(names.first))
        last_n = randint(0, len(names.last))

        response = names.first[first_n] + ' ' + names.last[last_n]

        if randint(0, 10) > 7:
            response = names.special[special_n]

        requests.post(SEND_URL, {
            'chat_id': chat_id,
            'text': response.encode('utf8')
        })

    return {'statusCode': 200}
