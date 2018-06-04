# -*- coding:utf-8 -*-

from base.Adb import ADB
from base.Activities import Activities
import time

"""
    冷启动,启动目标activity作为的参数
    参数activityName:应用名称，如CONTACTS,MESSAGE
"""

class StartupTest(object):


    def coldTest(self, activityName):

        adb = ADB()
        # 使log输出到cold_test_raw-data.txt文件中
        adb.setFlag('COLD')
        # 开始测试前先kill掉，防止后台运行
        adb.force_stop(activityName.split('/')[0]) # 从activity中切割包名
        time.sleep(3.0)

        for t in range(10):
            print("第 " + str(t + 1) + " 次cold test beginning...")
            # 启动一个activity
            adb.start(activityName)
            time.sleep(5.0)
            # 获取logcat 的 displayed 字段
            adb.getLogcatString("Displayed")
            time.sleep(5.0)
            # 强制停止应用
            adb.force_stop(activityName.split('/')[0])
            time.sleep(5.0)
            #   每次获取完log就要清除一次
            adb.clearLogcat()
            print("第 " + str(t + 1) + " 次cold test ending...")



    def hotStartupTest(self, activityName):

        adb = ADB()
        adb.setFlag("HOT")

        for t in range(11):
            print("第 " + str(t + 1) + " 次hot test beginning...")
            # 启动一个activity
            adb.start(activityName)
            time.sleep(5.0)
            adb.getLogcatString("Displayed")
            time.sleep(5.0)
            # 手机返回键，确保完全退出,返回操作3次
            adb.shell("input keyevent 4")
            # adb.shell("input keyevent 4")
            # adb.shell("input keyevent 4")

            #   每次获取完log就要清除一次
            adb.clearLogcat()
            time.sleep(5.0)

            print("第 " + str(t + 1) + "次hot test ending...")