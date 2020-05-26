"""
This script will let a user send messages on Skype
"""
import json
import os
from skpy import Skype

def get_channel_id(event):
    "Return the channel id, default to main if channel not available"
    channel = 'main'
    if event.has_key('channel'):
        channel = event['channel'].lower()
    channels = os.environ.get('SKYPE_CHANNELS')
    channels = channels.replace("'", "\"")
    channels = json.loads(channels)
    if channels.has_key(channel):
        channel_id = channels[channel]
    else:
        channel_id = channels['main']

    return channel_id

def post_message(event, context=None):
    "Post a message"
    msg = event['msg']
    channel_id = get_channel_id(event)
    skype_handler = Skype(os.environ.get('SKYPE_USERNAME'), os.environ.get('SKYPE_PASSWORD'))
    channel = skype_handler.chats.chat(channel_id)
    channel.sendMsg(msg)
