# -*- coding: utf-8 -*-

import datetime
import os
import subprocess
from distutils.spawn import find_executable


class ADB(object):
    # 全局变量,用于标记
    FLAG = ''

    adb_path = find_executable("adb")

    if not adb_path:
        print('adb path not found.')
        exit()

    def setFlag(self, flag):
        global FLAG
        FLAG = flag

    def getFlag(self):
        return FLAG

    def serial_no(self):
        """
        获取手机序列号
        :return:
        """
        if os.name == 'nt':
            return self.cmd("shell getprop | findstr ro.serialno").split(': ')[1]
        else:
            return self.cmd("shell getprop | grep ro.serialno").split(': ')[1]

    def getPackage(self):
        """
        获取包名
        :return:
        """
        return self.read_cmd('shell pm list package')


    def execute(self, command):
        """
        开启一个execute窗口并且执行command_text命令，将stdout输出到指定文件中
        :param command:  adb 命令
        :return: 返回输出流
        """

        os.makedirs("../TestData", exist_ok=True)
        command_result = ''
        command_text = 'adb %s ' % command
        if self.getFlag() == "COLD":
            write_text = open("../TestData/cold_raw_data.txt", 'a+')
        else:
            write_text = open("../TestData/hot_raw_data.txt", 'a+')
        try:
            pipe = subprocess.Popen(command_text, shell=True, stdout=write_text).stdout
        finally:
            write_text.close()
        while True:
            line = pipe
            if not line:
                break
            command_result += line

    def cmd(self, command):
        """
        单一执行cmd指令，没有对log进行存储操作
        :param command:   adb 命令
        :return:
        """
        command_result = ''
        command_text = 'adb %s ' % command
        results = os.popen(command_text, 'r')
        while True:
            line = results.read()
            if not line: break
            command_result += line
        return command_result

    def read_cmd(self, cmd):
        """
        这里主要用来获取包名
        :param cmd:
        :return:
        """
        command_text = 'adb %s ' % cmd
        results = subprocess.Popen(command_text, shell=True, stdout=subprocess.PIPE)
        result = []
        for i in results.stdout.readlines():
            result.append(str(i).split(':')[1].split("\\")[0])
        return result

    def devices(self):
        """
        获取手机列表
        :return:
        """
        result = self.cmd("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        return [device for device in devices if len(device) > 2]

    def push(self, from_computor, to_phone):
        """
        push 文件到手机
        :param from_computor:   电脑文件位置
        :param to_phone:    手机文件位置
        :return:
        """
        return self.cmd("push " + from_computor + " " + to_phone)

    def pull(self, from_phone, to_computor):
        '''
        pull 手机文件到电脑
        :param from_phone: 手机文件位置
        :param to_computor: 电脑文件位置
        :return: 
        '''
        return self.cmd("pull " + from_phone + " " + to_computor)

    def install(self, apk_path):
        """
        覆盖安装apk,并且默认允许了所有权限
        :param apk_path: apk路径
        :return:
        """
        return self.cmd("install -r -g " + apk_path)

    def uninstall(self, package):
        """
        卸载 APK
        :param package: 包名
        :return:
        """
        return self.cmd("shell pm uninstall " + package)

    def shell(self, command):
        """
         进入adb shell环境
        :param command:
        :return:
        """
        return self.execute("shell " + command)

    def start(self, activity):
        """
        启动一个activity界面
        activity: 指定activity
        :param activity:
        :return:
        """
        return self.execute("shell am start -W " + activity)

    def force_stop(self, package):
        """
        强制停止应用
        :param package: 应用包名
        :return:
        """
        return self.execute(" shell am force-stop " + package)

    def getLogcat(self, command):
        """
        获取 logcat
        参数: -d 将缓存的日志输出到屏幕上，并且不会堵塞
        -f 定义日志输出的文件位置，例如： adb logcat -f /sdcard/log.txt
        :param command:
        :return:
        """
        return self.execute("logcat -d " + command)

    def getLogcatString(self, str):
        """
        获取指定字段的 logcat
        :param str:
        :return:
        """
        if os.name == 'nt':  # Windows 系统
            return self.getLogcat("| findstr " + str)
        else:
            return self.getLogcat("| grep " + str)

    def clearLogcat(self):
        """
        清除logcat
        :return:
        """
        return self.getLogcat("-c")

    def screenShot(self):

        #   获取系统当前时间
        now = datetime.datetime.now()  # 时间数组格式

        #   转换为指定格式时间戳
        timestamp = now.strftime("%Y%m%d%H%M%S")

        return self.execute("shell screencap -p /mnt/sdcard/ScreenShot/screen_shot" + timestamp + ".png")
