#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import socket_request
from devtools import debug

# seed_list = [
#     "20.20.5.166:7100",
#     "20.20.5.167:7100",
#     "20.20.5.168:7100",
#     "20.20.5.169:7100",
#     "20.20.5.170:7100",
#     "20.20.5.172:7100",
#     "20.20.5.173:7100",
#     "20.20.5.174:7100",
#     "20.20.5.175:7100",
#     "20.20.5.176:7100"
# ]

# seed_list = [
#     # "20.20.5.169:7100",
#     # "20.20.5.172:7100",
#     # "20.20.5.175:7100",
#     # "20.20.5.176:7100",
#     # "20.20.5.168:7100",
#     # "20.20.5.166:7100",
#     "20.20.5.170:7100",
#     # "20.20.5.167:7100",
#     # "20.20.5.174:7100",
#     # "20.20.5.173:7100"
# ]

# seed_list = [
#     "20.20.5.166:7100",
#     "20.20.5.170:7100",
#     "20.20.5.167:7100",
#     "20.20.5.174:7100",
#     "20.20.5.173:7100",
# ]
seed_list = [
    "20.20.6.69",
    "20.20.6.67",
    "20.20.6.68",
    "20.20.6.71",
    "20.20.6.70"
]

gs_file = "conf/icon_genesis.zip"
# gs_file = "conf/gs.zip"
cid = "0xca97ec"
socket_address = './cli.sock'

cc = socket_request.ControlChain(
    unix_socket=socket_address,
    # cid=cid,
    debug=True,
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


# debug(cc.leave())
# debug(cc.join(seed_list=seed_list, gs_file=gs_file))
# time.sleep(2)

# cc.stop()
#
# debug(cc.import_icon(
#         payload={
#             "store_uri": "/goloop/icon/nvme/.storage/db_icon_dex,http://20.20.6.65:8000/api/v3",
#             # "store_uri": "http://20.20.6.65:8000/api/v3",
#             "config_url": "http://20.20.6.65:8000/config/nvme.json",
#             "max_rps": 500
#         }
#     )
# )


# debug(cc.backup())
# debug(cc.reset())
# debug(cc.start())


debug(cc.view_chain())

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

# while True:
#     debug(cc.view_chain(inspect=True))
#     debug(cc.view_system_config())
