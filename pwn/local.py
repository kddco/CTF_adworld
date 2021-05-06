sh  =  process ( './pwn_test' ) 
sh.recvuntil("input magic number")
sh.send(0)
sh.recvuntil("try harder")
sh.send(10)

#test