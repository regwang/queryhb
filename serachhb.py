# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

requestCookie={
	"ASP.NET_SessionId":"xrlwk4ox0fyofuzfyufa4azn",
	"hb.website.Mobile":"8ae6d697188c71cc99bdf733813d566d"
}

url=r'http://www.hb56.com/PublicQuery/ConGoodSearch.ashx?type=1'
datas={"cid":"COSU6142624050@0803","method":0,"rdcode":""}
r=requests.post(url,data=datas,cookies=requestCookie).content
soup=BeautifulSoup(r,'html.parser')
print(soup)
