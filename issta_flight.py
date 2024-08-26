Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.issta.co.il/"
        self.origin_input = (By.ID, "origin")
        self.destination_input = (By.ID, "destination")
        self.search_button = (By.ID, "searchButton")

    def load(self):
        self.driver.get(self.url)

    def enter_origin(self, origin):
        self.driver.find_element(*self.origin_input).send_keys(origin)

    def enter_destination(self, destination):
        self.driver.find_element(*self.destination_input).send_keys(destination)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()
from selenium.webdriver.common.by import By

class FlightSearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.select_flight_button = (By.CSS_SELECTOR, ".select-flight")

    def select_first_flight(self):
        self.driver.find_element(*self.select_flight_button).click()
... from selenium.webdriver.common.by import By
... 
... class CheckoutPage:
...     def __init__(self, driver):
...         self.driver = driver
...         self.checkout_button = (By.ID, "checkoutButton")
... 
...     def is_checkout_page_loaded(self):
...         return self.driver.find_element(*self.checkout_button).is_displayed()
... import pytest
... from selenium import webdriver
... from pages.homepage import HomePage
... from pages.flight_search_results_page import FlightSearchResultsPage
... from pages.checkout_page import CheckoutPage
... 
... @pytest.fixture
... def driver():
...     driver = webdriver.Chrome()
...     yield driver
...     driver.quit()
... 
... def test_flight_booking(driver):
...     homepage = HomePage(driver)
...     search_results_page = FlightSearchResultsPage(driver)
...     checkout_page = CheckoutPage(driver)
... 
...     # Load the homepage
...     homepage.load()
... 
...     # Enter flight details
...     homepage.enter_origin("Tel Aviv")
...     homepage.enter_destination("New York")
...     homepage.click_search()
... 
...     # Select the first flight from the search results
...     search_results_page.select_first_flight()
... 
...     # Assert that the checkout page is loaded
...     assert checkout_page.is_checkout_page_loaded()
... import pytest
... from selenium import webdriver
... 
... @pytest.fixture(scope="session")
... def driver():
...     driver = webdriver.Chrome()
...     yield driver
