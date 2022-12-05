#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import sys
parent_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, parent_dir)
sys.path.insert(0, f"{parent_dir}/socket_request")

import socket_request
from devtools import debug

for idx, path in enumerate(sys.path, 1):
    print(f'{idx} - {path}')

print(f'\nrsocket-request module location - {socket_request.__file__}')


seed_list = [
    "20.20.5.166:7100",
    "20.20.5.167:7100",
    "20.20.5.168:7100",
    "20.20.5.169:7100",
    "20.20.5.170:7100",
    "20.20.5.172:7100",
    "20.20.5.173:7100",
    "20.20.5.174:7100",
    "20.20.5.175:7100",
    "20.20.5.176:7100"
]

# gs_file = "conf/gs.zip"
# with open(gs_file, "rb") as genesis_fd:
#     fd_data = genesis_fd.read()

config_payload = dict(
    seed_list=",".join(seed_list),
    role=3,
    maxBlockTxBytes=2048000,
    normalTxPool=30000,
    channel="icon_dex",
    autoStart=True,
    platform="icon",
    # JOIN_OPTION=dict(
    #     platform="icon"
    # )
)

cid = "0x87b86"
socket_address = './data/cli.sock'
# socket_address = '/tmp/socketname'

cc = socket_request.ControlChain(
    unix_socket=socket_address,
    cid=cid,
    debug=True,
    auto_prepare=False,
    wait_state=False
)
# debug(cc.view_chain())
debug(cc.reset_test(blockheight=100))
