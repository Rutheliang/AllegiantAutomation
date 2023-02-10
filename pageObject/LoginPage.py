from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    popup1 = (By.XPATH, "//div[@class='Box-s8oj9r-0 hzaPoz']")
    close1 = (By.XPATH, "//img[@alt='closeIcon']")
    popup2 = (By.XPATH, "//div[@class='ot-sdk-container']")
    close2 = (By.CSS_SELECTOR, "div[id='onetrust-close-btn-container']")
    login = (By.XPATH, "//div[@class='Box-s8oj9r-0 dLFASS']")
    firstname = (By.ID, "firstName")
    lastname = (By.ID, "lastName")
    month = (By.XPATH, "//div[@data-hook='home-signup_dob-month_dobMonth']")
    month7 = (By.XPATH, "//div[@data-hook='home-signup_dob-month_dobMonth_7']")
    day = (By.XPATH, "//div[@data-hook='home-signup_dob-day_dobDay']")
    day24 = (By.XPATH, "//div[@data-hook='home-signup_dob-day_dobDay_24']")
    year = (By.ID, "dobYear")
    email = (By.ID, "email")
    email1 = (By.ID, "retypeEmail")
    password = (By.ID, "password")
    password1 = (By.ID, "retypePassword")
    submit = (By.XPATH, "//button[@data-hook='home-signup_submit-button_continue']")
    pwError = (By.ID, "retypePassword_error")

    def getPopup1(self):
        return self.driver.find_element(*LoginPage.popup1)

    def getClose1(self):
        return self.driver.find_element(*LoginPage.close1)

    def getPopup2(self):
        return self.driver.find_element(*LoginPage.popup2)

    def getClose2(self):
        return self.driver.find_element(*LoginPage.close2)

    def getLogin(self):
        return self.driver.find_element(*LoginPage.login)

    def getFirstName(self):
        return self.driver.find_element(*LoginPage.firstname)

    def getLastName(self):
        return self.driver.find_element(*LoginPage.lastname)

    def getMonth(self):
        return self.driver.find_element(*LoginPage.month)

    def getMonth7(self):
        return self.driver.find_element(*LoginPage.month7)

    def getDay(self):
        return self.driver.find_element(*LoginPage.day)

    def getDay24(self):
        return self.driver.find_element(*LoginPage.day24)

    def getYear(self):
        return self.driver.find_element(*LoginPage.year)

    def getEmail(self):
        return self.driver.find_element(*LoginPage.email)

    def getEmail1(self):
        return self.driver.find_element(*LoginPage.email1)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getPassword1(self):
        return self.driver.find_element(*LoginPage.password1)

    def getSubmit(self):
        return self.driver.find_element(*LoginPage.submit)

    def getPwError(self):
        return self.driver.find_element(*LoginPage.pwError)

