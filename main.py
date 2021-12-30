from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import sqlite3

drivePath="C:\\Users\cxz12\Downloads\chromedriver.exe"#chromedriver path

browser=webdriver.Chrome()#open browser
#Login
def login():
    try:
        browser.get('https://webapp.yuntech.edu.tw/YunTechSSO/Account/Login'  ) #login form
        # ------ address and password ------
        username = "B10923057"
        password = "cxz123499"
        # ------ enter address and password ------

        print("[System]",time.strftime(" %I:%M:%S %p",time.localtime())," Login condition prepare function not available please step by")
        elem = browser.find_element_by_id("pLoginName")#login input
        elem.send_keys(username)#key in username
        print("[System]",time.strftime(" %I:%M:%S %p",time.localtime())," type in username OK")
        elem = browser.find_element_by_id("pLoginPassword")#password input
        elem.send_keys(password)        #key in password
        print("[System]",time.strftime(" %I:%M:%S %p",time.localtime())," type in password OK")
        elem.send_keys(Keys.RETURN)
    except Exception as e:
        print(e)
        print("[System]",time.strftime(" %I:%M:%S %p",time.localtime()),"has logined")#login condition
    return True
#DB
def dbloader():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
if __name__ == "__main__":
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    login()
    url="https://webapp.yuntech.edu.tw/eStudent/StuCertificate/"
    browser.get(url)
    addbutton=browser.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_Insert_Button")
    addbutton.click()
    closebutton=browser.find_element_by_css_selector("#CloseButton")
    closebutton.click()
    #----
    browser.get("https://webapp.yuntech.edu.tw/eStudent/StuCertificate/StuCertificate_Edit.aspx?&N")
    select=browser.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_Cer_Name_NoDDL")
    #----
    sel=Select(select).options
    for s in sel:
        #print(s.text)
        print(f'INSERT INTO restfulapi_certification (name) VALUES (\'{s.text}\');')
        #cur.execute(f'INSERT INTO restfulapi_certification (name) VALUES (\"{s.text}\")')
    con.commit()
    con.close()
    print("[System] INFO Program Completes")
