# socket_request

socket_request is build and parses HTTP requests with unix domain sockets.

### Installing socket_request

socket_request is available on PyPI:

```
pip3 install socket-request

```
Officially supports Python 3.7+.



### Examples:

```python
import socket_request

docker = socket_request.DockerSock(unix_socket="/var/run/docker.sock")
docker.get_docker_images()

```


```python
import socket_request

control_chain = socket_request.ControlChain(unix_socket="./cli.sock")
control_chain.stop()
control_chain.start()

```

## CLI:
$ control_chain --help
```angular2html

    ╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋╋┏┓╋╋╋╋┏┓
    ╋╋╋╋╋╋╋╋┏┛┗┓╋╋╋╋┃┃╋╋╋╋┃┃
    ┏━━┳━━┳━╋┓┏╋━┳━━┫┃╋┏━━┫┗━┳━━┳┳━┓
    ┃┏━┫┏┓┃┏┓┫┃┃┏┫┏┓┃┃╋┃┏━┫┏┓┃┏┓┣┫┏┓┓
    ┃┗━┫┗┛┃┃┃┃┗┫┃┃┗┛┃┗┓┃┗━┫┃┃┃┏┓┃┃┃┃┃
    ┗━━┻━━┻┛┗┻━┻┛┗━━┻━┛┗━━┻┛┗┻┛┗┻┻┛┗┛

	 version : 1.0.11
	 base_dir: /app/icon2-node


usage: control_chain [-h] [-s unixsocket] [-d] [-t timeout] [-w wait_state]
                     [-r retry] [-ws] [-ap auto_prepare] [-p payload_file]
                     [-f] [-i] [--seedAddress SEEDADDRESS] [-b BASE_DIR]
                     [-pd payload dict]
                     {start,stop,reset,leave,view_chain,join,import_icon,import_finish,backup,restore,chain_config,ls}

Command Line Interface for control_chain

positional arguments:
  {start,stop,reset,leave,view_chain,join,import_icon,import_finish,backup,restore,chain_config,ls}

optional arguments:
  -h, --help            show this help message and exit
  -s unixsocket, --unixsocket unixsocket
                        unix domain socket path (default:
                        /app/icon2-node/data/cli.socket)
  -d, --debug           debug mode. (default: False)
  -t timeout, --timeout timeout
                        timeout (default: 60)
  -w wait_state, --wait-state wait_state
                        wait_state (default: True)
  -r retry, --retry retry
                        wait_state (default: True)
  -ws, --wait-socket    wait for unix domain socket
  -ap auto_prepare, --auto_prepare auto_prepare
                        auto_prepare (default: True)
  -p payload_file, --payload payload_file
                        payload file
  -f, --forever         retry forever
  -i, --inspect         inspect for view chain
  --seedAddress SEEDADDRESS
                        seed list string
  -b BASE_DIR, --base-dir BASE_DIR
                        base dir for goloop
  -pd payload dict, --payload-dict payload dict
                        payload dict
```


## ConnectSock
- ConnectSock class
- request(self, method="GET", url=None, headers={}, payload={}, files={}, return_dict=False) method

## ControlChain
Parent class is ConnectSock class
- ControlChain class
- start() method
- stop() method
- reset() method
- leave() method
- backup() method
- backup_list() method
- restore(name="name") method
- join(seed_list=["127.0.0.1:7100"], role=3) method
- view_chain(detail=False, inspect=False) method
- chain_config(payload={"key": "autoStart", "value": "true"}) method
- view_system_config() method
- system_config(payload={"key": "rpcIncludeDebug", "value": "true"}) method


## DockerSock
Parent class is ConnectSock class
- DockerSock class
