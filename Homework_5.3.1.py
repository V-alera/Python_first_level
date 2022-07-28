# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def inputText():
    textIn = input("Введите текст для проверки сжатия: ")
    return textIn


def encode (text):
    res = ""
    ch = ""
    runLength = 0

    for i in range(len(text)):
        if i == 0: 
            ch = text[i]
            runLength = 1
        else: 
            curCh = text[i]
            if curCh == ch:
                runLength += 1

            else:
                res += ch + str(runLength)
                ch = curCh
                runLength = 1
    res += ch + str(runLength)
    return res

def decode (text):
    res = ""
    for i in range (0, len(text), 2):
        ch = text[i]
        runLength = int(text[i+1])
        for j in range(runLength):
            res += ch
    return res

def printRes(txt):
    print(f"Результат декомпрессии: {txt}", end=' ')



originalText = inputText ()
encText = encode (originalText)
printRes(encText)
print()
decText = decode (encText)
printRes(decText)