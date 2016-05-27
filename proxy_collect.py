#coding=utf-8

import requests
import re
import time


def clooect_proxy():
	
	url = 'http://www.xicidaili.com/nn/1'

	headers = {
			'Host': 'www.xicidaili.com',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0'
			}

	r = requests.get(url=url, headers=headers)

	ips = re.findall(r'<td>(\d*?\.\d*?\.\d*?\.\d*?)</td>',r.text,re.S)
	https = re.findall(r'<td>(HTTP|HTTPS)</td>',r.text,re.S)
	ports = re.findall(r'<td>(\d*?)</td>',r.text,re.S)

	for (ip,port,http) in zip(ips,ports,https):
		#print ip,port,http
		proxy = {}
		proxy[str(http.lower())]=str('http://'+ip+':'+port)
		check_proxy(proxy)


def check_proxy(proxy):	

	try:
		#print proxy
		time_s = time.time()
		r_bd = requests.get(url='http://1212.ip138.com/ic.asp', proxies=proxy, timeout=6)
		time_e = time.time()
		if r_bd.status_code == 200:
			#print time_e-time_s
			#print r_bd.text
			check_proxy = re.findall(r'\[(.*?)\]',r_bd.text)
			print check_proxy[0]+'\t'+str(time_e-time_s)
			print proxy
	except:
		print 'timeout!'
		pass

def temp():	
	#try:
	proxy = {'HTTP': 'http://111.193.6.70:8888'}
	time_s = time.time()
	r_bd = requests.get(url='http://1212.ip138.com/ic.asp', proxies=proxy, timeout=6)
	time_e = time.time()
	if r_bd.status_code == 200:
		#print time_e-time_s
		#print r_bd.text
		check_proxy = re.findall(r'\[(.*?)\]',r_bd.text)
		print check_proxy[0]+'\t'+str(time_e-time_s)

if __name__ == '__main__':
	clooect_proxy()
	#temp()