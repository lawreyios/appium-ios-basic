import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class LoginTests(unittest.TestCase):

    def setUp(self):
        app = ('/Users/lawrey/Library/Developer/Xcode/DerivedData/AppiumTest-fubxvjmcpxiewkenopxpcerwhudw/Build/Products/Debug-iphonesimulator/AppiumTest.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '11.4',
                'deviceName': 'iPhone 6s'
            }
        )

    def tearDown(self):
        self.driver.quit()

    def testEmailField(self):
        emailTF = self.driver.find_element_by_accessibility_id('emailTextField')
        emailTF.send_keys("validEmail")
        emailTF.send_keys(Keys.RETURN)
        sleep(1)
        self.assertEqual(emailTF.get_attribute("value"), "validEmail")

    def testPasswordField(self):
        passwordTF = self.driver.find_element_by_accessibility_id('passwordTextField')
        passwordTF.send_keys("validPW")
        passwordTF.send_keys(Keys.RETURN)
        sleep(1)
        self.assertNotEqual(passwordTF.get_attribute("value"), "validPW")

    def testLogin(self):
        self.testEmailField()
        self.testPasswordField()
        self.driver.find_element_by_accessibility_id('loginButton').click()
        sleep(1)
        smiley = self.driver.find_element_by_accessibility_id('smileyImage')
        self.assertTrue(smiley.get_attribute('wdVisible'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
