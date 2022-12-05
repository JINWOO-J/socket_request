#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import sys
parent_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# sys.path.append(parent_dir)
sys.path.insert(0, parent_dir)
import socket_request
# import pandas as pd

from devtools import debug

from tabulate import tabulate

for idx, path in enumerate(sys.path, 1):
    print(f'{idx} - {path}')

print(f'\nrsocket-request module location - {socket_request.__file__}')

# unix_socket = "/var/run/docker.sock"
unix_socket = "data/docker.sock"
docker_socket = socket_request.DockerSock(unix_socket=unix_socket,)
# return_value = docker_socket.get_docker_images(return_type="merge", return_keys=["Id"], simple_name=False)
# return_value = docker_socket.get_docker_images(return_type="merge", simple_name=False)

# debug(return_value)
# res = docker_socket.call_api(
#     url="/images/create?fromImage=ubuntu",
#     method="POST",
#     # payload={
#     #     "Image": "ubuntu",
#     # }
# )

#
# res = docker_socket.call_api(
#     url="/containers/create",
#     method="POST",
#     payload={
#         "Image": "ubuntu",
#         "Name": "ubuntu"
#     }
# )

# debug(res)
while True:
    print(tabulate(docker_socket.get_async_proc()))
