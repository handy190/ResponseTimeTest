import pytest
import unittest
from base.Activities import Activities
from testcase.HotStartupTest import HotStartupTest


class TestSuite:


    def testHot(self):
        HotStartupTest().hotStartupTest(Activities.DIALER.value)






