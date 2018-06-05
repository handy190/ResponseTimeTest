# -*- coding:utf-8 -*-

from base.Adb import ADB
import time

"""
    冷启动,启动目标activity作为的参数
    参数activityName:应用名称，如CONTACTS,MESSAGE
"""

class StartupTest(object):

    """
    冷启动测试用例
    """
    def coldTest(self, activityName):

        adb = ADB()
        # 使log输出到cold_raw-data.txt文件中
        adb.setFlag('COLD')
        # 开始测试前先kill掉，防止后台运行
        adb.force_stop(activityName.split('/')[0]) # 从activity中切割包名
        # 终止所有后台进程
        adb.execute("shell am kill-all")

        #   每次执行前清除一次log
        adb.clearLogcat()
        time.sleep(5.0)

        for t in range(10):
            print(activityName.split('/')[0] + "第 " + str(t + 1) + " 次cold test beginning...")
            # 启动一个activity, -S 启动Activity前强行停止目标应用(冷启动)
            adb.start("-S " + activityName)
            time.sleep(10.0)
            # 获取logcat 的 displayed 字段
            adb.getLogcatString("Displayed")
            time.sleep(5.0)
            # 强制停止应用
            adb.force_stop(activityName.split('/')[0])
            time.sleep(5.0)
            #   每次获取完log就要清除一次
            adb.clearLogcat()
            print(activityName.split('/')[0] + "第 " + str(t + 1) + " 次cold test ending...")


    """
    热启动测试用例
    """
    def hotStartupTest(self, activityName):

        adb = ADB()
        # 使log输出到hot_raw-data.txt文件中
        adb.setFlag("HOT")

        # 制造一次热启动条件
        adb.start(activityName)
        time.sleep(5.0)
        # 点击home键
        adb.shell("input keyevent 3")
        time.sleep(5.0)
        #   每次执行前清除一次log
        adb.clearLogcat()
        time.sleep(3.0)

        for t in range(10):
            print(activityName.split('/')[0] + "第 " + str(t + 1) + " 次hot test beginning...")
            # 启动一个activity
            adb.start(activityName)
            time.sleep(10.0)
            adb.getLogcatString("Displayed")
            time.sleep(5.0)
            # 点击home键
            adb.shell("input keyevent 3")

            #   每次获取完log就要清除一次
            adb.clearLogcat()
            time.sleep(5.0)

            print(activityName.split('/')[0] + "第 " + str(t + 1) + "次hot test ending...")