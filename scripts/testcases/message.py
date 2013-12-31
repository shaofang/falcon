#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class MessageTest(unittest.TestCase):
    def setUp(self):
        super(MessageTest, self).setUp()
        d.wakeup()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        u.backHome(d)

    def tearDown(self):
        super(MessageTest, self).tearDown()
        u.backHome(d)

    def testMO_MTSms(self):
        str_receiver = '10010'
        str_content = 'Message Test Content'
        #assert d.exists(text='Messaging') , 'message app not appear on the home screen'
        #assert d.exists(text='Apps')  , 'apps not appear on the home screen'
        #d(text='Messaging').click.wait()

        d.start_activity(component='com.android.mms/.ui.ConversationList')
        assert d(text='Messaging').wait.exists(timeout=3000), 'can not launch message in 3s'

        #Delete messages
        if not d(text="No conversations.").wait.exists(timeout=2000):
            d.press('menu')
            d(text='Delete all threads').click.wait()
            d(text='Delete', className='android.widget.Button').click.wait()
            assert d(text="No conversations.").wait.exists(timeout=3000), 'Delete message failed'

        d(description='New message').click.wait()
        d(text='To').set_text(str_receiver)
        assert d(text=str_receiver).wait.exists(timeout=10000), 'receiver number input error'            
        d(text='Type message').set_text(str_content)
        assert d(text=str_content).wait.exists(timeout=10000), 'content input error'            
        d(description='Send', className='android.widget.ImageButton').click.wait()

        assert d(text='SENDING…').wait.exists(timeout=10000), 'Sending not start in 10s'
        assert d(text='SENDING…').wait.gone(timeout=20000), 'sms sending failed in 20s'
        d.sleep(15)
        assert d(textStartsWith='尊敬的').wait.exists(timeout=20000), 'No feedback in 35s'

    def testMoMMS(self):
        str_receiver = '13501101339'
        str_content = 'Message Test Content'
        d.start_activity(component='com.android.mms/.ui.ConversationList')

        if not d(text="No conversations.").wait.exists(timeout=2000):
            d.press('menu')
            d(text='Delete all threads').click.wait()
            d(text='Delete', className='android.widget.Button').click.wait()
            assert d(text="No conversations.").wait.exists(timeout=3000), 'Delete message failed'

        d(description='New message').click.wait()
        d(text='To').set_text(str_receiver)
        #assert d(text=str_receiver).wait.exists(timeout=10000), 'receiver number input error'            
        d(text='Type message').set_text(str_content)
        #assert d(text=str_content).wait.exists(timeout=10000), 'content input error'            
        #d(description='Send', className='android.widget.ImageButton').click.wait()

        d(description='Attach').click.wait()
        assert d(text='Capture picture').wait.exists(timeout=3000), 'no adding attachment panel' 
        d(text='Capture picture').click.wait()
        assert d(description='Shutter button').wait.exists(timeout=3000), 'no camera' 
        d(description='Shutter button').click.wait()
        d.sleep(1)
        assert d(description='Review done').wait.exists(timeout=3000), 'Take picture failed.'
        d(description='Review done').click.wait()
        assert d(text='MMS', description='Send MMS').wait.exists(timeout=3000), 'add attachment failed'
        d(text='MMS', description='Send MMS').click.wait()
        assert d(text='SENDING…').wait.exists(timeout=10000), 'No sending status'
        d.sleep(30)
        assert d(text='SENDING…').wait.gone(timeout=20000), 'MMS sending failed in 50s'



            

