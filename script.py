__author__ = 'Gundeti Dheeraj'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_till_pageloads(browser,identityby,value):
    delay=20 #seconds
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((identityby, value)))

def buy_amazon(browser,username,password,url,cvv):

    browser.get('https://www.amazon.in')

    wait_till_pageloads(browser, By.ID, 'nav-link-accountList')
    login=browser.find_element_by_id('nav-link-accountList')
    login.click()

    print('Logging into Amazon...')
    wait_till_pageloads(browser, By.ID, 'ap_email')
    userelem = browser.find_element_by_id('ap_email')
    userelem.send_keys(username)
    clickit = browser.find_element_by_id('continue')
    clickit.click()

    wait_till_pageloads(browser, By.ID, 'ap_password')
    passwrd=browser.find_element_by_id('ap_password')
    passwrd.send_keys(password)
    clickit=browser.find_element_by_id('signInSubmit')
    clickit.click()


    print('opening product page...')
    browser.get(url)
    wait_till_pageloads(browser, By.ID, 'add-to-cart-button')
    clickit = browser.find_element_by_id('add-to-cart-button')
    clickit.click()

    print('Adding item to cart..')
    wait_till_pageloads(browser,By.ID,'nav-cart')
    clickit=browser.find_element_by_id('nav-cart')
    clickit.click()

    wait_till_pageloads(browser,By.NAME,'proceedToCheckout')
    clickit=browser.find_element_by_name('proceedToCheckout')
    clickit.click()

    print('entering cvv number...')
    wait_till_pageloads(browser, By.NAME, 'addCreditCardVerificationNumber0')
    cvv_input=browser.find_element_by_name('addCreditCardVerificationNumber0')
    cvv_input.send_keys(cvv)
    clickit=browser.find_element_by_name('ppw-widgetEvent:SetPaymentPlanSelectContinueEvent')
    clickit.click()

    print('Waiting for Amazon to update order page... (This takes approximately 3 minutes.)')
    wait_till_pageloads(browser,By.NAME,'placeYourOrder1')
    clickit=browser.find_element_by_name('placeYourOrder1')
    clickit.click()


def main():

    input_file = open("input.txt", "r")
    line=input_file.readline()
    webdriver_path,mailid,password,url,cvv=line.split(',')

    print('\nInitializing Chrome WebDriver...')
    browser = webdriver.Chrome(webdriver_path)

    buy_amazon(browser,mailid,password,url,cvv)

    input("press any key and enter to terminate program!!")

if __name__=='__main__':
    main()