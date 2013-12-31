#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest, self).setUp()
        d.wakeup()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        u.backHome(d)

    def tearDown(self):
        super(CameraTest, self).tearDown()
        u.backHome(d)

    def testTakePicture(self):
        #assert d.exists(text='Camera') , 'camera app not appear on home screen'
        #assert d.exists(text='Apps')
        #d(text='Camera').click.wait()
        d.start_activity(component='com.android.gallery3d/com.android.camera.CameraLauncher')
        assert d(description='Shutter button').wait.exists(timeout=5000), 'can not launch camera in 5s'

        d(description='Shutter button').click.wait()
        d.sleep(1)
        d().swipe.left()
        assert d(description='Share with').wait.exists(timeout=3000), 'take picture failed'

        d.press('menu')
        d(text='Delete').click.wait()
        d(text='OK').click.wait()
        d().swipe.right()

        assert d(description='Shutter button').wait.exists(timeout=5000), 'Back to camera failed.'
