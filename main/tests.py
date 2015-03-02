from django.test import TestCase

# Create your tests here.

from django.test import LiveServerTestCase
from selenium import webdriver
import time

class BaseTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


class ImportTest(TestCase):

    def test_import_journal(self):
        from catalog.tasks import import_now 
        import_now(70833) 


class LoginTest(BaseTest):

    def test_login_form_html(self):
        # Edith goes to the home page
        self.browser.get('http://localhost:8008')
        # find login inbox
        username = self.browser.find_element_by_name('username')
        password = self.browser.find_element_by_name('password')
        time.sleep(2)
