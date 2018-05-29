# -*- coding:utf-8 -*-

from base.Adb import ADB
import time

class ColdStartupTest(object):


    """
    冷启动,启动目标activity作为的参数
    参数activityName:应用名称，如CONTACTS,MESSAGE
    """
    def coldTest(self, activityName):

        adb = ADB()
        # 使log输出到cold_test_raw-data.txt文件中
        adb.setFlag('COLD')
        # 开始测试前先kill掉，防止后台运行
        adb.force_stop(activityName.split('/')[0]) # 从activity中切割包名
        time.sleep(3.0)

        for t in range(10):
            print("第 " + str(t + 1) + " 次测试beginning...")
            # 启动一个activity
            adb.start(activityName)
            time.sleep(5.0)
            print("第 " + str(t + 1) + " 次测试正在获取字段..")
            # 获取logcat 的 displayed 字段
            adb.getLogcatString("Displayed")
            time.sleep(5.0)

            print("第 " + str(t + 1) + " 次测试获取字段结束..")
            # 强制停止应用
            adb.force_stop(activityName.split('/')[0])
            time.sleep(5.0)
            #   每次获取完log就要清除一次
            adb.clearLogcat()
            print("第 " + str(t + 1) + " 次测试ending...")
