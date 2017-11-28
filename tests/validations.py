import unittest
import json
from selenium import webdriver
import os


class ValidateForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Get test data from json object
        cls.path = os.getcwd()
        cls.tdata = json.load(open(cls.path + '\\data.json'))

        # Set up driver and open url
        cls.driver = webdriver.Chrome(cls.tdata["drivers-path"]["chrome"])
        cls.driver.get(cls.tdata["website-data"]["url"])

    @unittest.skip
    def test_fname_field(self):
        first_name = self.driver.find_element_by_xpath(self.tdata["website-data"]["f-name"])
        self.assertIsNotNone(first_name, "First Name field not present")

    @unittest.skip
    def test_lname_field(self):
        last_name = self.driver.find_element_by_xpath(self.tdata["website-data"]["l-name"])
        self.assertIsNotNone(last_name, "Last Name field not present")

    @unittest.skip
    def test_dept_name_field(self):
        dept_name = self.driver.find_elements_by_xpath(self.tdata["website-data"]["dept-name"])
        self.assertIsNotNone(len(dept_name), "Department field not present")

    @unittest.skip
    def test_user_name_field(self):
        user_name = self.driver.find_element_by_xpath(self.tdata["website-data"]["username"])
        self.assertIsNotNone(user_name, "User name field not present")

    @unittest.skip
    def test_password_field(self):
        password = self.driver.find_element_by_xpath(self.tdata["website-data"]["password"])
        self.assertIsNotNone(password, "First Name field not present")

    @unittest.skip
    def test_confirm_password_field(self):
        confirm_password = self.driver.find_element_by_xpath(self.tdata["website-data"]["confirm-pass"])
        self.assertIsNotNone(confirm_password, "Confirm Password field not present")

    @unittest.skip
    def test_email_field(self):
        email = self.driver.find_element_by_xpath(self.tdata["website-data"]["email"])
        self.assertIsNotNone(email, "Email field not present")

    @unittest.skip
    def test_mobile_field(self):
        phone_number = self.driver.find_element_by_xpath(self.tdata["website-data"]["mobile"])
        self.assertIsNotNone(phone_number, "Mobile Number field not present")

    def test_first_name_validation(self):
        first_name = self.driver.find_element_by_xpath(self.tdata["website-data"]["f-name"])
        first_name.send_keys("S")
        submit = self.driver.find_element_by_xpath(self.tdata["website-data"]["submit"])

        if submit.is_enabled():
            submit.click()

        failure_msg = self.driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[1]/div/small[1]')
        self.assertTrue(failure_msg.is_displayed(), "Not validated")

    def test_last_name_validation(self):
        last_name = self.driver.find_element_by_xpath(self.tdata["website-data"]["l-name"])
        last_name.send_keys("G")
        submit = self.driver.find_element_by_xpath(self.tdata["website-data"]["submit"])

        if submit.is_enabled():
            submit.click()

        failure_msg = self.driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[2]/div/small[1]')
        self.assertTrue(failure_msg.is_displayed(), "Not validated")

    def test_email_format(self):
        email = self.driver.find_element_by_xpath(self.tdata["website-data"]["email"])
        email.send_keys("sw@ti.g")
        invalid_msg = self.driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[7]/div/small[2]")
        self.assertTrue(invalid_msg.is_displayed(), "Not validated")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

