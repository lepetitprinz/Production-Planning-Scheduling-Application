
import os
import cx_Oracle

from m4.common.SingletonInstance import SingletonInstance
from m4.dao.AbstractDataSource import AbstractDataSource
from m4.dao.OracleSqlSession import OracleSqlSession
from m4.ApplicationConfiguration import ApplicationConfiguration


class OracleDataSource(AbstractDataSource, SingletonInstance):
    """
    Oracle Data Source 클래스
    """

    # Oracle Session Pool
    _pool: cx_Oracle.SessionPool = None

    def __init__(self):
        """
        생성자 : DbDataSource 클래스 멤버 변수들
        """
        # Oracle Database 언어 설정
        os.environ["NLS_LANG"] = ".AL32UTF8"
        super(__class__, self).__init__()

    # Public 메서드
    def init(self, config: ApplicationConfiguration):
        """
        Database SessionPool 초기화
        :param: config - Application Configuration
        """
        uri_map = dict(config.find_section("DatabaseSource"))
        tns: str = cx_Oracle.makedsn(
            host=uri_map["ds.connection.host"],
            port=uri_map["ds.connection.port"],
            sid=uri_map["ds.connection.sid"]
        )

        # Oracle Session Pool 생성
        self._pool: cx_Oracle.SessionPool = cx_Oracle.SessionPool(
            user=uri_map["ds.connection.id"],
            password=uri_map["ds.connection.password"],
            dsn=tns,
            min=1, max=20, increment=1, threaded=True
        )

    def get_session(self):
        """
        Data Source로부터 가용 세션을 획득하고 Data IO를 위한 세션 인스턴스를 반환
            (Database)DataSource    - SessionPool, Connection 등
            FileDataSource  - File IO 를 위한 객체 inherits _io.IOBase
        :return: AbstractSession 인스턴스
        """
        if self._pool is None:
            return None

        session: OracleSqlSession = OracleSqlSession()
        session.init(self, self._pool.acquire())
        return session

    def release_session(self, session: OracleSqlSession):
        """
        생성된 세션을 반환, 반환 세션은 데이터 소스에 따라 다름
            (Database)DataSource    - cx_Oracle.SessionPool.release( cx_Oracle.Connection )
            FileDataSource  - _io._IOBase.close()
        :param session: AbstractSession 인스턴스
        :return: void
        """
        if session is None:
            return
        connection = session.get_connection()
        self._pool.release(connection)

    def close(self):
        """
        DataSource 비 사용 상태로 전환
        :return: void
        """
        self._pool.close()
