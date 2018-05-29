from unittest import TestSuite

import pytest
import unittest
from base.Activities import Activities
from testcase.HotStartupTest import HotStartupTest


class TestSuite:

    def testHot(self):
        if 'a' in 'halo':
            HotStartupTest().hotStartupTest(Activities.DIALER.value)






