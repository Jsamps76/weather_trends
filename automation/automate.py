from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.nbastuffer.com/')

link_to_click =  driver.find_element_by_class_name('x-recent-post6.no-image')[4]
link_to_click.click()

sleep(5)

search_field = driver.find_element_by_tag_name('input')
# print(search_field)

search_field.send_keys('Jimmy Butler')



sleep(10)

driver.close()

