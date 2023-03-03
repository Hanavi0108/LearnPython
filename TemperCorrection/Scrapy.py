"""
-------------------------------------------------
   File Name：     Scrapy
   Description :
   Author :       Hanavi
   date：          2023/2/12
-------------------------------------------------
   Change Activity:
                   2023/2/12:
-------------------------------------------------
"""
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)

print(resp.read().decode("utf-8"))

with open("mybaidu.html", mode="w") as f:
    f.write(resp.read().decode("utf-8"))


print('over!')