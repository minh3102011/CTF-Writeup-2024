encFlag = "MGRL8\x83\x83\x4e\x7b\x4d\x81\x7c\x51\x7f\x7b\x80\x7f\x83\x50\x7b\x50\x51\x7d\x7d\x7f\x51\x7f\x51\x4f\x82\x4d\x7f\x51\x7c\x7e\x7f\x7a\x36"

flag = ""

for i in range(0, len(encFlag)):
    flag += chr((ord(encFlag[i]) - 20) ^ 0x5f)
    
print(flag)