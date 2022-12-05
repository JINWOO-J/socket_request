#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import sys
parent_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# sys.path.append(parent_dir)
sys.path.insert(0, parent_dir)
from devtools import debug
import socket_request

for idx, path in enumerate(sys.path, 1):
    print(f'{idx} - {path}')

print(f'\n socket-request module location - {socket_request.__file__}')

# unix_socket = "/var/run/docker.sock"
unix_socket = "data/docker.sock"
docker_socket = socket_request.DockerSock(unix_socket=unix_socket,)

res1 = docker_socket.get_containers()
debug(res1)

res2 = docker_socket.get_docker_images()
debug(res2)
