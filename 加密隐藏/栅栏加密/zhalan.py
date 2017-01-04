<<<<<<< HEAD
# -*- coding:utf-8 -*-

'''
***栅栏加密方法***

加密方法自行百度，解密方法如下：

例子：adaufdns p

先计算密文的长度，如长度为10(空格也算)，因为每行的字符串数量一样，因此这里要么是分为5行，要么就是2行。
假设是分为2行，则每5个为一行分开：
adauf（前5）
dns p（后5）

再将每行首字符合并：
答案：addnasu fp

多行的话也是一样

@By nmask	2016.12.6

'''

string="tn c0afsiwal kes,hwit1r  g,npt  ttessfu}ua u  hmqik e {m,  n huiouosarwCniibecesnren."
string=list(string)
print 'String len is :',len(string)    ##字符串总长度

result=[]
answer=""
i=17 ##因为长度为85，因此这里写17或者5

def split_list(st):
	'''
	将密文字符串分隔成多行，每行的数量一样。
	'''
	st1=st[0:i]
	result.append(st1)
	for j in range(len(st)/i-1):
		sts=st[i*(j+1):i*(j+2)]
		result.append(sts)

	return result


if __name__=="__main__":

	result=split_list(string)

	'''
	将每行的首字符相组合
	'''

	for m in range(i):
		sums=""
		for n in result:
			sums=sums+n[m]

		answer+=sums

=======
# -*- coding:utf-8 -*-

'''
***栅栏加密方法***

加密方法自行百度，解密方法如下：

例子：adaufdns p

先计算密文的长度，如长度为10(空格也算)，因为每行的字符串数量一样，因此这里要么是分为5行，要么就是2行。
假设是分为2行，则每5个为一行分开：
adauf（前5）
dns p（后5）

再将每行首字符合并：
答案：addnasu fp

多行的话也是一样

@By nmask	2016.12.6

'''

string="tn c0afsiwal kes,hwit1r  g,npt  ttessfu}ua u  hmqik e {m,  n huiouosarwCniibecesnren."
string=list(string)
print 'String len is :',len(string)    ##字符串总长度

result=[]
answer=""
i=17 ##因为长度为85，因此这里写17或者5

def split_list(st):
	'''
	将密文字符串分隔成多行，每行的数量一样。
	'''
	st1=st[0:i]
	result.append(st1)
	for j in range(len(st)/i-1):
		sts=st[i*(j+1):i*(j+2)]
		result.append(sts)

	return result


if __name__=="__main__":

	result=split_list(string)

	'''
	将每行的首字符相组合
	'''

	for m in range(i):
		sums=""
		for n in result:
			sums=sums+n[m]

		answer+=sums

>>>>>>> 0b9dbfb320a073901bf33fe49fb8fcc85520109c
	print answer