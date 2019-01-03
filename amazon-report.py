from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv
import getpass

try:
    _input = raw_input
except NameError:
    _input = input

amzn_url = _input('Your amazon account is at [www.amazon.de]: ').strip()
browser = _input('Selenium driver to use (chrome/firefox) [firefox]: ').strip()
username = _input('Your username on amazon: ').strip()
password = getpass.getpass()

print('')
print('All set! Please do not move your mouse while the script is running.')
print('Yeah, I know. :/')
print('')
_input('Press any key to start the script')
print('')

print('Sit back, relax, and enjoy your export. Keep your fingers crossed!')
print('If the script is stuck, just close the {} window'.format(
    browser if browser else 'firefox'))

browser = webdriver.Chrome() if browser == 'chrome' else webdriver.Firefox()
browser.implicitly_wait(3)
browser.get('https://{}'.format(amzn_url if amzn_url else 'www.amazon.de'))

your_account = browser.find_element(By.ID, 'nav-link-yourAccount')
actions = webdriver.ActionChains(browser)
sleep(3)
actions.move_to_element(your_account).perform()
WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'nav-flyout-ya-signin')))
sleep(2)
login = browser.find_element_by_css_selector('#nav-flyout-ya-signin > a')
login.click()

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
        EC.visibility_of_element_located((By.ID, 'nav-link-yourAccount')))
your_acct = browser.find_element_by_css_selector(
        '#nav-link-yourAccount > span.nav-line-1')
actions = webdriver.ActionChains(browser)
actions.move_to_element(your_acct).perform()
WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'nav_prefetch_yourorders')))
orders = browser.find_element(By.ID, 'nav_prefetch_yourorders')
actions.move_to_element(orders).click().perform()

WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'span.a-dropdown-prompt')))
sleep(3)
time_frame = browser.find_element_by_css_selector('span.a-dropdown-prompt')
time_frame.click()
last_year = browser.find_element_by_id('orderFilter_3')
last_year.click()


def text(el):
    return el.get_attribute('textContent').strip()


def get_values_and_get_last_button():
    orders = browser.find_elements_by_css_selector('div.a-box-group.order')
    values = []
    for o in orders:
        date = text(o.find_element(By.CSS_SELECTOR,
                                   'div.order-info div.a-col-left > div.a-row'
                                   '> div:nth-child(1) > div.a-size-base'
                                   '> span.value'))
        items = o.find_elements_by_css_selector(
            'div.shipment div.a-row > div.a-fixed-left-grid')
        for i in items:
            desc = text(i.find_element(By.CSS_SELECTOR,
                                       'div.a-col-right > div:nth-child(1)'
                                       '> a'))
            cost = text(i.find_element(By.CSS_SELECTOR,
                                       'div.a-col-right span.a-color-price'
                                       '> nobr')).split()[1]
            values.append((date, float(cost.replace(',', '.')),
                           '{}'.format(unicode(desc).encode('utf-8'))))
    try:
        last = browser.find_element_by_css_selector(
            'div.a-text-center.pagination-full ul.a-pagination li.a-last a')
    except:
        last = None
    return (values, last)

rows = []
values, last = get_values_and_get_last_button()
rows.extend(values)

while last:
    last.click()
    values, last = get_values_and_get_last_button()
    rows.extend(values)

print('Done! Writing results to amazon-report.csv...')
with open('amazon-report.csv', 'w') as file_out:
    csvwriter = csv.writer(file_out, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['Date', 'Price', 'Item description'])
    for row in rows:
        csvwriter.writerow(row)

browser.quit()

print('Your CSV is ready!')
