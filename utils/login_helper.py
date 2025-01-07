from pages.login_page import LoginPage

def login(driver, config):
    login_page = LoginPage(driver)
    username = config.get('basic_info', 'username')
    password = config.get('basic_info', 'password')
    login_page.login(username, password)