from m4.common.SingletonInstance import SingletonInstance
from m4.ApplicationConfiguration import ApplicationConfiguration
from m4.dao.AbstractDataSource import AbstractDataSource
from m4.dao.AbstractSession import AbstractSession
from m4.manager.FactoryBuilder import FactoryBuilder
from m4.manager.FactoryManager import FactoryManager
from m4.manager.SimulationMonitor import SimulationMonitor


class FactorySimulator(SingletonInstance):

    def __init__(self):
        pass

    def init(self, config: ApplicationConfiguration, data_source: AbstractDataSource):
        session: AbstractSession = data_source.get_session()

        factory_manager = FactoryManager.instance()
        factory_manager.init(FactoryBuilder.build(session))

        monitor: SimulationMonitor = SimulationMonitor.instance()
        monitor.init(factory_manager, data_source)

        session.close()

    def run(self):
        monitor: SimulationMonitor = SimulationMonitor.instance()
        monitor.snapshot()
