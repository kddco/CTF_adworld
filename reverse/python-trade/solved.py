import base64

def encode(message):
    s = ''
    for i in message:
        x = ord(i) ^ 32
        x = x + 16
        s += chr(x)

    return base64.b64encode(s)

flag=''
correct = 'XlNkVmtUI1MgXWBZXCFeKY+AaXNt'
flag = base64.b64decode(correct)
print(flag)
for i in flag:
    tmp = chr((i-16) ^ 32)
    print(tmp, end = '')