# -*- coding: utf-8 -*-

from base.adb import ADB
import time

class HotStartupTest(object):

    def hotStartupTest(self):

        adb = ADB()
        for t in range(11):
            # 启动一个activity
            adb.start("com.android.contacts/.activities.PeopleActivity")
            time.sleep(5.0)
            print("第 " + str(t + 1) + " 次测试正在获取字段..")
            adb.getLogcatString("Displayed")
            time.sleep(5.0)
            print("第 " + str(t + 1) + " 次测试获取字段结束..")
            # 手机返回键，确保完全退出,返回操作3次
            adb.shell("input keyevent 4")
            adb.shell("input keyevent 4")
            adb.shell("input keyevent 4")

            #   每次获取完log就要清除一次
            adb.clearLogcat()
            time.sleep(5.0)

if __name__ == '__main__':

    HotStartupTest().hotStartupTest()