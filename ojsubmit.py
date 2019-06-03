#Author: Akshat Chhajer (UG2k18)
#27th March 2019

import getpass
import os
import time
import sys

from selenium import webdriver
from bs4 import BeautifulSoup
from halo import Halo

try:
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--no-sandbox')
    driver = webdriver.Firefox()
    #gecko driver for firefox
except:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome()

url="http://oj.iiit.ac.in/public/login.php"

print("Trying to reach OJ...")

driver.get(url)


if driver.page_source.find('CAS')<1:
    print("Failed to access the IIIT-H network. Check the VPN maybe?")
    sys.exit()

while True:
    try:
        uname=input("CAS Email: ")
        passwd=getpass.getpass("Password: ")
        print("Logging in...")
        driver.get(url)
        driver.find_element_by_name("username").send_keys(uname)
        driver.find_element_by_name("password").send_keys(passwd)
        driver.find_element_by_name("submit").click()

        driver.find_element_by_xpath("//select[@name='cid']/option[last()]").click()
        break
    except:
        print("Invalid Credentials. Try Again!")

while(1):
    driver.refresh()
   
    print()
    soup=BeautifulSoup(driver.page_source, 'lxml')
    oplist=soup.find('select', {'id': "probid"}).findAll('option')
    problems=[]
    for option in oplist: problems.append(option.text)
    problems.pop()
    
    
    progname=input("Question name("+','.join(problems)+"): ")
    path=input("File path: ")
    while True:
        if os.path.exists(path):
            break
        else:
            print("File Not Found. Try Again!")
            path=input("File Path: ")
    
    if path[0]=='~':
        path='/home/'+getpass.getuser()+path[1:]
    ext=path.split('.')[-1]

    os.system('cat '+path+" > "+progname+"."+ext)
    pwd=os.getcwd()
    driver.find_element_by_id("maincode").send_keys(pwd+'/'+progname+'.'+ext)
    driver.find_element_by_name("submit").click()
    Alert=driver.switch_to.alert
    Alert.accept()
    
    status='pending'
    spinner=Halo(text='Pending...\n', spinner='dots', color='cyan', text_color='cyan')
    spinner.start()
    while(status=='pending'):
        driver.refresh()
        soup=BeautifulSoup(driver.page_source,'lxml')
        status=soup.findAll('span')[1].text
        time.sleep(0.25)
    
    spinner.stop()
    if(status=='correct'):
        print("\033[1;32m"+status.upper())
    else:
        print("\033[1;31m"+status.upper())
    
    
    driver.find_element_by_link_text('x').click()    


