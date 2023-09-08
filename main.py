# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import cv2 as cv
from selenium import webdriver #导入webdiver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#import requests
driver = webdriver.Chrome('./chromedriver.exe')
#driver = webdriver.Chrome('D:\chromedriver-win64\chromedriver-win64\chromedriver.exe')是可以的
# 这样也可以运行大概率是因为宝宝把exe文件挪到了当前project里面。如果是安装在其他地方，（）里要加什么呢？
# 括号里加exe文件的路径，让webdriver可以找到这个exe并且调用它
driver = webdriver.Chrome()
url = "https://www.taoboa.com"
driver.get(url)
#driver.find_element_by_css_selector('#J_search_key').send_keys("手机")#通过css选择器查找元素
#driver.find_element_by_css_selector("#J_searchForm > input").click()
#跳转网页时
#driver.implicitly_wait(10) #隐式等待，只要数据加载出来就运行     time.sleep(10)——一定需要等待1·0s
#5.获取商品数据信息
#lis = driver.find_elements_by_css_selector("#J_page_search_list_content")  #没有得到数据
#print(lis)
#for li in lis:
  #  title = li.find_element_by_css_selector("#J_page_search_list_content > a:nth-child(3) > div.header > span").text
 #   print(title)

#链接地址：https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/

#代码实现——
# 1、访问网站，将请求参数传进去，请求投（伪装信息）



import requests

params ={
'jsv': '2.5.1',
'appKey': '12574478',
't': '1694012067978',
'sign': 'bef83eb223a8ae56cb843c90aafbc5d5',
'api': 'mtop.alimama.union.xt.en.api.entry',
'v': '1.0',
'AntiCreep': 'true',
'timeout': '20000',
'AntiFlood': 'true',
'type': 'jsonp',
'dataType': 'jsonp',
'callback': 'mtopjsonp2',
'data': '{"pNum":0,"pSize":"60","refpid":"mm_26632258_3504122_32538762","variableMap":"{\"q\":\"手机\",\"navigator\":false,\"clk1\":\"a2838632ebeaf8a1472991df5b4e382b\",\"union_lens\":\"recoveryid:201_33.5.95.74_65365829_1694011997337;prepvid:201_33.5.95.74_65365829_1694011997337\",\"recoveryId\":\"201_33.39.253.94_65370830_1694012067879\"}","qieId":"36308","spm":"a2e0b.20350158.31919782","app_pvid":"201_33.39.253.94_65370830_1694012067879","ctm":"spm-url:a2e0b.20350158.search.1;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E6%2589%258B%25E6%259C%25BA%26clk1%3Da2838632ebeaf8a1472991df5b4e382b%26upsId%3Da2838632ebeaf8a1472991df5b4e382b%26spm%3Da2e0b.20350158.search.1%26pid%3Dmm_26632258_3504122_32538762%26union_lens%3Drecoveryid%253A201_33.5.95.74_65365829_1694011997337%253Bprepvid%253A201_33.5.95.74_65365829_1694011997337"}',
}
url = "https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/"


