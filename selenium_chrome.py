# encoding: utf-8
import os,sys,time
from pprint import pprint
from selenium import webdriver

br = webdriver.Chrome()

br.get('http://www.jslife.com.cn/jsstApp/index.action')

userinput = br.find_element_by_xpath('//*[@id="frmLogin"]/div/div[3]/div/div[2]/input')
pwdinput = br.find_element_by_xpath('//*[@id="frmLogin"]/div/div[3]/div/div[3]/input')
checkcode = br.find_element_by_xpath('//*[@id="frmLogin"]/div/div[3]/div/div[4]/input')

userinput.send_keys('admin')
pwdinput.send_keys('Ypt@jsstApp0728')
code = input('checkcode: ')

checkcode.send_keys(code)

loginbutton = br.find_element_by_xpath('//*[@id="frmLogin"]/div/div[3]/div/div[5]/input')

loginbutton.click()


with open(r'E:\pyfile\tmpfile\parkNo.txt') as f:
	data = f.readlines()

rows = []
for l in data:
	rows.append(l.split())


br.get('http://www.jslife.com.cn/jsstApp/crm/businesserAction.action')

shopnum = br.find_element_by_xpath('//*[@id="businesserCode"]')
shopnum.send_keys('880075201007846')
submit = br.find_element_by_xpath('//*[@id="searchBtn"]/a')
submit.click()
time.sleep(0.5)
modifybtn = br.find_element_by_xpath('//*[@src="http://www.jslife.com.cn:80/jsstApp/images/edit.gif"]')
modifybtn.click()

daikouframe = br.find_element_by_xpath('/html/body/div[3]/div/iframe')
br.switch_to.frame(daikouframe)

daikou = br.find_element_by_xpath('//*[@id="isSignatoryChecked"]')

br.switch_to.default_content()
closeframe = br.find_element_by_xpath('/html/body/div[3]/table/tbody/tr/td[3]/div')
closeframe.click()

#br.get('http://www.jslife.com.cn/jsstApp/crm/parkCodeManagerAction.action')
#
#print (dir(br))
#
#rows2 = []
#for l in rows:
#	parkinput = br.find_element_by_xpath('//*[@id="code"]')
#	parkinput.clear()
#	parkinput.send_keys(l[2])
#	searchbut = br.find_element_by_xpath('//*[@id="searchBtn"]/a')
#	searchbut.click()
#	time.sleep(0.5)
#	shopNo = br.find_element_by_xpath('//*[@aria-describedby="gridTable_busCode"]')
#	print (shopNo.text)
#	l.append(shopNo.text)
#	rows2.append(l)
#
#pprint (rows2)