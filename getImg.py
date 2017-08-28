# -*- coding:utf-8 -*-
import urllib.request
import time

url=r'http://www.hb56.com/LoginRdCode.aspx'
for i in range(10):
	time.sleep(1)
	urllib.request.urlretrieve(url,r'e:\\python\\queryhb\\oriimg\\{0}.gif'.format(i+1))
	print('{0} is done'.format(i+1))
