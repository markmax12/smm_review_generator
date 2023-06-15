from selenium import webdriver
from driver_options import options, service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class Driver:

    wait_element = "pdp-questions-entry-point__text"
    wait_element_string = "Задать вопрос"
    header_name = "pdp-header__title"

    def __init__(self,
                smm_link=str) -> None: 
        self.smm_link = smm_link
        self.driver = webdriver.Chrome(
            options=options,
            service=service
        )

    def get_tile(self) -> str:
        self.driver.get(self.smm_link)

        _ = WebDriverWait(driver=self.driver, timeout=3).until(
            EC.text_to_be_present_in_element(
            (By.CLASS_NAME, self.wait_element),
            self.wait_element_string))

        title = self.driver.find_element(By.CLASS_NAME, self.header_name)

        return title
    
    def quit(self):
        self.driver.quit()

    