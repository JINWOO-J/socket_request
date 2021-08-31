# socket_request

socket_request is build and parses HTTP requests with unix domain sockets.

### Installing socket_reuquest

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
