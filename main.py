from selenium import webdriver
from time import sleep
import os

URL         = 'https://www.gosuslugi.ru/'
URL_PROFILE = 'https://lk.gosuslugi.ru/profile'

FOLDER_NAME = 'folder'
FILE_NAME   = 'file.txt'

LOGIN       = '*some_login*'
PASSWORD    = '*some_password*'

def connect():
    return webdriver.Chrome()

def go_to_url(url, driver):
    driver.get(url)
    sleep(3)
    return driver

def main():
    driver = connect()
    driver = go_to_url(URL, driver)

    log_url = driver.find_element_by_class_name('lk-enter').get_attribute('href')

    driver = go_to_url(log_url, driver)

    input_fields = driver.find_elements_by_class_name('ui-inputfield')

    input_fields[0].send_keys(LOGIN)
    input_fields[1].send_keys(PASSWORD)
    
    driver.find_element_by_class_name('button-big').click()

    driver = go_to_url(URL_PROFILE, driver)

    content = []
    content.append(driver.find_element_by_class_name('title-h5').text)
    inform = driver.find_elements_by_class_name('mt-4')
    
    for i in range(3):
        content.append(inform[i].text)

    if not os.path.isdir(FOLDER_NAME):
        os.mkdir(FOLDER_NAME)

    file = open(f'{FOLDER_NAME}/{FILE_NAME}', 'w')

    for item in content:
        file.write(item + '\n')

    file.close()

main()