"""
Listen to a channel and send the message to an SNS

References:
1. https://pypi.org/project/SkPy/
"""

from skpy import SkypeEventLoop, SkypeNewMessageEvent
import os
import random
import qxf2_skype_sender

class SkypeListener(SkypeEventLoop):
    "Listen to a channel continuously"
    def __init__(self):
        username = os.environ.get('SKYPE_USERNAME')
        password = os.environ.get('SKYPE_PASSWORD')
        super(SkypeListener, self).__init__(username, password)

    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent):
            user_id = event.msg.userId
            chat_id = event.msg.chatId
            message = event.msg.content
            print(f'On channel {chat_id}, {user_id} sent the message: {message}')


#----START OF SCRIPT
if __name__ == "__main__":
    big_bro = SkypeListener()
    big_bro.loop()