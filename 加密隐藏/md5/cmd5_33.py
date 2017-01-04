<<<<<<< HEAD
# -*- coding:utf-8 -*-


'''
CMD5加密

@By nMask 2016.12.6

一般md5的密文为16或者32位长度的字符串。

本脚本为，从33位加密的密文中，遍历删除一位长度，然后用md5解密。

@解密网站：http://www.cmd5.com/b.aspx


'''

string="cca9cc444e64c8116a30la00559c042b4"
string=list(string)


for i in range(len(string)):
	'''
	遍历删除一位，然后将字符串放入cmd5网站，批量解密。
	'''
	result=string[:] ##复制一个列表，不会改变原列表。
	result.pop(i)
	
	print "".join(result)


=======
# -*- coding:utf-8 -*-


'''
CMD5加密

@By nMask 2016.12.6

一般md5的密文为16或者32位长度的字符串。

本脚本为，从33位加密的密文中，遍历删除一位长度，然后用md5解密。

@解密网站：http://www.cmd5.com/b.aspx


'''

string="cca9cc444e64c8116a30la00559c042b4"
string=list(string)


for i in range(len(string)):
	'''
	遍历删除一位，然后将字符串放入cmd5网站，批量解密。
	'''
	result=string[:] ##复制一个列表，不会改变原列表。
	result.pop(i)
	
	print "".join(result)


>>>>>>> 0b9dbfb320a073901bf33fe49fb8fcc85520109c
