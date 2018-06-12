
from base.Activities import Activities
from testcase.StartupTest import StartupTest
from testcase.Data_write_2_excel import Data
import time


"""
冷热启动测试类
"""


class TestAll(object):

    def test_hot(self):
        """
        遍历Activities的方式来启动测试
        :return:
        """
        StartupTest().delete_log_file()
        for appName, activityName in Activities.__members__.items():
            StartupTest().hot_test(activityName.value)

    def test_cold(self):
        """
        同上
        :return:
        """
        StartupTest().delete_log_file()
        for appName, activityName in Activities.__members__.items():
            StartupTest().cold_test(activityName.value)


if __name__ == '__main__':
    print("Now startup cold test...")
    TestAll().test_cold()
    print("Now startup hot test...")
    time.sleep(5.0)
    TestAll().test_hot()
    print("Now generate test report")
    time.sleep(5.0)
    Data().write_data_2_excel()
    print("All Test ending...")











