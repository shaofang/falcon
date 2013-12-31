#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class BrowserTest(unittest.TestCase):
    def setUp(self):
        super(BrowserTest, self).setUp()
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(BrowserTest, self).tearDown()
        u.backHome(d)

    def testOpenBrowser_wifi(self):
        self.openBrowser(True)

    def testOpenBrowser_3g(self):
        self.openBrowser(False)


    def openBrowser(self, wifi):
        u.openWifi(d, wifi)
        #Launch browser
        d.start_activity(component='com.android.browser/.BrowserActivity')
        assert d(description='Page manager').wait.exists(timeout=5000), 'Launch browser failed in 5s'

        d(className='android.widget.EditText').set_text('wap.qq.com')
        d.press('enter')

        #Sleep 15s to wait loading web page
        d.sleep(15)
        if d.find('browser_blank.png'):
            assert False, 'Open the web page failed.'
        else:
            assert True




