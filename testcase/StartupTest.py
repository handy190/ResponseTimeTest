# -*- coding:utf-8 -*-

from base.Adb import ADB
import time
import os

"""
    冷启动,启动目标activity作为的参数
    参数activityName:应用名称，如CONTACTS,MESSAGE
    
    实践证明：Total Time 的值和displayed的值是一样的，
             所以提取Total Time的值更简单一些，displayed的值有可能会获取不到或者有遗漏
"""


class StartupTest(object):

    """
    测试开始前先删除已存在的log文件
    """
    def delete_log_file(self):
        cold_log_file = "../TestData/cold_raw_data.txt"
        hot_log_file = "../TestData/hot_raw_data.txt"
        # 每次运行测试前先移除log文件
        if os.path.exists(cold_log_file):
            os.remove(cold_log_file)
            print("删除: %s" % cold_log_file)
        if os.path.exists(hot_log_file):
            os.remove(hot_log_file)
            print("删除: %s" % hot_log_file)

    """
    冷启动测试用例
    """
    def cold_test(self, activity_name):
        log_file = "../TestData/cold_raw_data.txt"
        adb = ADB()
        # 使log输出到cold_raw-data.txt文件中
        adb.setFlag('COLD')
        # 开始测试前先kill掉，防止后台运行
        adb.force_stop(activity_name.split('/')[0])  # 从activity中切割包名
        # 终止所有后台进程
        adb.execute("shell am kill-all")

        #   每次执行前清除一次log
        adb.clearLogcat()
        time.sleep(5.0)

        for i in range(10):

            # 将调试信息写入log文本中。  注：with 语句维护一个上下文，结束后会自动关闭流操作
            with open(log_file, 'a+') as f1:
                f1.write(activity_name.split('/')[0] + "第 " + str(i + 1) + " 次 cold test beginning...\r\n")
            print(activity_name.split('/')[0] + "第 " + str(i + 1) + " 次 cold test beginning...")
            # 启动一个activity, -S 启动Activity前强行停止目标应用(冷启动)
            adb.start("-S " + activity_name)
            time.sleep(10.0)
            # 获取logcat 的 displayed 字段
            adb.getLogcatString("Displayed")
            time.sleep(5.0)
            # 强制停止应用
            adb.force_stop(activity_name.split('/')[0])
            time.sleep(5.0)
            #   每次获取完log就要清除一次
            adb.clearLogcat()
            print(activity_name.split('/')[0] + "第 " + str(i + 1) + " 次 cold test ending...")
            with open("../TestData/cold_raw_data.txt", 'a+') as f1:
                f1.write(activity_name.split('/')[0] + "第 " + str(i + 1) + " 次 cold test ending...\r\n")
            time.sleep(3.0)

    """
    热启动测试用例
    """
    def hot_test(self, activity_name):

        test_file = "../TestData/hot_raw_data.txt"
        adb = ADB()
        # 使log输出到hot_raw-data.txt文件中
        adb.setFlag("HOT")
        # 制造一次热启动条件,不会记录时间到log文本中
        adb.cmd("shell am start -W " + activity_name)
        time.sleep(5.0)
        # 点击home键
        adb.shell("input keyevent 4")
        time.sleep(5.0)
        # 每次执行前清除一次log
        adb.clearLogcat()
        time.sleep(3.0)

        for i in range(10):

            # 将调试信息写入log文本中。  注：with 语句维护一个上下文，结束后会自动关闭流操作
            with open(test_file, 'a+') as f1:
                f1.write(activity_name.split('/')[0] + "第 " + str(i + 1) + " 次 hot test beginning...\r\n")
            print(activity_name.split('/')[0] + "第 " + str(i + 1) + " 次 hot test beginning...")
            # 启动一个activity
            adb.start(activity_name)
            time.sleep(10.0)
            adb.getLogcatString("Displayed")
            time.sleep(5.0)
            # 点击home键
            adb.shell("input keyevent 4")

            #   每次获取完log就要清除一次
            adb.clearLogcat()
            time.sleep(5.0)

            print(activity_name.split('/')[0] + "第 " + str(i + 1) + " 次 hot test ending...")
            with open(test_file, 'a+') as f1:
                f1.write(activity_name.split('/')[0] + "第 " + str(i + 1) + " 次 hot test ending...\r\n")
            time.sleep(3.0)