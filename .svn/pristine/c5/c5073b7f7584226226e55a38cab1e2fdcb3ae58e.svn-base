from m4.entity.Factory import Factory
from m4.dao.AbstractSession import AbstractSession
from m4.dao.FactoryDao import FactoryDao
from m4.dao.BOMDao import BOMDao


class FactoryBuilder(object):

    @classmethod
    def build(cls, session: AbstractSession):

        instance: Factory = None

        factory, bom = FactoryBuilder.get_dao_data(session)

        return instance

    @classmethod
    def get_dao_data(cls, session: AbstractSession):

        factory = FactoryDao.instance().select_one(session)
        bom = BOMDao.instance().select_list(session)

        return factory, bom
