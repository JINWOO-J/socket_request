#!/bin/bash

#REMOTE_IP="20.20.5.170"
#REMOTE_IP="20.20.6.76"
#REMOTE_IP="20.20.6.78"
REMOTE_IP="20.20.5.169"
#REMOTE_IP="20.20.1.167"
LOCAL_SOCKET_FILE="${PWD}/data/cli.sock"
#REMOTE_SOCKET_FILE="/app/icon2-node/data/cli.sock"
REMOTE_SOCKET_FILE="/app/goloop/data/cli.sock"

rm -rf ${LOCAL_SOCKET_FILE}

socat "UNIX-LISTEN:${LOCAL_SOCKET_FILE},reuseaddr,fork" EXEC:"ssh root@${REMOTE_IP} socat STDIO UNIX-CONNECT\:${REMOTE_SOCKET_FILE}"

