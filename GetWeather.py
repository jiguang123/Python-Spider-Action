#coding=utf-8
import sys
import re
import urllib

#reload(sys)
#sys.setdefaultencoding('gbk')

def getHtml(url):
    page = urllib.urlopen(url)
    mybytes = page.read()
    html = mybytes.decode("utf8")
    page.close()
    return html

def getWeather(html):
    reg = r'<a title=.*?>(.*?)</a>.*?'
    reg += r'<img.*?alt="(.*?)".*?'
    reg += r'<img.*?alt="(.*?)".*?'
    reg += r'<span>(.*?)</span>.*?<b>(.*?)</b>'
    weatherList = re.compile(reg).findall(html)
    return weatherList;

weatherList = getWeather(getHtml(r"http://www.weather.com.cn/shanghai/index.shtml"))
for weather in weatherList :
    print("{0} Night:{1} / Day:{2} {3}/{4}".format(weather[0], weather[1], weather[2], weather[3], weather[4]))
