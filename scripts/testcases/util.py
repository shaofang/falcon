#!/usr/bin/python
# -*- coding:utf-8 -*- 
def openWifi(d, flag):
    d.start_activity(component='com.android.settings/.Settings')

    str_wifi='Wi-Fi'

    assert d(text=str_wifi).wait.exists(timeout=3000), 'can not launch settings in 3s'
    #d(text='Wi-Fi').click.wait()
    wifi = d(className='android.widget.LinearLayout').child_by_text(str_wifi).sibling(className='android.widget.Switch')
    #Should open wifi
    if flag:
        if wifi.text == 'OFF':
            d(text=str_wifi).click.wait()
            d(className='android.widget.Switch').click.wait()
            assert d(className='android.widget.Switch', text='ON').wait.exists(timeout=10000), "wifi can not be opened"
            d.sleep(5)
    #Should close the wifi
    else:
        if wifi.text == 'ON':
            d(text=str_wifi).click.wait()
            d(className='android.widget.Switch').click.wait()
            assert d(className='android.widget.Switch', text='OFF').wait.exists(timeout=10000), "wifi can not be opened"
            d.sleep(5)
        
    #Wait for network switching
    d.press('home')

def backHome(d):
	d.press('back')
	d.sleep(1)
	d.press('back')
	d.sleep(1)
	d.press('home')

