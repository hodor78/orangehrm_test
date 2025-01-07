# Test Automation Framework for OrangeHRM

## Overview
This test automation framework is designed to validate the functionality of the OrangeHRM application. 
It includes tests for both the UI and backend systems, covering user management workflows such as creating, 
deleting, and retrieving users. 


Key Features

* Page Object Model (POM): Implements the Page Object Model pattern to separate test logic from UI interaction.
* System Independent: Can be run on any operating system.
* No Upfront Browser Driver Installation: Tests can be run without the need to manually install browser drivers.
* Backend Testing Extensibility: Easily extendable to support backend testing.
* Scalable and Maintainable: Designed for scalability and easy maintenance with a clear structure and self-descriptive code.
* Configurable Settings: Reads settings from a config.ini file, including browser type, credentials, rerun count, URLs, headless mode
* Multi-browser Support: Runs test scenarios in Chrome, Edge, and Firefox.
* Automatic Rerun: Automatically reruns failed steps a specified number of times.
* Headless Mode: Supports headless mode with the option to turn it on or off.

## Requirements
The framework uses the following tools and libraries, as specified in `requirements.txt`:
- **Selenium**: For UI automation
- **Pytest**: For test execution
- **PyMySQL**: For database validation
- **Requests**: For API validation
- **Webdriver-Manager**: For managing browser drivers

Install all dependencies by running:
pip install -r requirements.txt

Running Tests:
pytest tests/

Note: 
backend tests are commented!
