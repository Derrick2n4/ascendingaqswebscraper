from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import pandas as pd
import time

import unittest


driver = webdriver.Safari()
url = driver.get("https://vmatrix1.brevardclerk.us/beca/CaseType_Search.cfm")
driver.maximize_window()
time.sleep(20)


# accept_button = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[1]/td/input[1]")
def safari_open_website(driver, url):
    driver.get(url)

def accept_usage(xpath):
    select = Select(driver.find_element(By.XPATH, xpath))
    values = select.select_by_value("Yes")
    for i in values:
        if i != values:
            print("Did not accept terms")
        else:
            i.click()

def submit_button(xpath):
    element = driver.find_element(By.XPATH, xpath)
    all_options = element.find_elements(By.TAG_NAME, "option")
    for option in all_options:
        if option == option.get_attribute("Submit"):
            option.click()

def select_gen_pop_court_records(xpath):
    gen_pop_button = driver.find_element(By.XPATH, xpath)
    return gen_pop_button.click()

def search_button(xpath):
    element = driver.find_element(By.XPATH, xpath)
    select = Select(element)
    values = select.select_by_value("Search")
    for i in values:
        if i != values:
            exit()
        else:
            i.click()

def case_type_menu_option():
    case_type_button = driver.find_element(By.Name, "case_type")
    for name in case_type_button:
        if name == case_type_button:
            name.click()
        else:
            exit()
        # search_button(xpath)

def get_probate_page(xpath):
    # Select case type drop down menu
    probate_menu_option = driver.find_element(By.XPATH, xpath) # xpath = /html/body/form/div[1]/table/tbody/tr[1]/td[2]/select/option[129]
    all_options = probate_menu_option.find_elements(By.TAG_NAME, "option")
    select = Select(probate_menu_option)
    probate_value = select.select_by_value("PROBATE")

    # Search for Probate option and click
    for options in all_options:
        if options != probate_value:
            exit()
        else:
            options.click()
        search_button = driver.find_element(By.XPATH, '//*[@id="inputform"]/div[2]/input[1]')
        # Click Search button to navigate to probate page
        probate_page = search_button.click()
        return probate_page
    # /html/body/form/div[1]/table/tbody/tr[1]/td[2]/select

# # def no_new_data():

#     """
#     probate_page = drop_down_menu(xpath='/html/body/div[5]/table/tbody')
#     todays_date = datetime.now()
#     yesterday = todays_date - timedelta(days=1)

#     # first entry in date filed column
#     date_filed_column_data = driver.find_element(By.XPATH, '/html/body/div[5]/table/tbody/tr[2]/td[1]')
#     date_filed_list = []
#     for dates in range(len(date_filed_column_data)):
#         date_filed_list.append(date_filed_column_data[dates].text)
#     """



























select = Select(driver.find_element(By.NAME,'name'))
select.select_by_index()
select.select_by_visible_text("text")
select.select_by_value()











