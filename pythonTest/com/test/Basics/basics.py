#!/usr/bin/env python
#coding: utf-8

class A:
	pass

class B(A):
	pass

def run():
	print("hello")
	
	print("----------------------type")
	#数据类型
	a,b,c,d = 1,2,True,4+3j
	print(type(a),type(b),type(c),type(d))
	
	#type()不会认为子类是一种父类类型。
	#isinstance()会认为子类是一种父类类型
	print(isinstance(A(),A))
	print(type(A()) == A)
	print(isinstance(B(),A))
	print(type(B()) == A)
	
	print("----------------------string")
	#String参数值不可变
	str = 'Runoob'
	print(str)  # 输出字符串
	print(str[1] + '1')  # 输出字符串
	print(str[0:-1])  # 输出第一个个到倒数第二个的所有字符
	print(str[0])  # 输出字符串第一个字符
	print(str[2:5])  # 输出从第三个开始到第五个的字符
	print(str[2:])  # 输出从第三个开始的后的所有字符
	print(str * 2)  # 输出字符串两次
	print(str + "TEST")  # 连接字符串
	
	print("----------------------list")
	#list中参数可变
	list = ['abcd', 786, 2.23, 'runoob', 70.2]
	tinylist = [123, 'runoob']
	list[2] = 223
	print(list)  # 输出完整列表
	print(list[0])  # 输出列表第一个元素
	print(list[1:3])  # 从第二个开始输出到第三个元素
	print(list[2:])  # 输出从第三个元素开始的所有元素
	print(tinylist * 2)  # 输出两次列表
	print(list + tinylist)  # 连接列表
	
	print("----------------------tuple")
	#tuple中元素不可变
	tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
	tinytuple = (123, 'runoob')
	print(tuple)  # 输出完整元组
	print(tuple[0])  # 输出元组的第一个元素
	print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
	print(tuple[2:])  # 输出从第三个元素开始的所有元素
	print(tinytuple * 2)  # 输出两次元组
	print(tuple + tinytuple)  # 连接元组
	
	print("----------------------set")
	#set无序不重复
	student = ({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'})
	print(student)  # 输出集合，重复的元素被自动去掉
	# 成员测试
	if ('Rose' in student):
		print('Rose 在集合中')
	else:
		print('Rose 不在集合中')
	
	# set可以进行集合运算
	a = set('abracadabra')
	b = set('alacazam')
	print(a)
	print(a - b)  # a和b的差集
	print(a | b)  # a和b的并集
	print(a & b)  # a和b的交集
	print(a ^ b)  # a和b中不同时存在的元素
	
	print("----------------------Dictionary（字典）")
	dict = {}
	dict['one'] = "1 - 菜鸟教程"
	dict[2] = "2 - 菜鸟工具"
	tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
	print(dict['one'])  # 输出键为 'one' 的值
	print(dict[2])  # 输出键为 2 的值
	print(tinydict)  # 输出完整的字典
	print(tinydict.keys())  # 输出所有键
	print(tinydict.values())  # 输出所有值
	
	#while
	a, b = 0, 1
	while b < 10:
		print(b)
		a, b = b, a + b

if __name__ == "__main__":
	run()