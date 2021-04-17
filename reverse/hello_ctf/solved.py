# 模擬程式邏輯 v13轉成文字就能得到flag
v13 = "437261636b4d654a757374466f7246756e"
v4 = 0
v8 = 0
v10 = 0
while 1:
    v11 = 0
    v12 = 0
    v9 = input("input flag: ")
    if (len(v9)>17):
        break
    v3 = 0
    while 1:  # 模擬do while
        v4 = v9[v3]
        if not v4:
            break
        v8 = hex(v4)
        v10 = v10 + v8
        ++v3
        if (v3 >17):
            break
    if (v10 == v13):
        print(v3)
    else:
        print("error")




