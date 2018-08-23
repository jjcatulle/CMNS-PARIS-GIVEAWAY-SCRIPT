import names
from random import randint, choice
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#the script above import packages and the modules
# I'm using chrome browser
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " CMNS PARIS GIVEAWAY SCRIPT  by Jean     ")

Entries= input('how many entries?:')
def entry():

    catchall='@catchall.com'#enter your catchall dont forget to add '@'
    gender = choice(['male', 'female'])
    firstname = names.get_first_name(gender=gender)
    lastname = names.get_last_name()
    fullname= names.get_full_name()
    email = (firstname + choice("-_.") + lastname).lower() + "".join([str(randint(0, 10)) for x in range(randint(1, 5))]) + catchall
    url='https://kimsoswimwear.lpages.co/cmns-giveaway/'    


    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(5)

    email1=driver.find_element_by_xpath('//*[@id="e38206f748d9f5ee39fc7f65383b3bda-us5jH3xVb7m33QyzQFd2dL"]')
    email1.send_keys(email)
    signup=driver.find_element_by_xpath('//*[@id="section-main-content"]/div[1]/div/div/div[5]/div/div[2]/form/div/div[2]/div/div/div/button')
    signup.click()
    
    driver.implicitly_wait(5)
    
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " entry submitted")
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " follow me on twitter: @viniciusjr_7 ")
    
    





for i in range(Entries):
    entry()
print('   ')
print('   ')
print ("[" + (time.strftime("%H:%M:%S")) + "]" + "          Please Donate To: ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " the Epilepsy Foundation New England ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " 335 Main St., Wilmington, MA 01887")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + "              or  ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " the American Foundation for Suicide Prevention (AFSP) ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " 120 Wall St., 29th Floor, New York, NY 10005")
print('   ')
print('   ')

''' hey guys someone closed to me passed away and its literally the hardest thing
i've ever dealt with,it steal affect me everyday. Be nice to people, and always check on
your friends'''
