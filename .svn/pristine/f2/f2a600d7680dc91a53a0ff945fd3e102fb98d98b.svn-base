from m4.ApplicationConfiguration import ApplicationConfiguration
from m4.dao import DataSourceError
from m4.dao.OracleDataSource import OracleDataSource
from m4.FactorySimulator import FactorySimulator

"""
최상위 어플리케이션 실행 파일
    FactorySimulator 클래스 인스턴스를 생성
    Simulator를 실행
"""

if __name__ == '__main__':

    try:
        config: ApplicationConfiguration = ApplicationConfiguration.instance()
        config.init('m4.properties')

        data_source: OracleDataSource = OracleDataSource.instance()
        data_source.init(config)

        simulator: FactorySimulator = FactorySimulator.instance()
        simulator.init(config, data_source)

        simulator.run()

    except DataSourceError as e:
        print(e)
    finally:
        pass
