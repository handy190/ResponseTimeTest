
from base.adb import ADB
import time

class ColdStartupTest(object):

    def coldTest(self):

        adb = ADB()

        # 开始测试前先kill掉，防止后台运行
        # adb.start("-S com.android.contacts/.activities.PeopleActivity")
        adb.force_stop("com.android.contacts") # split('/')[0]
        time.sleep(3.0)

        for t in range(10):
            print("第 " + str(t + 1) + " 次测试beginning...")
            # 启动一个activity
            adb.start("com.android.contacts/.activities.PeopleActivity")
            time.sleep(5.0)
            print("第 " + str(t + 1) + " 次测试正在获取字段..")
            # 获取logcat 的 displayed 字段
            adb.getLogcatString("Displayed")
            time.sleep(5.0)

            print("第 " + str(t + 1) + " 次测试获取字段结束..")
            # 强制停止应用
            adb.force_stop("com.android.contacts")
            time.sleep(5.0)
            #   每次获取完log就要清除一次
            adb.clearLogcat()
            print("第 " + str(t + 1) + " 次测试ending...")

if __name__ == '__main__':

    ColdStartupTest().coldTest()