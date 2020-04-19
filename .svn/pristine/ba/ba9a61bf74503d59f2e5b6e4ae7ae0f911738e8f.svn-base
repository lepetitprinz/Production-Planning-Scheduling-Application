from m4.common.SingletonInstance import SingletonInstance
from m4.manager.FactoryManager import FactoryManager
from m4.dao.AbstractDataSource import AbstractDataSource
from m4.dao.AbstractSession import AbstractSession


class SimulationMonitor(SingletonInstance):

    _factory_manager: FactoryManager = None

    _data_source: AbstractDataSource = None

    def __init__(self):
        pass

    def init(self, factory_manager: FactoryManager, data_source: AbstractDataSource):
        self._factory_manager = factory_manager
        self._data_source = data_source

    def snapshot(self):
        session: AbstractSession = self._data_source.get_session()

        session.close()
