
import struct

fBuff = [1.1, 15.2, 255.8, 69.2]

def floatArr2HexStr(buff):
    s = str()
    for x in fBuff:
        ba = bytearray(struct.pack("f", x))
        for o in ba:
            s += "\\x" + format(o , "02x") 


    print(s)
    return s


def hexStr2FloatArr(s):
    valArr = s.split("\\x")
    valArr.remove('')
    print(valArr)
    numList = list()
    for i in range(len(fBuff)):
        numList.append(str(valArr[0+i*4] + valArr[1+i*4] + valArr[2+i*4] + valArr[3+i*4]))

    print(numList)


    floatOut = list()
    for n in numList:
        x = struct.unpack("f", bytes.fromhex(n))[0]
        floatOut.append(round(x, 2))

    print(floatOut)


hexStr2FloatArr( "\\xac\\x4a\\x3a\\x3e\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x2e\\x64\\x42\\x3e")