
from abc import *

from ..dao.AbstractSession import AbstractSession


class AbstractDAO(metaclass=ABCMeta):
    """
    Data Access Object 추상 클래스
    """

    @classmethod
    def map(cls, inp: dict) -> list:
        """
         Data Source의 조회 결과를 dict 형식으로 변환(필요 시)
         {"columns" : columns, "data" : list} =>
         [{"column_name" : value, "column_name" : value, ...}, {"column_name" : value, "column_name" : value, ...}, {"column_name" : value, "column_name" : value, ...}, ...]
         :rtype: list
         :param inp : 조회 결과({"columns" : columns, "data" : list})
         :return dict array
        """
        arr = []
        for data in inp["data"]:
            arr.append(dict(zip(inp["columns"], data)))
        return arr

    @classmethod
    def hash_map(cls, inp: dict, key_column: str) -> dict:
        """
         Data Source의 조회 결과를 dict 형식으로 변환(필요 시)
         {"columns" : columns, "data" : list} =>
         {"value1": [{"column_name" : value1, "column_name" : value, ...}],
          "value2": [{"column_name" : value2, "column_name" : value, ...}],
          "value3": [{"column_name" : value3, "column_name" : value, ...}], ...}
         :rtype: dict
         :param inp : 조회 결과({"columns" : columns, "data" : list})
         :param key_column : hash key column
         :return dict
        """
        arr: list = cls.map(inp)
        res: dict = {}
        for row in arr:
            values: list = res.get(row[key_column])
            if values is None:
                values = []
                res[row[key_column]] = values
            values.append(row)
        return res

    @abstractmethod
    def select_one(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 1개 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터 Keyword Arguments
        :return: {"columns" : columns, "data" : list}
        """

    @abstractmethod
    def select(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 리스트 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터 Keyword Arguments
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
