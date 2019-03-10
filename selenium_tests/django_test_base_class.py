from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
import unittest
from dotenv import load_dotenv
from os.path import join, dirname
import os
import time

dotenv_path = join(dirname(__file__), '..', '.env')
if os.path.isfile(dotenv_path):
    load_dotenv(dotenv_path)


class DjangoTestBaseClass(unittest.TestCase):


    base_url = os.environ.get('SERVER_URL')

    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(5)
        # Attempt to load the MediaSuite Campaign page
        self.driver.get("{}/MediaSuite_2019_Campaign/dashboard".format(self.base_url))
        WebDriverWait(self.driver, 10).until( # We are lenient on the wait time as it can take time for ember to start
            ec.presence_of_element_located((By.CSS_SELECTOR, '.c-app-nav__programme'))
        )

    def tearDown(self):
        self.driver.close()

    
    def _check_element_exists(self, id):
        try:
            self.driver.find_element_by_id(id)
            return True
        except NoSuchElementException:
            return False
            
        
        
    def _select_element_by_id(self, element_id, expected_element_id):
        element_select = self.driver.find_element_by_id(element_id)
        element_select.click()
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, expected_element_id))
        )


