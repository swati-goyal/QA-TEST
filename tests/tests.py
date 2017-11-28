import unittest
import json
from selenium import webdriver
import os


class TestForm(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # Get test data from json object
        inst.path = os.getcwd()
        inst.tdata = json.load(open(inst.path + '\\data.json'))

        # Set up driver and open url
        inst.driver = webdriver.Chrome(inst.tdata["drivers-path"]["chrome"])
        inst.driver.get(inst.tdata["website-data"]["url"])

    @unittest.skip
    def test_url(self):
        title = self.driver.title
        page_title = self.driver.find_element_by_xpath(self.tdata["website-data"]["title"])
        self.assertEqual(page_title.text, 'Registration Form', 'You are hitting the wrong Url!')

    @classmethod
    def tearDownClass(inst):
        inst.driver.close()
        pass


