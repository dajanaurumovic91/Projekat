import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import Constants
import Locators
import MockedData


def TestRegistration(username,email,password):
    driver = webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()

    HomeLoginButton = driver.find_element_by_css_selector(Locators.PrijavaDugme)
    HomeLoginButton.click()

    RegisterButton = driver.find_element_by_css_selector(Locators.login_page_register_button_css_selector)
    RegisterButton.click()

    UsernameField = driver.find_element_by_name(Locators.register_page_username_field)
    EmailField = driver.find_element_by_name(Locators.register_page_email_field)
    PasswordField = driver.find_element_by_name(Locators.register_page_password1_field)
    Password2Field = driver.find_element_by_name(Locators.register_page_password2_field)
    RegisterButton2 = driver.find_element_by_css_selector(Locators.register_page_submit_button)
    
    UsernameField.send_keys(username)
    EmailField.send_keys(email)
    PasswordField.send_keys(password)
    Password2Field.send_keys(password)

    RegisterButton2.click()
    time.sleep(3)
    
    if len(driver.find_elements(By.ID, Locators.registration_page_successfull_registration_button_id))>0:
        print(f'Registration Successful with {email} and {username} and {password}')
    else:
        print(f'Registration Unsuccessful with {email} and {username} and {password}')
    time.sleep(3)

TEST_DATA = MockedData.getTestData('MOCK_DATA.json')

for Data in TEST_DATA:

    TestRegistration(Data['username'], Data['email'], Data['password'])
