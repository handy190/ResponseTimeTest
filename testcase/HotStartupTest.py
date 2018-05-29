# -*- coding: utf-8 -*-

import time

from base.Adb import ADB


class HotStartupTest(object):

    def hotStartupTest(self, activityName):

        adb = ADB()
        adb.setFlag("HOT")

        for t in range(11):
            # 启动一个activity
            adb.start(activityName)
            time.sleep(5.0)
            print("第 " + str(t + 1) + " 次测试正在获取字段..")
            adb.getLogcatString("Displayed")
            time.sleep(5.0)
            print("第 " + str(t + 1) + " 次测试获取字段结束..")
            # 手机返回键，确保完全退出,返回操作3次
            adb.shell("input keyevent 4")
            # adb.shell("input keyevent 4")
            # adb.shell("input keyevent 4")

            #   每次获取完log就要清除一次
            adb.clearLogcat()
            time.sleep(5.0)

