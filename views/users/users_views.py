#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import tornado.web
from tornado.escape import json_decode

from common.commons import(
	http_response,
	)

from conf.base import(
	ERROR_CODE,
	)

class RegistHandle(tornado.web.RequestHandler):
	''' handle /user/regist request
	:param phone: users sign up phone
	:param password:users sign up password
	:param code: users sign up code, must six digital
	'''
	
	def post(self):
		try:
			args = json_decode(self.request.body)
			phone = args['phone']
			password = args['password']
			verify_code = args['code']
		except:
			http_response(self,ERROR_CODE['1001'],1001)
			return
			
		http_response(self,ERROR_CODE['0'],0)