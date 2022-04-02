import requests
import random, string
import time
from discord_webhook import DiscordWebhook

def RandomWord(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))
while True:
    InviteCode = ""
    for i in range(0,8):
        InviteCode = InviteCode+"\ndiscord.gg/"+RandomWord(random.randint(6,10))
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/959911393497337906/qQrgluR3XwCjV5SrpNS0DtpYT_gsffYdgJkQysW0UpDUPG5GRafUk8QrMR27eUh4JM4q', content=InviteCode)
    print(webhook.execute())
    time.sleep(2)
    