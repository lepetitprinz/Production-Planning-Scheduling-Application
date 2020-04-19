
import os
import unittest

from m4.ApplicationConfiguration import ApplicationConfiguration


class ConfigTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.conf: ApplicationConfiguration = ApplicationConfiguration.instance()

    def test_init(self):
        self.conf.init(properties_file='m4.properties')

    def test_section_dict(self):
        db_source: dict = dict(self.conf.find_section("DatabaseSource"))
        for item in db_source.items():
            print(f"{item[0]} >> {item[1]}")


if __name__ == '__main__':
    testCase: ConfigTestCase = ConfigTestCase()
    testCase.setUp()
    testCase.test_init()
    testCase.test_section_dict()
