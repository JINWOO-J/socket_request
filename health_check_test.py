#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import socket_request
from devtools import debug

socket_address = './data/cli.sock'

cc = socket_request.ControlChain(
    unix_socket=socket_address,
    # cid="0xef17db",
    # debug=True,
    auto_prepare=True,
    wait_state=True,
    # wait_socket=True,
    retry=None
    # check_args=False,
    # increase_sec=2
)


# debug(cc.get_state())
# debug(cc.stop())
# debug(cc.system_config(payload={"key": "rpcIncludeDebug", "value": "true"}))

# debug(cc.view_system_config(detail=True))
#
# while cc.health_check() is False:
#     time.sleep(1)
#     debug(cc.health_check())
#     debug(cc.view_chain())

# debug(cc.health_check())
while cc.health_check().status_code != 200:
    time.sleep(1)
    debug(cc.health_check())


# print("-"* 100)
# debug(cc.view_chain())

# while cc.start():
#     time.sleep(1)
# debug(cc.health_check())

# while cc.start().get('error'):
#     debug(cc.health_check())
#     # debug(cc.stop())
#     time.sleep(1)

# while cc.health_check() is False:
#     debug(f"state = {cc.health_check()}")
#     debug(cc.start())
#     time.sleep(1)

# # while cc.health_check() is False:
# #     debug(f"state = {cc.health_check()}")
# #     time.sleep(1)
# #
# #
# debug(cc.view_chain())
#
