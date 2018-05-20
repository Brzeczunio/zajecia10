import unittest
import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestAndroidApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        # platform
        desired_caps['platformName'] = 'Android'
        # platform version
        desired_caps['platformVersion'] = '7.0'
        # mobile app
        desired_caps['app'] = PATH('C:\APP\ApiDemos-debug.apk')
        # device name
        desired_caps['deviceName'] = 'Gigaset GS160'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        # Polaczenie z APPIUM SERVER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # close the browser window
        self.driver.quit()

    def test_is_app_uninstalled(self):
        self.driver.remove_app('io.appium.android.apis')
        self.assertFalse(self.driver.is_app_installed('io.appium.android.apis'))

    def test_is_app_installed(self):
        self.assertTrue(self.driver.is_app_installed('io.appium.android.apis'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAndroidApp)
    unittest.TextTestRunner(verbosity=2).run(suite)