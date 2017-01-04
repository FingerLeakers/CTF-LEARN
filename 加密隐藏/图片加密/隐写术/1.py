from PIL import Image  
  
def makeImageEven(image):  
    pixels = list(image.getdata())  
    evenPixels = [(r>>1<<1,g>>1<<1,b>>1<<1,t>>1<<1) for [r,g,b,t] in pixels]  
    evenIMG = Image.new(image.mode,image.size)  
    evenIMG.putdata(evenPixels)  
    return evenIMG  
  
  
def encodeDataInImage(image,data):  
    evenIMG = makeImageEven(image)  
    binary = ''.join(map(constLen,bytearray(data,'utf-8')))  
    evenPixels = list(evenIMG.getdata())  
    if len(binary) > len(evenPixels)*4:  
        raise Exception("Error:cannot conver data coded larger than"+len(evenPixels)*4+4)  
    encodedPixels = [(r+int(binary[index*4+0]),g+int(binary[index*4+1]),b+int(binary[index*4+2]),t+int(binary[index*4+3])) if index*4 < len(binary) else (r,g,b,t) for index,(r,g,b,t) in enumerate(evenPixels)]  
    encodedIMG = Image.new(image.mode,image.size)  
    encodedIMG.putdata(encodedPixels)  
    return encodedIMG  
  
def constLen(int):  
    binary = '0'*(8-(len(bin(int))-2))+bin(int).replace('0b','') # 8 bit lenth with front 0s  
    return binary # the zero can be deleted later, which won't effect the result  
  
  
def BinaryToString(binary):  
    index = 0  
    string = []  
    rec = lambda x, i: x[2:8] + (rec(x[8:], i-1) if i > 1 else '') if x else ''  
    # rec = lambda x, i: x and (x[2:8] + (i > 1 and rec(x[8:], i-1) or '')) or ''  
    fun = lambda x, i: x[i+1:8] + rec(x[8:], i-1)  
    while index + 1 < len(binary):  
        chartype = binary[index:].index('0')  
        length = chartype*8 if chartype else 8  
        string.append(chr(int(fun(binary[index:index+length],chartype),2)))  
        index += length  
    return ''.join(string)  
  
  
  
def decodeImage(image):  
    pixels = list(image.getdata())  
    binary = ''.join([str(r%2)+str(g%2)+str(int(b%2))+str(int(t%2)) for (r,g,b,t) in pixels])  
    location_END = binary.find('0000000000000000')  
    if location_END % 8 == 0 :  
        End_Index = location_END  
    else:  
        End_Index = location_END + (8 - location_END % 8)  
    data = BinaryToString(binary[:End_Index])  
    return data  
  
  
  
  
if __name__ == '__main__':    
    # IMGname = raw_input("IMG name:")  
    IMGname='2.png'  
    IMG = Image.open(IMGname)  
    # data = raw_input("the data:")  
    # data='asdasdasd'  
    # encodedIMG = encodeDataInImage(IMG,data)  
    # encodedIMG.save('encoded'+IMGname)  
    print decodeImage(IMG)  