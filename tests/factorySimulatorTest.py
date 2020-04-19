
import unittest

from m4.ApplicationConfiguration import ApplicationConfiguration
from m4.FactorySimulator import FactorySimulator
from m4.dao.OracleDataSource import OracleDataSource


class FactorySimulatorTestCase(unittest.TestCase):

    def setUp(self) -> None:

        # 테스트용 FactorySimulator 인스턴스 생성
        self.simulator: FactorySimulator = FactorySimulator.instance()

        print("Test Environment has been SetUp !")

    def test_init(self):

        config: ApplicationConfiguration = ApplicationConfiguration.instance()
        config.init('m4.properties')

        data_source: OracleDataSource = OracleDataSource.instance()
        data_source.init(config)

        self.simulator.init(config, data_source)

        print("Initialized !")

    def test_run(self):

        self.simulator.run()


if __name__ == '__main__':
    tester: FactorySimulatorTestCase = FactorySimulatorTestCase()
    tester.setUp()
    tester.test_init()
    tester.test_run()
