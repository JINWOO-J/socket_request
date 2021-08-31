#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
import os
import json
import socket_request
import re

sys.path.append('../common')
import base

from devtools import debug

socket_address = './test_socket.sock'
# socket_address = '/Users/jinwoo/work/icon/icon2-node/src/jinwoo/test_socket.sock'

# Make sure the socket does not already exist
try:
    os.unlink(socket_address)
except OSError:
    if os.path.exists(socket_address):
        print("Error")
        raise


def handle_response():
    # Listens on an abstract namespace socket and sends one HTTP response
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(socket_address)

    while True:
        sock.listen(1)
        print(f"[server] Listening socket -> {socket_address}")
        client_sock, addr = sock.accept()
        data = client_sock.recv(1024)
        request = data.strip().decode("utf-8").split("\r\n")

        tokens = request[0].split()
        body = request[-1]

        headers = {}
        for idx, req in enumerate(request):
            if idx != 0 and req != body:
                debug(f"header: ", req)
                req_list = req.strip().split(":")
                if len(req_list) > 1:
                    headers[req_list[0].strip()] = req_list[1].strip()

        debug("[server]", headers)

        print(f"[server] data = {data}")
        debug(f"[server] tokens =", tokens)

        method = tokens[0].upper()
        url = tokens[1].lower()
        http_version = tokens[2].upper()

        print(f"[server] {method} , {url}, {http_version}")
        response_dict = {
            "method": method,
            "url": url,
            "http_version": http_version,
            "header": headers,
            "body": body,

        }

        # body = data.strip().split('H')


        client_sock.sendall(f'{http_version} 200 OK\r\n'.encode('utf-8'))
        # client_sock.sendall(b'Content-Type: text/plain\r\n\r\n')
        client_sock.sendall(b'Content-Type: application/json\r\n\r\n')
        client_sock.sendall(f'{json.dumps(response_dict)}'.encode("utf-8"))

        # client_sock.sendall(b'HTTP/1.0 200 OK\r\n')
        # client_sock.sendall(b'Content-Type: text/plain\r\n\r\n')
        # client_sock.sendall(b'Hello world!')

        client_sock.close()


# print(f"{socket_address} = {os.path.exists(socket_address)}, {os.path.isfile(socket_address)}")
# res = socket_request.ConnectSock(unix_socket=socket_address)
# print(res.text)
#
# exit()

pid = os.fork()


if pid:
    handle_response()
    pid, status = os.wait()
    print(f"[server] pid={pid}, status={status}")
else:

    print(f"{socket_address} = {os.path.exists(socket_address)}, {os.path.isfile(socket_address)}")
    res = socket_request.ConnectSock(unix_socket=socket_address)\
        .request(
        method="GET",
        url="/",
        headers={
            "content-Type": "text/plain",
            "User-Agent": "socket-request"
        },
        payload={
            "key": "value"
        }
    )
    debug("[client] response", res.get_json())

    # res = socket_request.ConnectSock(unix_socket=socket_address).request(method="POST", url="/")
    # base.dump(res)

# else:
#     print(f"{socket_address} = {os.path.exists(socket_address)}, {os.path.isfile(socket_address)}")
#     res = socket_request.ConnectSock(unix_socket=socket_address)
#     print(res)


exit()
if os.fork() == 0:        # child
    # session = requests_unixsocket.Session()
    # res = session.get('http+unix://\0test_socket/get')
    print(f"{socket_address} = {os.path.exists(socket_address)}, {os.path.isfile(socket_address)}")
    res = socket_request.ConnectSock(unix_socket=socket_address)
    print(res)

else:                     # parent
    try:
        handle_response()

    finally:
        os.wait()


