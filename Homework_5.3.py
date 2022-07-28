# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rleEncode (text):
    if text == "":
        return ""
    enc = []
    len = 1
    for i in range (1, len(text)):
        if text [i] == text [i-1]:
            len +=1
        else:
            enc.extend([str(len), str(text[i-1])])
            len = 1
    enc.extend([str(len), str(text[-1])])
    return "".join(enc)

def rleDecode (text):
    if text == "":
        return ""
    dec = []
    len = 0
    for ch in text:
        if ch.num():
            len = 10* len + int(ch)
        else: 
            dec.append(len*ch)
            len = 0
    return "".join(dec)



resEn = rleEncode ("aaafffrrrrkkfssfkasdddddd")
print(resEn)
resDec = rleDecode (resEn)
print(resDec)