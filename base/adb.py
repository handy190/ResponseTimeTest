# -*- coding: utf-8 -*-



import os
import platform
import string
import subprocess
import datetime



class ADB(object):

    def __init__(self, serial=None):
        self._serial = serial

    """获取手机序列号"""
    def serial(self):
        if self._serial:
            return self._serial
        if os.name == 'nt':
            self._serial = self.execute("getprop | findstr ro.serialno")
        else:
            self._serial = self.execute("getprop | grep ro.serialno")
        return self._serial

    """
    开启一个execute窗口并且执行command_text命令，将stdout输出到指定文件中
    """
    def execute(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        write_text = open(r"/Users/hongzhi/Test/raw_data.txt", "a+") # 每个应用对应一个文件比较合适
        pipe = subprocess.Popen(command_text, shell=True, stdout=write_text).stdout
        write_text.close()
        while True:
            line = pipe
            if not line: break
            command_result += line
        return command_result

    """
    获取手机列表
    """
    def devices(self):
        result = self.execute("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        return [device for device in devices if len(device) > 2]


    """push 文件到手机"""
    def push(self, from_computor, to_phone):
        return self.execute("push " + from_computor + " " + to_phone)


    """pull 手机文件"""
    def pull(self, from_phone, to_computor):
        return self.execute("pull " + from_phone + " " + to_computor)


    """覆盖安装apk,并且默认允许了所有权限"""
    def install(self, apk_path):
        return self.execute("install -r -g " + apk_path)

    """卸载apk"""
    def uninstall(self, package):
        return self.execute("shell pm uninstall " + package)

    """进入adb shell环境"""
    def shell(self, command):
        return self.execute("shell " + command)

    """启动一个activity界面"""
    def start(self, activity):
        return self.execute("shell am start " + activity)

    """获取logcat"""
    def getLogcat(self, command):
        return self.execute("logcat " + command)

    """获取指定字段的logcat"""
    def getLogcatString(self, str):
        if os.name == 'nt': # Windows 系统
            return self.getLogcat("| findstr " + str)
        else:
            return self.getLogcat("| grep " + str)

    def clearLogcat(self):
        return self.getLogcat("-c")

    def screenShot(self):

        #   获取系统当前时间
        now = datetime.datetime.now()  # 时间数组格式

        #   转换为指定格式时间戳
        timestamp = now.strftime("%Y%m%d%H%M%S")

        return self.execute("shell screencap -p /mnt/sdcard/ScreenShot/screen_shot" + timestamp + ".png")


test = ADB()
print("正在获取字段")
test.getLogcatString("Displayed")
print("获取字段结束")
