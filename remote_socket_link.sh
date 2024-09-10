#!/bin/bash

#REMOTE_IP="20.20.5.170"
#REMOTE_IP="20.20.6.76"
#REMOTE_IP="20.20.6.78"
#REMOTE_IP="20.20.1.65"
#REMOTE_IP="20.20.6.97"
#REMOTE_IP="20.20.1.167"
#REMOTE_IP="100.106.142.90"
#REMOTE_IP="20.20.4.132"

REMOTE_IP="100.83.246.68"

LOCAL_SOCKET_FILE="${PWD}/data/cli.sock"
#REMOTE_SOCKET_FILE="/app/icon2-node/data/cli.sock"
#REMOTE_SOCKET_FILE="/app/goloop/data/cli.sock"
#REMOTE_SOCKET_FILE="/app/havah-chain-node-docker/test_data/cli.sock"
#REMOTE_SOCKET_FILE="/app/havah_cc_test/data/cli.sock"
#REMOTE_SOCKET_FILE="/app/goloop/data/cli.sock"

REMOTE_SOCKET_FILE="/app/havah-chain-node-docker/local/data/cli.sock"

echo "LOCAL_SOCKET_FILE: ${LOCAL_SOCKET_FILE} -> REMOTE_IP ${REMOTE_IP}:${REMOTE_SOCKET_FILE}"
rm -rf ${LOCAL_SOCKET_FILE}

socat "UNIX-LISTEN:${LOCAL_SOCKET_FILE},reuseaddr,fork" EXEC:"ssh root@${REMOTE_IP} socat STDIO UNIX-CONNECT\:${REMOTE_SOCKET_FILE}"

