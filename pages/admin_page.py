import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.unique_user_helper import generate_unique_user_id


class AdminPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Locators
        self.admin_page = (By.XPATH, "//*[contains(@class, 'upgrade-layout')]")
        self.main_menu = (By.XPATH, "//*[@class='oxd-main-menu']")
        self.admin_tab_main_menu = (By.XPATH, "(//*[@class='oxd-main-menu']/li)[1]")
        self.add_user_button = (By.XPATH, "//*[@class='orangehrm-header-container']/button")
        self.user_role_selection_area = (By.XPATH, "(//*[@class='oxd-select-wrapper'])[1]")
        self.user_role_admin = (By.XPATH, "(//div[@role='listbox']/*)[2]")
        self.user_role_ess = (By.XPATH, "(//div[@role='listbox']/*)[3]")
        self.status_selection_area = (By.XPATH, "(//*[@class='oxd-select-wrapper'])[2]")
        self.status_enabled = (By.XPATH, "(//div[@role='listbox']/*)[2]")
        self.status_disabled = (By.XPATH, "(//div[@role='listbox']/*)[3]")
        self.employee_name = (By.XPATH, "//*[@class='oxd-autocomplete-wrapper']//input")
        self.empl_names_suggestions = (By.XPATH, "//*[@role='listbox']")
        self.select_1st_empl_name = (By.XPATH, "(//div[@role='listbox']/*)[1]")
        self.username = (By.XPATH, "(//*[contains(@class,'label-')])[4]/..//input")
        self.error_message = (By.XPATH, "//*[@class='oxd-input oxd-input--active']")
        self.password = (By.XPATH, "(//*[@type='password'])[1]")
        self.confirm_password = (By.XPATH, "(//*[@type='password'])[2]")
        self.save_button = (By.XPATH, "//*[@type='submit']")
        self.success_confirmation = (By.XPATH, "//*[contains(@class, 'content--success')]")
        self.username_system_users_search = (By.XPATH, "(//*[@class='oxd-input oxd-input--active'])[2]")
        self.records_table = (By.XPATH, "//*[@class='orangehrm-container']")
        self.search_button = (By.XPATH, "//*[@type='submit']")
        self.username_in_record_found_table = (By.XPATH, "(//*[@role='cell'])[2]/div")
        self.reset_button = (By.XPATH, "//*[@class='oxd-form-actions']/*[@type='button']")
        self.delete_button_table = (By.XPATH, "(//*[contains(@class,'action-')])[1]")
        self.delete_confirmation_button = (By.XPATH, "//*[contains(@class,'button--medium oxd-button--label-danger')]")
        self.no_records_found_msg = (By.XPATH, "(//*[@class='oxd-text oxd-text--span'])[1]")


    def admin_page_is_visible(self):
        return self.driver.find_element(*self.admin_page).is_displayed()

    def create_user(self, role, status, employee_name_hint):
        self.driver.find_element(*self.admin_tab_main_menu).click()
        self.driver.find_element(*self.add_user_button).click()
        self.driver.find_element(*self.user_role_selection_area).click()
        if role == "Admin":
            self.driver.find_element(*self.user_role_admin).click()
        elif role == "ESS":
            self.driver.find_element(*self.user_role_ess).click()
        self.driver.find_element(*self.status_selection_area).click()
        if status == "Enabled":
            self.driver.find_element(*self.status_enabled).click()
        elif status == "Disabled":
            self.driver.find_element(*self.status_disabled).click()
        self.driver.find_element(*self.employee_name).send_keys(employee_name_hint)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.select_1st_empl_name)).click()
        self.driver.find_element(*self.username).send_keys(generate_unique_user_id())
        self.driver.find_element(*self.password).send_keys("qwertY1")
        self.driver.find_element(*self.confirm_password).send_keys("qwertY1")
        self.username_value = self.driver.find_element(*self.username).get_property("value")
        self.driver.find_element(*self.save_button).click()
        succesfully_saved_confirm = WebDriverWait(self.driver, 10).until \
            (EC.visibility_of_element_located(self.success_confirmation)).text
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.records_table))
        return {
            "success_message": succesfully_saved_confirm,
            "username": self.username_value
        }

    def search_existing_user_in_system_users(self):
        self.driver.find_element(*self.username_system_users_search).send_keys(self.username_value)
        self.driver.find_element(*self.search_button).click()
        username = self.driver.find_element(*self.username_in_record_found_table).text
        return username

    def reset_existing_user_from_system_users(self):
        self.driver.find_element(*self.reset_button).click()
        search_input = self.driver.find_element(*self.username_system_users_search)
        return search_input.get_property("value")

    def delete_user_from_records_table(self):
        self.driver.find_element(*self.username_system_users_search).send_keys(self.username_value)
        self.driver.find_element(*self.search_button).click()
        self.driver.find_element(*self.delete_button_table).click()
        self.driver.find_element(*self.delete_confirmation_button).click()
        succesfully_deleted_confirm = WebDriverWait(self.driver, 10).until \
            (EC.visibility_of_element_located(self.success_confirmation)).text
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.username_in_record_found_table))
        self.driver.find_element(*self.search_button).click()
        no_records_found_msg = self.driver.find_element(*self.no_records_found_msg).text

        return {
            "delete_message": succesfully_deleted_confirm,
            "no_records_found_message": no_records_found_msg
        }







