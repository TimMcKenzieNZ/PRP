import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from .django_test_base_class import DjangoTestBaseClass



class TestPRPPages(DjangoTestBaseClass):


    def test_load_application(self):
        """
        Test the MediaSuite dashboard page is correctly loaded by comparing the current url with the expected one
        """
        self.assertEqual(self.base_url + '/MediaSuite_2019_Campaign/dashboard', self.driver.current_url)

    def test_programme_select(self):
      """
      Tests the homepage button works correctly
      """
      self._select_element_by_id("PRP","PRP")
      self.assertEqual(self.base_url + '/', self.driver.current_url) # have to add a '/' because ember does :L

    def test_load_benefits(self):
      """
      Test if the benefit page is loaded correctly
      """
      self._select_element_by_id('benefit', 'benefit page')
      self.assertEqual(self.driver.current_url, '{}/MediaSuite_2019_Campaign/benefits'.format(self.base_url))

    def test_app_walk_through_priority_to_delivery(self):
      """
      Tests that the main elements of the priority page is visible and that we can navigate to the delivery page through a selected initiative
      """
      self._select_element_by_id('priority', 'priority page')
      self._select_element_by_id('Making MediaSuite Great again', 'Making MediaSuite Great again statistics')
      time.sleep(1)

      # Checking elements exist as expected: project description, project goal, project manager
      self.assertTrue(self._check_element_exists('Making MediaSuite Great again description'))
      self.assertTrue(self._check_element_exists('Making MediaSuite Great again More Learning Lunches'))
      self.assertTrue(self._check_element_exists('Tim'))

      # Loading next page and checking it loads correctly
      self._select_element_by_id('Construct the Wall statistics', 'delivery page')
      self.assertTrue(self._check_element_exists('delivery page'))

      
    def test_app_walk_through_delivery_to_change(self):
      """
      Tests if that the main elements of the delivery page is visible and that we can navigate to the change page via a selected deliverable
      """
      self._select_element_by_id('delivery', 'delivery page')
      self._select_element_by_id('Construct the Wall', 'Construct the Wall statistics')

      # Loading next page and checking it loads correctly
      self._select_element_by_id('Procure Bricks', 'change page')

    def test_app_change_looking_at_updates(self):
      """
      Tests that the main elements of the change page are visible and that we can show & hide update comments
      """
      self._select_element_by_id('change', 'change page')
      self.assertTrue(self._check_element_exists('Tweet on Social Media'))
      self.assertTrue(self._check_element_exists('2 comments'))

      # open comments
      self._select_element_by_id('2 comments', 'Hide')
      self.assertTrue(self._check_element_exists('Tim'))

      # close comments
      self._select_element_by_id('Hide', '2 comments')
      self.assertFalse(self._check_element_exists('Tim'))


