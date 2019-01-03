from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

username = 'my_amazon_username'
password = 'my_amazon_password'

browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get('https://www.amazon.de')

your_account = browser.find_element(By.ID, 'nav-link-yourAccount')
actions = webdriver.ActionChains(browser)
actions.move_to_element(your_account).perform()
WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'nav-flyout-ya-signin')))
login = browser.find_element_by_css_selector('#nav-flyout-ya-signin > a')
actions.move_to_element(login).click().perform()

browser.find_element(By.ID, 'ap_email')
email = browser.find_element(By.ID, 'ap_email')
email.clear()
email.send_keys(username)

passwd = browser.find_element(By.ID, 'ap_password')
passwd.clear()
passwd.send_keys(password)

login_btn = browser.find_element(By.ID, 'signInSubmit')
login_btn.click()

WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'nav-link-yourAccount')))
your_acct = browser.find_element_by_css_selector(
        '#nav-link-yourAccount > span.nav-line-1')
actions = webdriver.ActionChains(browser)
actions.move_to_element(your_acct).perform()
sleep(2)
WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'nav_prefetch_yourorders')))
orders = browser.find_element(By.ID, 'nav_prefetch_yourorders')
actions.move_to_element(orders).click().perform()

sleep(2)
values = browser.find_elements_by_css_selector(
        'div.a-column.a-span2 > div.a-row.a-size-base > span.value')

for value in values:
    print(value.get_attribute('textContent'))
time_frame = browser.find_element_by_css_selector('span.a-dropdown-prompt')
time_frame.click()
sleep(2)
last_year = browser.find_element_by_id('orderFilter_3')
last_year.click()

values = browser.find_elements_by_css_selector(
        'div.a-column.a-span2 > div.a-row.a-size-base > span.value')

for value in values:
    print(value)
