from selenium import webdriver
import time
import Constants
import Locators

def LogoutPageTest(username, password):
    driver = webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()

    usernameField = driver.find_element_by_css_selector(Locators.login_page_username_css_selector)
    passwordField = driver.find_element_by_css_selector(Locators.login_page_password_css_selector)

    loginInButton = driver.find_element_by_css_selector(Locators.login_page_login_button_css_selector)

    usernameField.send_keys(username)
    passwordField.send_keys(password)

    loginInButton.click()

    if driver.current_url == {Constants.BASE_URL}:
        print ('Login successful')
        return

    time.sleep(3)    

    LogoutButton = driver.find_element_by_css_selector(Locators.Logout_page_button_css_selector)
    LogoutButton.click()

    time.sleep(3)


    if driver.current_url == f"{Constants.BASE_URL}{Constants.LOGIN_PAGE}":
        print ('Logout successful')  
    else:
        print ('Login unsuccessfull')
    time.sleep(3)

    #TEST_DATA = MockedData.getTestData('MOCK_DATA.json')

    #for Data in TEST_DATA:
      #  TestLogin(Data['username'], Data['password'])
