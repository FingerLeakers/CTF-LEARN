<<<<<<< HEAD
# -*- coding:utf-8 -*-

'''
@crc32算法

crc算法的结果可以转化为16进制。

'''

import binascii
import datetime

def all_date():
	'''
	获取所有日期
	'''
	result=[]
	begin=datetime.date(1900,1,1) #从1900年1月1日开始
	end=datetime.date(3000,12,6) #到3000年12月6日结束

	delta=datetime.timedelta(days=1)
	d=begin

	while d<=end:
		date=d.strftime("%Y%m%d")
		d+=delta
		result.append(date)

	return result


def _crc32(content): 
  """ 
	crc32解密
  """
  return '%x' % (binascii.crc32(content) & 0xffffffff) #取crc32的八位数据 %x返回16进制



if __name__=="__main__":

	result=all_date()

	for i in result:
		'''
		遍历每一个日期，暴力破解出密文结果
		'''
		tag=_crc32(i)

		if tag=="4d1fae0b":  ##16进制密文
=======
# -*- coding:utf-8 -*-

'''
@crc32算法

crc算法的结果可以转化为16进制。

'''

import binascii
import datetime

def all_date():
	'''
	获取所有日期
	'''
	result=[]
	begin=datetime.date(1900,1,1) #从1900年1月1日开始
	end=datetime.date(3000,12,6) #到3000年12月6日结束

	delta=datetime.timedelta(days=1)
	d=begin

	while d<=end:
		date=d.strftime("%Y%m%d")
		d+=delta
		result.append(date)

	return result


def _crc32(content): 
  """ 
	crc32解密
  """
  return '%x' % (binascii.crc32(content) & 0xffffffff) #取crc32的八位数据 %x返回16进制



if __name__=="__main__":

	result=all_date()

	for i in result:
		'''
		遍历每一个日期，暴力破解出密文结果
		'''
		tag=_crc32(i)

		if tag=="4d1fae0b":  ##16进制密文
>>>>>>> 0b9dbfb320a073901bf33fe49fb8fcc85520109c
			print i