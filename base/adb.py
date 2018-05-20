# encoding=utf-8
import os
import string
import subprocess
import datetime


class ADB(object):


    """
    开启一个cmd窗口并且执行command_text命令，将stdout输出到指定文件中
    """
    def cmd(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        write_text = open(r"/Users/hongzhi/Test/cmd.txt", "w")
        results = subprocess.Popen(command_text, shell=True, stdout=write_text,).stdout
        write_text.close()
        while 1:
            line = results
            if not line: break
            command_result += line
        return command_result


    def devices(self):
        result = self.cmd("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        return [device for device in devices if len(device) > 2]


    """push 文件到手机"""
    def push(self, from_computor, to_phone):
        return self.cmd("push " + from_computor + " " + to_phone)


    """pull 手机文件"""
    def pull(self, from_phone, to_computor):
        return self.cmd("pull " + from_phone + " " + to_computor)


    """覆盖安装apk"""
    def install(self, apk_file):
        return self.cmd("install -r " + apk_file)

    def uninstall(self, package):
        return self.cmd("shell pm uninstall " + package)

    def shell(self, command):
        return self.cmd("shell " + command)

    def start(self, activity):
        return self.cmd("shell am start " + activity)

    def screenShot(self):

        #   获取系统当前时间
        now = datetime.datetime.now()  # 时间数组格式

        #   转换为指定格式时间戳
        timestamp = now.strftime("%Y%m%d%H%M%S")

        self.cmd("shell screencap -p /mnt/sdcard/ScreenShot/screen_shot" + timestamp + ".png")


test = ADB()
test.screenShot()
