# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:40:17 2021

@author: omarkhattab
@email: omarkhattab256@gmail.com
"""

file1= open("login.txt","r+")
s = file1.readlines()
if s:
  #  s= s.split('\n')
    usr =  s[0].split('\n')[0]
    pw = s[1]
else:
    usr = input("Enter username: ")
    pw = input("Enter password: ")
    L = [usr , '\n', pw]
    file1.writelines(L) 

print(usr,pw)
file1.close()

# ==============(1) IMPORTS ===========
from selenium import webdriver
import time

def scroll(element):
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = driver.execute_script('return window.innerHeight')
        window_y = driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y
        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by) 


# ==============(2) Connect to Chrome ===========
web = webdriver.Chrome("chromedriver.exe")  # Optional argument, if not specified will search path.
driver = web


# ============= Main Function ===========

web.get('http://apps.iti.gov.eg/ManagementSystem/Student/CourseEval.aspx')
time.sleep(1) #Delay to load the page

username = web.find_element_by_id('txtUsername')
username.send_keys(usr)
username.click()

password = web.find_element_by_id('txtpassword')
password.send_keys(pw)
password.click()

submitbtn = web.find_element_by_id('btnlogin')
submitbtn.click()

print("Logged in successfully")
time.sleep(2) #Delay to load the page
select = driver.find_element_by_id('ContentPlaceHolder1_UcCourseEval1_ddlCourseName_chzn')
select.click()
select2 =driver.find_element_by_id('ContentPlaceHolder1_UcCourseEval1_ddlCourseName_chzn_o_1')
select2.click() 

courseName = web.find_element_by_xpath('//*[@id="uniform-ContentPlaceHolder1_UcCourseEval1_ddlCourseName"]/span').get_attribute('innerHTML')
print('Course name: ' + courseName + '\n')


input("Press enter when the page is fully loaded and you can see the rating stars: ")
time.sleep(4) #Delay to load the page

choice = 5
alltest = driver.find_elements_by_xpath("//a[@style='text-decoration:none']")
for p in alltest:
    r = p.find_elements_by_xpath("*")
    scroll(r[choice-1])
    r[choice-1].click()
    
print("Added all ratings")

time.sleep(2) #Delay to load the page
comment1 = "The course was great and very useful"
comment2 = "Instructor was helpful and very cooperative"
try:
    courseComment = driver.find_element_by_id('ContentPlaceHolder1_UcCourseEval1_txtCourseComment')
    instComment = driver.find_element_by_id('ContentPlaceHolder1_UcCourseEval1_txtLectureInstructorComment')
    scroll(courseComment)
    scroll(instComment)
    courseComment.click()
    instComment.click()
    courseComment.send_keys(comment1)
    instComment.send_keys(comment2)
    
    print("Added comments")
except:
    print("Cannot find comment placeholders")


# instructorsTable = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_UcCourseEval1_DataListLectureEval"]/tbody').find_elements_by_xpath("*")
# icount = len(instructorsTable)


# for i in instructorsTable:
#     questions1 = i.find_element_by_xpath('./td/div/table/tbody').find_elements_by_xpath("*")
#     del questions1[0]
#     print(len(questions1))
    
#     for j in questions1:
#         ratings1 = j.find_element_by_xpath('./td[2]/div/a').find_elements_by_xpath("*")
#         print(len(ratings1))
#         ratings1[choice-1].click()
        

# labsTable = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_UcCourseEval1_GrdViewcourseEval"]/tbody').find_elements_by_xpath("*")
# del labsTable[0]
# labcount = len(labsTable)

# for j in labsTable:
#     ratings2 = j.find_element_by_xpath('./td[2]/div/a').find_elements_by_xpath("*")
#     print(len(ratings2))
#     ratings2[choice-1].click()

# for i in labsTable:
#     questions2 = i.find_element_by_xpath('./td/div/table/tbody').find_elements_by_xpath("*")
#     del questions2[0]
#     print(len(questions2))
    
#     for j in questions2:
#         ratings2 = j.find_element_by_xpath('./td[2]/div/a').find_elements_by_xpath("*")
#         print(len(ratings2))
#         ratings2[choice-1].click()
    

#"/html/body/div[3]/div[3]/form/fieldset/div/div/div[2]/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td[2]/div/a/span[5]"

#select.select_by_visible_text('ESS/DB/100 Database Fundamentals')
time.sleep(1) #Delay to load the page
























