
from base.Activities import Activities
from testcase.StartupTest import StartupTest


class TestAll(object):

    """
    遍历Activities
    """

    def test_hot(self):
        for appName,activityName in Activities.__members__.items():
            StartupTest().hotStartupTest(activityName.value)


    def test_cold(self):
        for appName, activityName in Activities.__members__.items():
            StartupTest().coldTest(activityName.value)



if __name__ == '__main__':
    TestAll().test_hot()












