#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import json
def http_response(self,msg,code):
	self.write(json.dumps({"data":{"msg":msg,"code":code}}))
	
if __name__ == "__main__":
	http_response()
	