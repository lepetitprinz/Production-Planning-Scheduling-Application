from m4.common.SingletonInstance import SingletonInstance
from m4.dao.AbstractDao import AbstractDao
from m4.dao.AbstractSession import AbstractSession


class FactoryDao(AbstractDao, SingletonInstance):
    """
    Factory Data Access Object
    """

    def select_one(self, session: AbstractSession, params: tuple = ()):
        """
        세션 인스턴스를 통해 Data Source로부터 1개 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        return session.select("select * from FS_FACTORY", params)

    def select_list(self, session: AbstractSession, params: tuple = ()):
        """
        세션 인스턴스를 통해 Data Source로부터 리스트 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        pass

    def execute(self, session: AbstractSession, data_list: list):
        """
        세션 인스턴스를 통해 Data Source에 대한 CUD를 실행
        :param session: AbstractSession 인스턴스
        :param sql_template: sql template string
        :param data_list: CUD 대상 데이터
        :return: True/False
        """
        pass