from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()

a=4
b=5

driver.get("http://localhost:5000")
text1=driver.find_element_by_name('text1')
text2=driver.find_element_by_name('text2')

text1.send_keys(str(a))
text2.send_keys(str(b))
text1.send_keys(Keys.RETURN)

assert ("Answer is 20" in driver.page_source),'Mismatch' 

driver.close()
