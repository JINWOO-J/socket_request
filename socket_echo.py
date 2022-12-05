import socket, os

def main():
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        os.remove("/tmp/socketname")
    except OSError:
        pass
    s.bind("/tmp/socketname")
    s.listen(1)
    conn, addr = s.accept()
    while 1:
        data = conn.recv(1024)
        print(data)
        request = data.strip().decode("utf-8").split("\r\n")
        print(request)
        if not data:
            break

        conn.send(data)
    conn.close()


if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            print(f"error => {e}")
