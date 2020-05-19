"""
This script will post a new message everyday on Skype
"""
import datetime, os, random
import new_hire_messages as new_hire_msg
from skpy import Skype

#Channels
Qxf2_PTO='19:f33e901e871d4c3c9ebbbbee66e59ebe@thread.skype'
Qxf2_Main='19:I211cmFsaWRoYXJhbi5hcnVua3VtYXIvJHJhamkuZ2FsaTtkYmQyNjZlY2RjN2NmMzY3@p2p.thread.skype'
ETC_ETC_ETC='19:626bd82f2bf249e788091763f2042b87@thread.skype'

def get_weekday():
    "Return the current day of the week"
    #Src: https://stackoverflow.com/a/9847269
    #Note: Monday is 0 and Sunday is 6
    return datetime.datetime.today().weekday()

def get_quote():
    "Return a good quote"
    return random.choice(new_hire_msg.QUOTES)

def get_comic():
    "Return a comic"
    return random.choice(new_hire_msg.COMICS)

def get_encouragement():
    "Return some encouragement"
    return random.choice(new_hire_msg.ENCOURAGEMENTS)

def get_habits():
    "Return some habits we want to drill in"
    return random.choice(new_hire_msg.HABITS)

def get_reminders():
    "Return a reminder"
    return random.choice(new_hire_msg.REMINDERS)

def get_message(day):
    "Return a suitable message based on the day of the week"
    if day==0: #Monday
        return get_quote()
    if day==1: #Tuesday
        return get_comic()
    if day==2: #Wednesday
        return get_habits()
    if day==3: #Thursday
        return get_encouragement()
    if day==4: #Friday
        return get_reminders()

def post_message(msg):
    "Post a message"
    sk = Skype(os.environ.get('SKYPE_USERNAME'),os.environ.get('SKYPE_PASSWORD'))
    channel = sk.chats.chat(Qxf2_Main)
    channel.sendMsg(msg)

#----START OF SCRIPT
if __name__=='__main__':
    weekday = get_weekday()
    msg = get_message(weekday)
    post_message(msg)