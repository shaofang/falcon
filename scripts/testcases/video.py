#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class VideoTest(unittest.TestCase):
    def setUp(self):
        super(VideoTest, self).setUp()
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(VideoTest, self).tearDown()
        u.backHome(d)

    def testVideoPlayer(self):
        #Find and launch Video app
        #assert d.exists(text='Video') , 'Video app not appear on the home screen'
        #d(text='Video').click.wait()
        #d.start_activity(component='com.miui.video/.HomeActivity')
        d.start_activity(component='com.android.gallery3d/.app.Gallery')
        assert d(text='Albums').wait.exists(timeout=3000), 'Gallery app can not be launched.'
        d.click('movies.png')
        d.click('play.png')
        d.sleep(600)
        d.press('back')
        

