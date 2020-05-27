"""
This script will let a user send messages on some Qxf2 Skype channels
The channels must be listed in the environment variable SKYPE_CHANNELS
"""
import json
import os
from skpy import Skype

def get_dict(my_string):
    "Return a dict from a string"
    my_string = my_string.replace("'", "\"")
    my_string = json.loads(my_string)

    return my_string

def get_channel_id(msg_body):
    "Return the channel id, default to main if channel not available"
    channel = 'main'
    if 'channel' in msg_body.keys():
        channel = msg_body['channel'].lower()
        print(f'The channel in the message is: {channel}')
    channels = get_dict(os.environ.get('SKYPE_CHANNELS'))
    print(f'The available channels are {channels}')
    if channel in channels.keys():
        channel_id = channels[channel]
    else:
        channel_id = channels['main']

    return channel_id

def post_message(event, context=None):
    "Post a message"
    print(f'The trigger event is: {event}')
    full_msg = get_dict(event['Records'][0]['body'])
    if 'msg' in full_msg.keys():
        msg = full_msg['msg']
        channel_id = get_channel_id(full_msg)
        skype_handler = Skype(os.environ.get('SKYPE_USERNAME'), os.environ.get('SKYPE_PASSWORD'))
        channel = skype_handler.chats.chat(channel_id)
        channel.sendMsg(msg)
    else:
        print('The event had no key called msg in it\'s body')
