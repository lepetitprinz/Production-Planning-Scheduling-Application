
import cx_Oracle

from ..dao.AbstractDataSource import AbstractDataSource
from ..dao.AbstractSession import AbstractSession
from ..dao.DataSourceError import DataSourceError


class OracleSqlSession(AbstractSession):
    """
    Oracle Sql Session 클래스
    """
    # 세션을 생성한 Data Source
    _data_source: AbstractDataSource = None

    # Oracle Session Pool
    _connection: cx_Oracle.Connection = None

    def __init__(self):
        """
        생성자 : SqlSession
        """

    # Public 메서드
    def init(self, data_source: AbstractDataSource, connection: cx_Oracle.Connection):
        """
        Data Source와 Connection 객체를 초기화
        """
        self._data_source = data_source
        self._connection = connection

    def get_connection(self):
        """
        Data Source Connection 객체를 반환
        """
        return self._connection

    def commit(self):
        """
        commit
        """
        self._connection.commit()

    def rollback(self):
        """
        rollback
        """
        self._connection.rollback()

    def close(self):
        """
        생성된 세션을 반환, Data Source 접속을 해제하는 처리
        :return: void
        """
        self._data_source.release_session(self)

    def select(self, sql: str, params: dict):
        """
        Data Source로부터 Query문 결과 Array를 가져오는 처리
        :param sql: sql string
        :param params: sql 파라미터
        :return: {"columns" : columns, "data" : list}
        """
        if self._connection is None:
            raise DataSourceError('Data Source session is not initialized')

        try:
            cursor = self._connection.cursor()
            cursor.execute(sql, params or {})
            columns = [d[0] for d in cursor.description]
            result = cursor.fetchall()

            return {"columns": columns, "data": result}
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            error_code = error.code
            raise DataSourceError("Oracle database select Error", e, error_code)

    def execute(self, sql_template: str, data_list: list):
        """
        CRUD 쿼리문을 실행하는 처리
        :param sql_template: sql template
        :param data_list:  CUD 대상 데이터
        :return: True/False : 성공 여부
        """
        if self._connection is None:
            raise DataSourceError('Data Source session is not initialized')

        try:
            cursor = self._connection.cursor()
            cursor.executemany(sql_template, data_list)
            return True
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            error_code = error.code
            raise DataSourceError("Oracle database execute Error", error_code)

    def execute_procedure(self, procedure_name: str, params):
        """
        DB 에 저장된 프로시져를 호출하는 처리
        :param procedure_name: procedure name
        :param params: procedure 파라미터
        :return: True/False : 성공 여부
       """
