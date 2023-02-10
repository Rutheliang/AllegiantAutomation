import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_SearchAddFlight(self):
        homePage = HomePage(self.driver)
        if homePage.getPopup1().is_displayed():
            homePage.getClose1().click()

        if homePage.getPopup2().is_displayed():
            homePage.getClose2().click()

        homePage.getOrigin().click()
        homePage.getOrigin1().click()

        homePage.getDestination().click()
        homePage.getDestination1().click()

        time.sleep(2)
        homePage.getStart().click()

        time.sleep(2)
        dates = homePage.getStartDates()
        for date in dates:
            if date.get_attribute("data-hook") == "flight-search-date-picker_calendar-0_select-day-24":
                date.click()
                break

        time.sleep(2)
        dates = homePage.getBackDates()
        for date in dates:
            if date.get_attribute("data-hook") == "flight-search-date-picker_calendar-1_select-day-24":
                date.click()
                break

        homePage.getSearch().click()
        homePage.getContSelect().click()

        time.sleep(3)
        homePage.getBundle1().click()

        homePage.getContBundle1().click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[id='adults.0.first-name']")))

        homePage.getFirstName().send_keys("Test")
        homePage.getLastName().send_keys("One")
        homePage.getGender().click()
        homePage.getMonth().click()
        homePage.getMonth4().click()
        homePage.getDay().click()
        homePage.getDay24().click()
        homePage.getYear().send_keys("1985")
        homePage.getEmail().send_keys("test123@aol.com")
