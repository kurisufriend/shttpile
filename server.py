import socket
import response
import sys
import os
_PORT = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bound = False
while not(bound):
    try:
        s.bind(("0.0.0.0", _PORT))
        bound = True
        print("bound to port", _PORT)
    except OSError:
        _PORT += 1
        print("encountered error, trying port", _PORT)
s.listen()
while True:
    c, c_add = s.accept()
    print(c_add)
    raw_req = c.recv(2048).decode("ascii")
    print(raw_req)
    r = response.request.build_response(response.request.parse(raw_req))
    c.sendall(r.text().encode("ascii"))
    c.close()
s.close()
