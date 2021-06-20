from selenium import webdriver
import Constants
import Locators
import time

def TestLogin(username, password):
    driver = webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()

    PrijavaDugme = driver.find_element_by_css_selector(Locators.PrijavaDugme)
    PrijavaDugme.click()
    usernameField = driver.find_element_by_css_selector(Locators.login_page_username_css_selector)
    passwordField = driver.find_element_by_css_selector(Locators.login_page_password_css_selector)

    loginInButton = driver.find_element_by_css_selector(Locators.login_page_login_button_css_selector)

    usernameField.send_keys(username)
    passwordField.send_keys(password)

  
    loginInButton.click()
    
    time.sleep(3)

    if(driver.current_url==Constants.BASE_URL):
        print('Uspesno logovanje')
    else:
        print('Neuspesno logovanje')


TestLogin('dajana.urumovic@gmail.com','Ribizla2017')

