
from base.Activities import Activities
from testcase.StartupTest import StartupTest


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
    TestAll().test_cold()












