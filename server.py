import socket
import response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 1337))
s.listen()
while True:
    c, c_add = s.accept()
    print(c_add)
    print(c.recv(1024).decode("ascii"))
    r = response.request.build_response("body.html")
    c.sendall(r.text().encode("ascii"))
    c.close()
s.close()
