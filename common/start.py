# coding:utf-8
from appium import webdriver

des_leidian = {
                "platformName": "Android",
                "deviceName": "GUR4C19408000505",
                "platformVersion": "9",
                "appPackage": "com.mmc.feelsowarm",
                "appActivity": "com.mmc.feelsowarm.WelcomeActivity",
                'unicodeKeyboard': True,   # appium自带键盘
                'resetKeyboard': True,     # 解决中文乱码问题
                "noReset": True,
                }

des_yeshen = {
                "platformName": "Android",
                "deviceName": "6LZSN77L99999999",
                "platformVersion": "5.0.1",
                "appPackage": "com.mmc.feelsowarm",
                "appActivity": "com.mmc.feelsowarm.WelcomeActivity",
                "noReset": True,
                "udid": "6LZSN77L99999999",  # 识别手机唯一标识
                "autoGrantPermissions": True,
                'unicodeKeyboard': True,   # appium自带键盘
                'resetKeyboard': True,     # 解决中文乱码问题
                }


def start_app(deviceName="leidian", port=4723):
    '''启动app'''
    if deviceName == "leidian":
        des = des_leidian
    elif deviceName == "yeshen":
        des = des_yeshen
    else:
        des = des_leidian
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % port, des)
    return driver
if __name__ == '__main__':
    driver = start_app()