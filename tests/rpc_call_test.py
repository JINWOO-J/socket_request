#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import sys
parent_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# sys.path.append(parent_dir)
sys.path.insert(0, parent_dir)

import socket_request
from devtools import debug

for idx, path in enumerate(sys.path, 1):
    print(f'{idx} - {path}')

print(f'\nrsocket-request module location - {socket_request.__file__}')


cid = "0x153140"
socket_address = './data/cli.sock'

cc = socket_request.ControlChain(
    unix_socket=socket_address,
    cid=cid,
    debug=True,
    auto_prepare=False,
    wait_state=False
)

# debug(cc.view_chain())
payload = {
    "jsonrpc": "2.0",
    "method": "icx_getBlockByHeight",
    "id": 1234,
    "params": {
        "height": "0x22"
    }
}


debug(cc.rpc_call(payload=payload))

# debug("<<<<<<<<sdsdsdsd>>>>>>>>", cc.view_chain())
# debug(cc.view_chain(detail=True).__dict__)
# debug(cc.view_chain(inspect=True).__dict__)
# debug(cc.leave())
# # debug(cc.reset())
# debug(cc.join(role=3, seedAddress=["20.20.6.77:7100", "20.20.6.79:7100", "20.20.6.80:7100"]))
# debug(cc.start())
# debug(cc.backup_list())


# docker = socket_request.DockerSock()
# debug(docker.get_docker_images())

# socket_request.get_state_loop(loopfunc=cc.view_chain, check_key="state", required_state="started", description="check status")


