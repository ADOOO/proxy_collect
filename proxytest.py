#coding=utf-8

import requests
import re
import time

proxies = {'http': 'http://223.13.86.170:8118'}

rk = 'http://www.rkpass.cn/u.jsp?u=299602'
rk_headers = {
      'Host': 'www.rkpass.cn',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
      'Accept-Encoding': 'gzip, deflate',
      'Connection': 'keep-alive',
      }


try:
  time_s = time.time()
  r_bd = requests.get(url='http://1212.ip138.com/ic.asp', proxies=proxies, timeout=15)
  r_rk = requests.get(url=rk, headers=rk_headers, proxies=proxy, timeout=6)
  time_e = time.time()
  if r_bd.status_code == 200:
  #print r.text
    print r_rk.status_code
    print time_e-time_s
    #print r_bd.text
    check_proxy_pattern = re.compile('\[(.*?)\]')
    check_proxy = check_proxy_pattern.findall(r_bd.text)
    print check_proxy[0]
except:
  print 'timeout!'
  pass