#https://chromedriver.chromium.org/downloads
# pip install bs4
#pip install
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import os,random,sys,time
from selenium import webdriver
import pandas as pd
from time import time
#setting path for chromedriver
path= "../chromedriver.exe"
#reading config.txt
user=input("Please enter the e-mail id of linkdin")
password=input("Please enter the password")
#setting which browser to use
#setting which browser to use
import timeit
import time
start = timeit.default_timer()
browser=webdriver.Chrome(path)
url="https://www.linkedin.com/login?"
browser.get(url) #open the site in chrome
elementID=browser.find_element_by_id("username")
elementID.send_keys(user) #login here
elementID=browser.find_element_by_id("password")
elementID.send_keys(password)
elementID.submit()
profileID="https://www.linkedin.com/in/oleksandra-yelizarova/detail/recent-activity/shares/"
browser.get(profileID)
flag=1
while flag:
    try:
        new = browser.execute_script("return document.body.scrollHeight")
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(7)
        last_height = browser.execute_script("return document.body.scrollHeight")
        content=browser.page_source
        if(last_height==new):
            flag=0
    except:
        flag=0
        print("Error occured while scrolling. Please re-try again")
stop = timeit.default_timer()
print(stop-start)
soup=BeautifulSoup(content,'html.parser')
container=soup.find_all('div',{'class':'occludable-update ember-view'})
def getPost(container):
    post = []
    for i in range(len(container)):
        try:
            p = container[i].find_all('span', {'class': 'break-words'})[0].span.span.text
            post.append(p)
        except:
            try:
                ip = container[i].find_all('span', {'class': 'break-words'})[0].span.text
                post.append(ip)
            except:
                pass
    return post
#for tag
def getTag(text):
    tag = []
    tags=' '
    for t in text:
        words=t.split()
        for word in words:
            if word.startswith('#'):
                tags=tags+word+' '
        tag.append(tags)
        tags=''
    return tag
def getImage(container):
    img = []
    for i in range(len(container)):
        try:
            src = container[i].find_all('img', {
                'class': "ivm-view-attr__img--centered feed-shared-image__image feed-shared-image__image--constrained lazy-image ember-view"})[
                0]['src']
            img.append(src)
        except:
            try:
                src = container[i].find_all('img', {
                    'class': "ivm-view-attr__img--centered feed-shared-image__image lazy-image ember-view"})[0]['src']
                img.append(src)
            except:
                img.append('')
    return img
post=getPost(container)
tag=getTag(post)
img=getImage(container)
#try
h=max([len(post),len(tag),len(img)])
#padding
for i in range(h-len(post)):
    print("post")
    post.append('')
for i in range(h-len(tag)):
    print("tag")
    tag.append(' ')
for i in range(h-len(img)):
    print("img")
    img.append(' ')
Profile_Content={}
Profile_Content={'Post':post,'Image':img,'Tag':tag}
linkdin_dataframe=pd.DataFrame(Profile_Content)
linkdin_dataframe.to_csv("LinkedinUpwork.csv",index=False)