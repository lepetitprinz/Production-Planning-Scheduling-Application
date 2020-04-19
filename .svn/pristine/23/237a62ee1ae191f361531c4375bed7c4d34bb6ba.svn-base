from m4.ApplicationConfiguration import ApplicationConfiguration
from m4.util.LogHandler import LogHandler
from m4.dao import DataSourceError
from m4.dao.OracleDataSource import OracleDataSource
from m4.FactorySimulator import FactorySimulator

"""
최상위 어플리케이션 실행 파일
    FactorySimulator 클래스 인스턴스를 생성
    Simulator를 실행
"""

if __name__ == '__main__':

    config: ApplicationConfiguration = ApplicationConfiguration.instance()
    config.init('m4.properties')

    logHandler: LogHandler = LogHandler.instance()
    logHandler.init(config)

    logger = logHandler.get_logger()

    simulator: FactorySimulator = FactorySimulator.instance()

    try:
        data_source: OracleDataSource = OracleDataSource.instance()
        data_source.init(config)

        simulator.init(config, data_source)

    except DataSourceError as e:
        logger.error(e)
    finally:
        pass

    # Simulation 시작
    simulator.run()
