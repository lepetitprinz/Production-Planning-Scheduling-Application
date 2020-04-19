
import os
import unittest

from m4.ApplicationConfiguration import ApplicationConfiguration


class ConfigTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.conf: ApplicationConfiguration = ApplicationConfiguration()

    def test_init(self):
        self.conf.init(properties_file='m4.properties')

    def test_mycase(self):
        db_source: dict = self.conf.find_section("DatabaseSource")      # m4.properties 파일 경로는 찾았으나, Section 을 찾지 못하고 있음
        for item in db_source.items():
            print(f"{item[0]} >> {item[1]}")


if __name__ == '__main__':
    testCase: ConfigTestCase = ConfigTestCase()
    testCase.setUp()
    testCase.test_init()
    testCase.test_mycase()
