# -*- coding:utf-8 -*-

import base64
import json

from Crypto.Cipher import DES

class Crypt(object):
    """加密和解密工具类"""
    des_key = "12345678"
    block_size = DES.block_size  
    pad_str = ['\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08']

    @classmethod
    def des_base64_encrypt(cls, reqdata):
        """ 基于DES和base64的加密算法
            @:param reqdata 需要加密的请求数据           
        """
        key = cls.des_key
        length = len(reqdata)
        if length < cls.block_size:
            add = cls.block_size - length
        elif length > cls.block_size:
            add = cls.block_size - (length % cls.block_size)
        else:
            add = 8

        reqdata = reqdata + (cls.pad_str[add-1] * add)
        des = DES.new(key, DES.MODE_ECB)
        encrypt_data = des.encrypt(reqdata)

        return base64.b64encode(encrypt_data)


    @classmethod
    def des_base64_decrypt(cls, retdata):
        """DES解密
            @:param retdata: lakala reponse retData
        """
        key = cls.des_key
        debase64_data = base64.b64decode(retdata)
        des = DES.new(key, DES.MODE_ECB)
        decrypt_data = des.decrypt(debase64_data)
        
        return decrypt_data