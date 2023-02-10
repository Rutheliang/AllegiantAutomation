from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    popup1 = (By.XPATH, "//div[@class='ot-sdk-container']")
    close1 = (By.CSS_SELECTOR, "div[id='onetrust-close-btn-container']")
    popup2 = (By.XPATH, "//div[@class='Box-s8oj9r-0 hzaPoz']")
    close2 = (By.XPATH, "//img[@alt='closeIcon']")
    origin = (By.XPATH, "//div[@data-hook='flight-search-origin']")
    origin1 = (By.XPATH, "//div[@data-hook='flight-search-origin_AUS']")
    destination = (By.XPATH, "//div[@data-hook='flight-search-destination']")
    destination1 = (By.XPATH, "//div[@data-hook='flight-search-destination_AVL']")
    start = (By.XPATH, "//button[@data-hook='flight-search-date-picker_expand-start-date']")
    startDates = (By.XPATH, "//div[@data-hook='flight-search-date-picker_calendar-0']/div[3]/button")
    backDates = (By.XPATH, "//div[@data-hook='flight-search-date-picker_calendar-1']/div[3]/button")
    search = (By.XPATH, "//button[@data-hook='flight-search-submit']")
    contSelect = (By.XPATH, "//button[@data-hook='flights-page_continue']")
    bundle1 = (By.XPATH, "//button[@data-hook='select-tier-1']")
    contBundle1 = (By.XPATH, "//button[@data-hook='bundles-page_continue']")
    firstname = (By.CSS_SELECTOR, "input[id='adults.0.first-name']")
    lastname = (By.ID, "adults.0.last-name")
    gender = (By.CSS_SELECTOR, "label[data-hook='travelers-form_adults_0_gender_FEMALE']")
    month = (By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-month']")
    month4 = (By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-month_4']")
    day = (By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-day']")
    day24 = (By.XPATH, "//div[@data-hook='travelers-form_adults_0_dob-day_24']")
    year = (By.ID, "adults.0.dob-year")
    email =(By.ID, "adults.0.email")

    def getPopup1(self):
        return self.driver.find_element(*HomePage.popup1)

    def getClose1(self):
        return self.driver.find_element(*HomePage.close1)

    def getPopup2(self):
        return self.driver.find_element(*HomePage.popup2)

    def getClose2(self):
        return self.driver.find_element(*HomePage.close2)

    def getOrigin(self):
        return self.driver.find_element(*HomePage.origin)

    def getOrigin1(self):
        return self.driver.find_element(*HomePage.origin1)

    def getDestination(self):
        return self.driver.find_element(*HomePage.destination)

    def getDestination1(self):
        return self.driver.find_element(*HomePage.destination1)

    def getStart(self):
        return self.driver.find_element(*HomePage.start)

    def getStartDates(self):
        return self.driver.find_elements(*HomePage.startDates)

    def getBackDates(self):
        return self.driver.find_elements(*HomePage.backDates)

    def getSearch(self):
        return self.driver.find_element(*HomePage.search)

    def getContSelect(self):
        return self.driver.find_element(*HomePage.contSelect)

    def getBundle1(self):
        return self.driver.find_element(*HomePage.bundle1)

    def getContBundle1(self):
        return self.driver.find_element(*HomePage.contBundle1)

    def getFirstName(self):
        return self.driver.find_element(*HomePage.firstname)

    def getLastName(self):
        return self.driver.find_element(*HomePage.lastname)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getMonth(self):
        return self.driver.find_element(*HomePage.month)

    def getMonth4(self):
        return self.driver.find_element(*HomePage.month4)

    def getDay(self):
        return self.driver.find_element(*HomePage.day)

    def getDay24(self):
        return self.driver.find_element(*HomePage.day24)

    def getYear(self):
        return self.driver.find_element(*HomePage.year)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)




