# coding:utf-8
import unittest
import time
from pages.login_page import LoginPage
from common.logger import Log
from pages.accom_page import Voice
from pages.find_page import Cancel
from pages.listen_page import Live
from pages.ming_page import More
from common.start import start_app


class Test_01(unittest.TestCase):
    '''陪聊页面'''
    @classmethod
    def setUpClass(cls):
        time.sleep(10)
        cls.driver = start_app()
        cls.log = Log()
        cls.login = LoginPage(cls.driver)
        cls.voice = Voice(cls.driver)
        cls.cancel = Cancel(cls.driver)
        cls.driver.implicitly_wait(20)

    # def test_01(self):
    #     '''测试登录功能点：输入账号密码点击登录'''
    #     self.login.step_01()
    #     self.login.step_02()
    #     self.login.step_03()
    #     self.login.step_04()
    #     self.login.step_05()
    #     self.login.step_06()
    #     self.login.step_07()
    #     self.login.step_08()

    def test_02(self):
        '''陪聊页面-测试邀约功能点:选择15分钟点击立即邀约'''
        self.voice.step_01()

    def test_03(self):
        '''陪聊页面-测试邀约功能点:选择15分钟点击立即邀约'''
        self.voice.step_02()

    def test_04(self):
        '''陪聊页面-测试拉黑功能点'''
        self.voice.step_03()

    def test_05(self):
        '''陪聊页面-测试举报功能点'''
        self.voice.step_04()

    def test_06(self):
        '''陪聊页面-测试关注功能点'''
        self.voice.step_05()

    def test_07(self):
        '''陪聊页面-测试TA的主页:邀他传图功能点'''
        self.voice.step_06()

    def test_08(self):
        '''陪聊页面-测试TA的主页，分享我的图片'''
        self.voice.step_07()

    def test_09(self):
        '''陪聊页面-测试TA的主页，分享-保存到相册'''
        self.voice.step_08()

    def test_10(self):
        '''陪聊页面-获取该用户看过的数量'''
        self.voice.step_09()

    def test_11(self):
        '''陪聊页面-获取该用户关注数量'''
        self.voice.step_10()

    def test_12(self):
        '''陪聊页面-获取该用户粉丝数量'''
        self.voice.step_11()

    def test_13(self):
        '''陪聊页面-获取该用户暖流号'''
        self.voice.step_12()


class Test_02(unittest.TestCase):
    '''动态页面'''
    @classmethod
    def setUpClass(cls):
        time.sleep(10)
        cls.driver = start_app()
        cls.log = Log()
        cls.cancel = Cancel(cls.driver)
        cls.driver.implicitly_wait(20)

    def test_01(self):
        '''陪聊页面-测试邀约功能点:选择15分钟点击立即邀约'''
        self.cancel.step_01()
        time.sleep(5)

    def test_02(self):
        '''陪聊页面-测试邀约功能点:选择15分钟点击立即邀约'''
        self.cancel.step_02()

    def test_03(self):
        '''陪聊页面-测试拉黑功能点'''
        self.cancel.step_03()

    def test_04(self):
        '''陪聊页面-测试举报功能点'''
        self.cancel.step_04()
        time.sleep(5)

    def test_05(self):
        '''陪聊页面-测试关注功能点'''
        self.cancel.step_05()

    def test_06(self):
        '''发布动态:文字'''
        self.cancel.step_06()

    def test_07(self):
        '''发布动态:图片'''
        self.cancel.step_07()

    def test_08(self):
        '''发布动态:音频'''
        self.cancel.step_08()

    def test_09(self):
        '''测试举报功能点'''

        self.cancel.step_09()


class Test_03(unittest.TestCase):
    '''消息页面'''
    @classmethod
    def setUpClass(cls):
        time.sleep(10)
        cls.driver = start_app()
        cls.log = Log()
        cls.live = Live(cls.driver)
        cls.driver.implicitly_wait(20)

    def test_01(self):
        '''测试发起私信功能点'''
        self.live.step_01()

    def test_02(self):
        '''测试清空私信功能点'''
        self.live.step_02()

    def test_03(self):
        '''测试新用户功能点'''
        self.live.step_03()

    def test_04(self):
        '''测试评论功能点'''
        self.live.step_04()

    def test_05(self):
        '''测试看过功能点'''
        self.live.step_05()

    def test_06(self):
        '''测试粉丝功能点'''
        self.live.step_06()


class Test_04(unittest.TestCase):
    '''我的页面'''
    @classmethod
    def setUpClass(cls):
        cls.driver = start_app()
        cls.log = Log()
        cls.more = More(cls.driver)
        cls.driver.implicitly_wait(20)

    def test_01(self):
        '''测试-发起私信功能点'''
        time.sleep(7)
        self.more.step_01()
        time.sleep(7)

    def test_02(self):
        '''测试-清空私信功能点'''
        self.more.step_02()

    def test_03(self):
        '''测试-新用户功能点'''
        self.more.step_03()

    def test_04(self):
        '''测试-评论功能点'''
        self.more.step_04()

    def test_06(self):
        '''测试-看过功能点'''
        self.more.step_06()

    def test_07(self):
        '''测试-我的-设置-个人资料'''
        self.more.step_07()

    def test_08(self):
        # self.more.step_08()
        pass

    def test_09(self):
        '''测试-我的-设置-陪伴师管理'''
        self.more.step_09()

    def test_10(self):
        '''测试-我的-设置-通知设置-私信'''
        self.more.step_10()

    def test_11(self):
        '''测试-我的-设置-通知设置-关注的人发内容'''
        self.more.step_11()

    def test_12(self):
        '''测试-我的-设置-通知设置-倾听开播'''
        self.more.step_12()

    def test_13(self):
        '''测试-我的-设置-隐私设置-谁可以发私信给我'''
        self.more.step_13()

    def test_14(self):
        '''测试-我的-设置-隐私设置-黑名单'''
        self.more.step_14()

    def test_15(self):
        '''测试-我的-设置-隐私设置-私信自动回复'''
        self.more.step_15()

    def test_16(self):
        '''测试-我的-设置-隐私设置-私信自动打招呼内容'''
        self.more.step_16()

    def test_17(self):
        '''测试-我的-设置-清除缓存'''
        self.more.step_17()

    def test_18(self):
        '''测试-我的-设置-网络流量提醒'''
        self.more.step_18()

    def test_19(self):
        '''测试-我的-我的钱包-获取充值钱包余额'''
        self.more.step_19()

    def test_20(self):
        '''测试-我的-我的钱包-获取收益钱包余额'''
        self.more.step_20()

    def test_21(self):
        '''测试-我的-我的钱包-获取陪伴师钱包余额'''
        self.more.step_21()

    def test_22(self):
        '''测试-我的-我的钱包-钱包明细-支出N币'''
        self.more.step_22()

    def test_23(self):
        '''测试-我的-我的钱包-钱包明细-收入N币-功能点'''
        self.more.step_23()

    def test_24(self):
        '''测试-我的-财富等级-功能点'''
        self.more.step_24()


if __name__ == "__main__":
    unittest.main()

