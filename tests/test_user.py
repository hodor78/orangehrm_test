import pymysql
import requests
from utils.config_reader import read_config
from utils.login_helper import login
from pages.admin_page import AdminPage
from utils.sql_helper import is_user_deleted_in_backend
from utils.api_helper import get_user_records_from_api

config = read_config()
url = config.get('basic_info', 'url')


def test_url_is_correct(driver):
    driver.get(url)
    assert "OrangeHRM" in driver.title, "Wrong title name"


def test_login_functionality(driver):
    driver.get(url)
    login(driver, config)
    admin_page = AdminPage(driver)
    assert admin_page.admin_page_is_visible(), "Login wasn't successfull"


def test_admin_user_added(driver):
    driver.get(url)
    login(driver, config)
    admin_page = AdminPage(driver)
    new_user = admin_page.create_user("Admin", "Enabled", "a")
    users_in_record_found_table = admin_page.search_existing_user_in_system_users()
    reset_user_value = admin_page.reset_existing_user_from_system_users()
    assert "Success".lower() in new_user["success_message"].lower(), "User not added successfully message"
    assert new_user["username"] in users_in_record_found_table, "User is not in the records table"
    assert reset_user_value == "", "The username field is not empty after clicking reset."
    assert new_user["username"] in users_in_record_found_table, "User is not in the records table"


def test_ess_user_added(driver):
    driver.get(url)
    login(driver, config)
    admin_page = AdminPage(driver)
    new_user = admin_page.create_user("ESS", "Disabled", "a")
    users_in_record_found_table = admin_page.search_existing_user_in_system_users()
    reset_user_value = admin_page.reset_existing_user_from_system_users()
    assert "Success".lower() in new_user["success_message"].lower(), "User not added successfully message"
    assert new_user["username"] in users_in_record_found_table, "User is not in the records table"
    assert reset_user_value == "", "The username field is not empty after clicking reset."
    assert new_user["username"] in users_in_record_found_table, "User is not in the records table"

def test_ess_user_deleted(driver):
    driver.get(url)
    login(driver, config)
    admin_page = AdminPage(driver)
    new_user = admin_page.create_user("ESS", "Disabled", "a")
    deleted_user = admin_page.delete_user_from_records_table()
    assert "Success".lower() in deleted_user["delete_message"].lower(), "User not deleted successfully message"
    assert deleted_user["no_records_found_message"].lower() in "No Records Found".lower(), "User was not deleted from the records table"

    # # SQL validation
    # db_config = {
    #     "host": config.get("database", "host"),
    #     "user": config.get("database", "user"),
    #     "password": config.get("database", "password"),
    #     "db": config.get("database", "db"),
    # }
    # user_deleted_in_backend = is_user_deleted_in_backend(db_config, new_user["username"])
    # assert user_deleted_in_backend, "User was not deleted in the backend database"
    #
    # # API validation
    # api_url = config.get("api", "get_users_url")
    # api_users = get_user_records_from_api(api_url)
    # usernames_from_ui = admin_page.get_all_usernames_in_table()
    # assert set(usernames_from_ui) == set(api_users), "API data does not match UI data"