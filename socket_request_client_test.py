#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket_request
from devtools import debug

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

gs_file = "conf/gs.zip"
cid = "0x92c4dc"
socket_address = './cli.sock'

cc = socket_request.ControlChain(
    unix_socket=socket_address,
    cid=cid,
    # debug=True,
    auto_prepare=True,
    wait_state=True,
    # increase_sec=2
)
# cc.start()
# cc.leave()
# cc.join(files=join_payload)
# cc.start()
# res = cc.view_chain()
# res = cc.backup_list()
# base.dump(res.__dict__)

# debug(cc.view_system_config())
# debug(cc.system_config(payload={"key": "rpcIncludeDebug", "value": "true"}))
# debug(cc.chain_config(payload={"key": "autoStart", "value": True}))

# debug(cc.backup())
# debug(cc.backup_list())
# debug(cc.restore(payload={"name": "0x18ed1_0x53_icon_dex_20210830-032339.zip", "overwrite": True}))
# debug(cc.restore(name="0x18ed1_0x53_icon_dex_20210830-032339.zip"))


# res = cc.start()
# debug(res)
# debug(res.__dict__)
# debug(res.status_code)
#
# exit()

# debug(cc.backup())
# debug(cc.reset())
# debug(cc.start())

# debug("<<<<<<<<sdsdsdsd>>>>>>>>", cc.view_chain())
# debug(cc.view_chain(detail=True).__dict__)
# debug(cc.view_chain(inspect=True).__dict__)

# debug(cc.reset().status_code)
# debug(cc.backup())

debug(cc.restore(name="0x92c4dc_0x53_icon_dex_20210903-033922.zip"))
# debug(cc.start())
# debug(cc.backup_list())
# debug(cc.leave().status_code)
# debug(cc.join(seed_list=seed_list).status_code)
# debug(cc.start().status_code)
# debug(cc.view_chain().get_json("height"))


# while True:
#     debug(cc.view_chain(inspect=True))
#     debug(cc.view_system_config())
