#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
import time
from devicewrapper.android import device as d
import util as u

class PhoneTest(unittest.TestCase):
    def setUp(self):
        super(PhoneTest, self).setUp()
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(PhoneTest, self).tearDown()
        if d(description="End"):
            d(description="End").click.wait()
        u.backHome(d)

    def testMoCall(self):
        #assert d.exists(text='Phone') , 'Phone app not appear on home screen'
        #assert d.exists(text='Apps')
        #d(text='Phone').click.wait()
        d.start_activity(component='com.android.contacts/.activities.DialtactsActivity')

        assert d(description='dial', className='android.widget.ImageButton').wait.exists(timeout=3000), 'Launch dialer failed in 3s'
        
        d(description='one').click()
        d(description='zero').click()
        d(description='zero').click()
        d(description='one').click()
        d(description='zero').click()
        assert d.exists(text="10010") , 'Input number error!'
        
        #Click the call button
        d(description='dial', className='android.widget.ImageButton').click.wait()
        
        #Wait 'Dialing' to see if begin to dial, and wait 'Dialing' disappear to see if connected. 
        #Wait '0:10' to see if duration is over 10s.  
        assert d(text="Dialing").wait.exists(timeout=10000), 'Should begin to dialing in 10 secs'
        assert d(text="Dialing").wait.gone(timeout=10000), 'Should connect in 10 secs'
        assert d(text="0:10").wait.exists(timeout=20000), 'call duration should be 10 secs'
        assert d(description="End").wait.exists(timeout=3000), 'End call button should displayed.'

        d(description="End").click.wait()
        assert d(description='dial').wait.exists(timeout=5000), ''
        #d.sleep(3)


