#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class MusicTest(unittest.TestCase):
    def setUp(self):
        super(MusicTest, self).setUp()
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(MusicTest, self).tearDown()
        u.backHome(d)

    def testMusicPlayer(self):
        #Find and launch Video app
        #assert d.exists(text='Music') , 'Music app not appear on the home screen'
        #d(text='Music').click.wait()

        #d.start_activity(component='com.miui.player/.ui.MusicBrowserActivity')
        d.start_activity(component='com.google.android.music/com.android.music.activitymanagement.TopLevelActivity')
        
        assert d(text='爸爸去哪儿').wait.exists(timeout=3000) , 'Music app can not be launched.'
        #assert d(className='android.widget.ImageView', index=2).wait.exists(timeout=3000) , 'play and stop button.'
        assert d(description='Play').wait.exists(timeout=3000)
        d(description='Play').click.wait()
        assert d(description='Pause').wait.exists(timeout=3000), 'Can not play'
        d.sleep(15)
        d(description='Pause').click.wait()
        assert d(description='Play').wait.exists(timeout=3000)