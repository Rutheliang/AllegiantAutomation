import pytest
from selenium.webdriver import ActionChains

from testData.LoginPageData import LoginPageData
from pageObject.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_NewAccount(self, getData):
        loginPage = LoginPage(self.driver)
        if loginPage.getPopup1().is_displayed():
            loginPage.getClose1().click()

        if loginPage.getPopup2().is_displayed():
            loginPage.getClose2().click()

        loginPage.getLogin().click()
        loginPage.getFirstName().send_keys(getData["firstname"])
        loginPage.getLastName().send_keys(getData["lastname"])
        loginPage.getMonth().click()

        action = ActionChains(self.driver)
        action.move_to_element(loginPage.getMonth7()).click().perform()

        loginPage.getDay().click()
        action = ActionChains(self.driver)
        action.move_to_element(loginPage.getDay24()).click().perform()

        loginPage.getYear().send_keys(getData["year"])

        loginPage.getEmail().send_keys("test24@aol.com")
        loginPage.getEmail1().send_keys("test24@aol.com")

        loginPage.getPassword().send_keys("Test@111")
        loginPage.getPassword1().send_keys("Test@222")

        loginPage.getSubmit().click()

        error = loginPage.getPwError().text
        assert "Passwords do not match" == error

    @pytest.fixture(params=LoginPageData.test_LoginPage_Data)
    def getData(self, request):
        return request.param

