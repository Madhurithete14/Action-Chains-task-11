"""
Using Python Selenium Automation And Action Chains Visit the  URL
https://jqueryui.com/droppable/
and do Drag and Drop operation of the white Rectangle Box into the Yellow Rectangle Box.
"""
import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)


def drag_and_drop(elem1, elem2):
    action = ActionChains(driver)
    action.drag_and_drop(elem1, elem2)
    action.perform()


def context_click(elem1):
    action = ActionChains(driver)
    action.context_click(elem1)
    action.perform()


iframe_element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "iframe[class='demo-frame']")))
driver.switch_to.frame(iframe_element)


image1 = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='draggable']")))
drop = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='droppable']")))
drag_and_drop(image1, drop)
time.sleep(2)
context_click(drop)

time.sleep(5)
driver.close()