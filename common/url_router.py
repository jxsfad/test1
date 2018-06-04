#!/usr/bin/python3
#_*_ coding:utf-8 _*_
from __future__ import unicode_literals
from importlib import import_module

def include(module):
	'''根据传入的字符串，调用相应的模块，如module为字符串regist时，
	调用view.users.users_view.RegistHandle模块
	'''
	res = import_module(module)
	urls = getattr(res,'urls',res)
	return urls

def url_wrapper(urls):
	'''拼接请求url,调用对应的模块，如拼接users和regist 成url /users/regist,
	调用views.users.users_view.RegistHandle模块
	'''
	wrapper_list = []
	for url in urls:
		path,handles = url
		if isinstance(handles,(tuple,list)):
			for handle in handles:
				pattern,handle_class = handle
				wrap = ('{0}{1}'.format(path,pattern),handle_class)
				wrapper_list.append(wrap)
		else :
			wrapper_list.append((path, handles))
	return wrapper_list
		