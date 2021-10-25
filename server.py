import socket
import response
import sys
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 1337))
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
