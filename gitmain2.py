
# -*- coding: utf-8 -*-
from telethon import TelegramClient, events, sync
import os
from telethon import utils
import time
group_id = os.environ.get('group_id')
api_id = os.environ.get('api_id')
api_hash = os.environ.get('api_hash')
sp_group_id = group_id.split(",")

for num in range(len(api_id)):
    client = TelegramClient('session_name', api_id[num], api_hash[num])
    client.start()
    for useid in sp_group_id:
        real_id, peer_type = utils.resolve_id(int(useid))
        message = client.send_message(peer_type(real_id), '签到')    #第一项是机器人ID，第二项是发送的文字
client.disconnect()
time.sleep(5)
client.run_until_disconnected()

