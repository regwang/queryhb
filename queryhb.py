# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

requestCookie={
	"ASP.NET_SessionId":"dz5vvfigkkv2qbdasmc0qjdz",
	"hb.website.Mobile":"8ae6d697188c71cc99bdf733813d566d"
}
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}


s=requests.Session()
s.cookies.update(requestCookie)
s.headers=headers
print(s.headers)
url=r'http://www.hb56.com/PublicQuery/ConGoodSearch.ashx?type=1'

def getOrderData(cid,method=0,rdcode=''):
	datas={"cid":cid,"method":method,"rdcode":rdcode}
	r=s.post(url,data=datas)
	#更新cookie
	if len(r.cookies)>0:
		s.cookies.update(r.cookies)
	print(time.localtime())
	print(s.cookies)	
	soup=BeautifulSoup(r.content,'html.parser')
	print(soup)
	print('-----------------------------------------')
	print()


if __name__=='__main__':
	print('ok')
	while(True):
		getOrderData('COSU6142624050@0803')
		time.sleep(60*10)
else:

	print('not ok')
