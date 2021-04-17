v9 = 0
v8=":\"AL_RT^L*.?+6/46"
v7 = 'harambe'  #要先反轉 因儲存方式
v6 = 7

flag=''
# ( s[i] != (char)(*((_BYTE *)&v7 + i % v6) ^ v8[i]) )

for i in range(len(v8)):
    flag += chr(ord(v7[i % v6]) ^ ord(v8[i]))
# for i in range(len(v8)):
#     tmp= chr(ord(v7[i % v6]) ^ ord(v8[i]))
#     flag += tmp
#
print(flag)