from abc import *


class AbstractSession(metaclass=ABCMeta):

    @abstractmethod
    def get_connection(self):
        """
        Data Source Connection 객체를 반환
        """
    @abstractmethod
    def commit(self):
        """
        commit
        """

    @abstractmethod
    def rollback(self):
        """
        rollback
        """

    @abstractmethod
    def close(self):
        """
        생성된 세션을 반환, Data Source 접속을 해제하는 처리
        :return: void
        """

    @abstractmethod
    def select(self, sql: str, params: tuple = ()):
        """
        Data Source로부터 Query문 결과 Array를 가져오는 처리
        :param sql: sql string
        :param params: sql 파라미터
        :return: {"columns" : columns, "data" : list}
        """

    @abstractmethod
    def execute(self, sql_template: str, data_list: list):
        """
        CRUD 쿼리문을 실행하는 처리
        :param sql_template: sql template
        :param data_list:  CUD 대상 데이터
        :return: True/False : 성공 여부
        """

    @abstractmethod
    def execute_procedure(self, procedure_name: str, params: tuple = ()):
        """
        DB 에 저장된 프로시져를 호출하는 처리
        :param procedure_name: procedure name
        :param params: procedure 파라미터
        :return: True/False : 성공 여부
       """
