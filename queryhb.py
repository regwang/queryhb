# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

requestCookie={
	"ASP.NET_SessionId":"xrlwk4ox0fyofuzfyufa4azn",
	"hb.website.Mobile":"8ae6d697188c71cc99bdf733813d566d"
}


s=requests.session()
url=r'http://www.hb56.com/PublicQuery/ConGoodSearch.ashx?type=1'

def getOrderData(cid,method=0,rdcode=''):
	datas={"cid":cid,"method":method,"rdcode":rdcode}
	r=s.post(url,data=datas,cookies=requestCookie)
	soup=BeautifulSoup(r.content,'html.parser')
	print(soup)


if __name__=='__main__':

	print('ok')
else:

	print('not ok')
