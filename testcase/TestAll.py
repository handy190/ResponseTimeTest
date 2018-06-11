
from base.Activities import Activities
from testcase.StartupTest import StartupTest
from testcase.Data_write_2_excel import Data
import time

class TestAll(object):

    """
    遍历Activities
    """
    def test_hot(self):
        StartupTest().delete_log_file()
        for appName, activityName in Activities.__members__.items():
            StartupTest().hot_test(activityName.value)

    def test_cold(self):
        StartupTest().delete_log_file()
        for appName, activityName in Activities.__members__.items():
            StartupTest().cold_test(activityName.value)


if __name__ == '__main__':
    print("Now startup cold test...")
    TestAll().test_cold()
    print("Now startup hot test...")
    TestAll().test_hot()
    print("Now generate test report")
    Data().write_data_2_excel()
    print("All Test ending...")











