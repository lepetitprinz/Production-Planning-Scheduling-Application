
from abc import *
from m4.dao.AbstractSession import AbstractSession


class AbstractDao(metaclass=ABCMeta):
    """
    Data Access Object 추상 클래스
    """

    @abstractmethod
    def select_one(self, session: AbstractSession, params: tuple = ()):
        """
        세션 인스턴스를 통해 Data Source로부터 1개 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """

    @abstractmethod
    def select_list(self, session: AbstractSession, params: tuple = ()):
        """
        세션 인스턴스를 통해 Data Source로부터 리스트 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """

    @abstractmethod
    def execute(self, session: AbstractSession, sql_template: str, data_list: list):
        """
        세션 인스턴스를 통해 Data Source에 대한 CUD를 실행
        :param session: AbstractSession 인스턴스
        :param sql_template: sql template string
        :param data_list: CUD 대상 데이터
        :return: True/False
        """


