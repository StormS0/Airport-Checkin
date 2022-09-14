
# -*- coding: utf-8 -*-
from telethon import TelegramClient, events, sync
import os
from telethon import utils

group_id = os.environ.get('group_id')
api_id = os.environ.get('api_id')
api_hash = os.environ.get('api_hash')
sp_group_id = group_id.split(",")

for num in range(len(api_id)):
    session_name[num] = "id_" + str(session_name[num])
    client = TelegramClient('session_name', api_id[num], api_hash[num] ,proxy=("socks5", '127.0.0.1', 1081))
    client.start()
    for useid in sp_group_id:
        real_id, peer_type = utils.resolve_id(useid)
        message = client.send_message(peer_type(real_id), '签到')    #第一项是机器人ID，第二项是发送的文字
