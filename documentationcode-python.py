from selenium import webdriver
import selenium.webdriver.support

#create instance of driver
driver = webdriver.Chrome()

#direct driver to web page
driver.get("https://www.google.com")

#locate web element by identifier
search_bar = driver.find_element_by_name("q")
search_button = driver.find_element_by_name("btnK")

#perform action on web elements using web driver
search_bar.send_keys("Revolos")
search_button.click()

#close browser and quit driver
driver.close()
driver.quit()