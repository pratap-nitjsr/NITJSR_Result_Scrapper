from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException

class StudentPortal:
    def __init__(self, headless=True):
        self.chrome_options = webdriver.ChromeOptions()
        if headless:
            self.chrome_options.add_argument("--headless")
    def __make_driver(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def __refresh(self):
        self.driver.refresh()

    def __change_pwd(self, username):
        self.driver.get('http://202.168.87.90/StudentPortal/ForgetPassword.aspx')

        self.driver.find_element(By.NAME, 'txt_username').send_keys(username)
        self.driver.find_element(By.NAME, 'txtnewpass').send_keys('a')
        self.driver.find_element(By.NAME, 'txtConfirmpass').send_keys('a')
        try:
            self.driver.find_element(By.NAME, 'btnSubmit').click()
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
            except NoAlertPresentException:
                pass
        except:
            pass

    def __login(self, username):
        self.driver.get('http://202.168.87.90/StudentPortal/Login.aspx')

        self.driver.find_element(By.NAME, 'txt_username').send_keys(username)
        self.driver.find_element(By.NAME, 'txt_password').send_keys('a')

        self.driver.find_element(By.NAME, 'btnSubmit').click()

    def __access_result(self, sem):
        dropdown = Select(self.driver.find_element(By.NAME, 'ddlSemester'))
        dropdown.select_by_value(sem)

        self.driver.find_element(By.NAME, 'btnimgShowResult').click()

        result_div = self.driver.find_element(By.ID, 'PnlShowResult')
        result_table = result_div.find_element(By.TAG_NAME, 'table')

        rows = result_table.find_elements(By.TAG_NAME, 'tr')

        result = []

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if not cells:
                cells = row.find_elements(By.TAG_NAME, 'th')
            row_data = [cell.text for cell in cells]
            result.append(row_data)

        return result

    def __quit(self):
        self.driver.quit()

    def get_result(self, username, sem):
        self.__make_driver()
        self.__refresh()
        print("Process Started.....")
        self.__change_pwd(username)
        print("Attempting Login....")
        self.__login(username)
        print("LOgged In Succesfully!!")
        print("Accessing Result...")
        result = self.__access_result(sem)
        self.__quit()

        return result


