# -*- encoding:utf-8 -*-

'''
AES算法，密钥（key）长度一般为16,24,32位，密文一般为128位，192位，256位。

'''

from Crypto.Cipher import AES
from Crypto import Random

def encrypt(data, password):
    '''
    AES加密算法

    '''
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    iv = Random.new().read(bs)
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data = cipher.encrypt(pad(data))
    data = iv + data
    return data

def decrypt(data, password):
    '''
    DES解密算法
    '''
    bs = AES.block_size
    if len(data) <= bs:
        return data
    unpad = lambda s : s[0:-ord(s[-1])]
    iv = data[:bs]
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data  = unpad(cipher.decrypt(data[bs:]))
    return data 



	
if __name__ == '__main__':
	data = 'flagadadh121lsf9adad' #要加密的数据
	password = '123456789abcdefg' #16,24,32位长的密码
	encrypt_data = encrypt(data, password)  ##获取加密后的字符串
	print 'encrypt_data:', encrypt_data  #<str>
	
	decrypt_data = decrypt(encrypt_data, password)
	print 'decrypt_data:', decrypt_data  #<str>


    