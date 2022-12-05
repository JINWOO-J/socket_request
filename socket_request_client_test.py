#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import socket_request
from devtools import debug

seed_list = [
    # "20.20.5.166:7100",
    # "20.20.5.170:7100",
    # "20.20.5.167:7100",
    # "20.20.5.174:7100",
    # "20.20.5.173:7100",

    "20.20.1.242:7100",
    "20.20.1.122:7100",
    "20.20.1.123:7100",
    "20.20.1.65:7100",
    "20.20.1.167:7100",
]

# seed_list = [
#     "20.20.5.169:7100",
#     "20.20.5.172:7100",
#     "20.20.5.175:7100",
#     "20.20.5.176:7100",
#     "20.20.5.168:7100",
#     "20.20.5.166:7100",
#     "20.20.5.170:7100",
#     "20.20.5.167:7100",
#     "20.20.5.174:7100",
#     "20.20.5.173:7100"
# ]

gs_file = "conf/gs.zip"
cid = "0x546653"
socket_address = './data/cli.sock'

cc = socket_request.ControlChain(
    unix_socket=socket_address,
    # cid=cid,
    # debug=True,
    auto_prepare=True,
    wait_state=True,
    timeout=30
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

# debug(cc.view_chain())
# debug(cc.guess_cid())
# debug(cc.stop())
# time.sleep(3)
# debug(cc.stop())

# for i in range(1, 10):
#     debug(cc.join())

# for i in range(1,100):
#     debug(cc.leave())
#     debug(cc.join(seed_list=seed_list))
#     debug(cc.start())
#     time.sleep(3)
#     debug(cc.view_chain().json)





# debug(cc.backup())
# debug(cc.reset())
# debug(cc.start())

# debug("<<<<<<<<sdsdsdsd>>>>>>>>", cc.view_chain())
# debug(cc.view_chain(detail=True).__dict__)
# debug(cc.view_chain(inspect=True).__dict__)

# debug(cc.reset().status_code)
# debug(cc.backup())
#
# debug(cc.restore(name="0x92c4dc_0x53_icon_dex_20210906-044248.zip"))
# debug(cc.start())
# debug(cc.backup_list())
# debug(cc.leave().status_code)
# debug(cc.join(seed_list=seed_list).status_code)
# debug(cc.start())
# debug(cc.view_chain().get_json("height"))

# cc.stop()

payload = {
    "normalTxPool": 30001,
    # "role": 3,
    # "seedAddress": "20.20.1.122:7100,20.20.165:7100,20.20.1.223:7100,20.20.1.167:7100,20.20.1.242:7100",
    # "autoStart": True,

}

# res = cc.chain_config(payload=payload)
#
# debug(res.status_code)
#
# # debug(res.json)
# debug(res.get_json())

# result = cc.view_chain(inspect=True)
#
# debug(result)

# debug(cc.get_state())

# metrics = result.json['module'].get('metrics')
# debug(metrics)
# socket_request.print_table("ttt", source_dict=metrics)
# while True:
#     debug(cc.view_chain(inspect=True))
#     debug(cc.view_system_config())

# cc.join(seedAddress=seed_list, gs_file="conf/icon_genesis.zip", role=3)

# debug(cc.view_chain(cid=None))
# debug(cc.restore(restore_name="0x87b86_0x53_icon_dex_20220614-074532.zip"))
debug(cc.prune(blockheight=1))
debug(cc.get_state())

# for i in range(1, 100):
#     print(i)
#     cc.leave()
#     cc.join(seedAddress=seed_list, gs_file="conf/icon_genesis.zip", role=3)
#     cc.start()
#     time.sleep(3)
#     debug(cc.get_state())


