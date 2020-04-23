from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


def test_items(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    try:
        add_button = WebDriverWait(browser, 10).until(presence_of_element_located((By.CLASS_NAME, 'btn-add-to-basket')))
    except TimeoutException:
        add_button = None

    assert add_button, "button 'add to basket' not found"
