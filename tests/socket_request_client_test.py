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

# chain_control_sock("start", cid)
# exit()
# chain_control_sock("stop", cid)
# exit()

# chain_control_sock("view_configure", cid)
# exit()
# chain_control_sock("chain_configure", cid,)


# chain_control_sock("chain_configure", cid, payload={"key": "autoStart", "value": "true"})
# chain_control_sock("view_configure", cid)
#
# exit()

# chain_control_sock("system_configure", cid, payload={"key": "rpcIncludeDebug", "value": "true"})
# chain_control_sock("view_system_configure", cid)
#
# exit()
# chain_control_sock("backup", cid)
# chain_control_sock("backup_list", cid)
# chain_control_sock("restore", cid, payload={"name": "0x3340cf_0x53_icon_dex_20210826-141203.zip", "overwrite": True})


# chain_control_sock("leave", cid)

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

cid = "0x153140"
socket_address = './data/cli.sock'

cc = socket_request.ControlChain(
    unix_socket=socket_address,
    # cid=cid,
    debug=True,
    auto_prepare=True,
    wait_state=True
)
# debug(chain_control.url)
# cc.view_system_config()
# a = cc.stop()
# cc.start()
# cc.view_system_config()
# cc.view_chain()
# cc.test(detail=True, headers={"sss","sdsdsd"})
# cc.start()
# for i in range( 1, 10):

# cc.start()
# cc.leave()
# cc.join(files=join_payload)
# cc.start()
# res = cc.view_chain()
# debug(res.__dict__)

# res = cc.backup_list()
# base.dump(res.__dict__)
# socket_request.color_print("red", "FAIL")
# socket_request.color_print("red")
# debug(cc.reset())
# debug(cc.leave())
# debug(cc.join(seed_list=seed_list))
# debug(cc.start())
# debug(cc.view_chain(detail=True))

# debug(cc.view_system_config())
# debug(cc.system_config(payload={"key": "rpcIncludeDebug", "value": "true"}))
# debug(cc.view_system_config())

# for i in range(1, 10):
#     debug(cc.leave())
#     debug(cc.join(seed_list=seed_list))

# cc.start()
# for i in range(1, 10):
#     debug(cc.leave())
#     debug(cc.join(seed_list=seed_list))
#     debug(cc.start())

# debug(cc.chain_config(payload={"key": "autoStart", "value": True}))

# debug(cc.leave())
# debug(cc.join(seed_list=seed_list))

# for i in range(1, 100):

# debug(cc.start())

# debug(cc.guess_cid())

# debug(cc.start())

# debug(cc.backup())
# debug(cc.backup_list())
# debug(cc.restore(payload={"name": "0x18ed1_0x53_icon_dex_20210830-032339.zip", "overwrite": True}))
# debug(cc.restore(restore_name="0x18ed1_0x53_icon_dex_20210830-032339.zip"))


# res = cc.start()
# debug(res)
# debug(res.__dict__)
# debug(res.status_code)
#
# exit()

# debug(cc.chain_config(payload={"autoStart": False}))
# debug(cc.chain_config(payload={"autoStart": True, "txTimeout": 60001}))
# debug(cc.chain_config(payload={"key": "autoStart", "value": 'true'}))
# debug(cc.system_config(payload={"rpcIncludeDebug": True}))
# debug(cc.system_config(payload={"key": "rpcIncludeDebug", "value": True}))

debug(cc.view_chain())
# debug(cc.start())
# debug(cc.backup_list())
# debug(cc.restore(restore_name="0x64c2c6_0x2_icon_dex_20220519-091158.zip"))
debug(cc.prune(1))
# debug(cc.stop())
debug(cc.backup())
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


