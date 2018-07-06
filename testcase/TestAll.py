
from base.Activities import Activities
from testcase.StartupTest import StartupTest
from base.Data_write_2_excel import Data
import time


class TestAll(object):

    """
    冷热启动测试类
    """
    def test_hot(self):
        """
        冷启动测试
        :return:
        """
        # StartupTest().delete_log_file()   这里再删除会把cold_raw_data.txt删除掉
        for appName, activityName in Activities.__members__.items():
            StartupTest().hot_test(activityName.value)

    def test_cold(self):
        """
        热启动测试
        :return:
        """
        StartupTest().delete_log_file()
        for appName, activityName in Activities.__members__.items():
            StartupTest().cold_test(activityName.value)


if __name__ == '__main__':
    print("开始检查包名。。。。")
    StartupTest().check_phone_package()
    print("Now startup cold test...")
    TestAll().test_cold()
    print("Now startup hot test...")
    time.sleep(10.0)
    TestAll().test_hot()
    print("Now generate test report")
    time.sleep(10.0)
    Data().write_data_2_excel()
    print("All Test ending...")











