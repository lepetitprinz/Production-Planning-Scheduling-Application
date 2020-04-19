
from abc import *


class AbstractDataSource(metaclass=ABCMeta):
    """
    Abstract Data Source Object
    데이터 소스에 대한 함수를 정의한 추상 클래스(특히 데이터베이스에 특화되어 정의됨)
    자손 클래스의 경우 데이터 소스의 종류에 따라 다르게 구현
        (Database)DataSource    : Database 와의 연결을 담당
        FileDataSource  : File System (패키지가 설치된 로컬 내 파일 시스템)과의 연결을 담당
    """

    @abstractmethod
    def get_session(self):
        """
        Data Source로부터 가용 세션을 획득하고 Data IO를 위한 세션 인스턴스를 반환
            (Database)DataSource    - SessionPool, Connection 등
            FileDataSource  - File IO 를 위한 객체 inherits _io.IOBase
        :return: AbstractSession 인스턴스
        """

    @abstractmethod
    def release_session(self, session: object):
        """
        생성된 세션을 반환, 반환 세션은 데이터 소스에 따라 다름
            (Database)DataSource    - cx_Oracle.SessionPool.release( cx_Oracle.Connection )
            FileDataSource  - _io._IOBase.close()
        :param session: AbstractSession 인스턴스
        :return: void
        """

    @abstractmethod
    def close(self):
        """
        DataSource 비 사용 상태로 전환
        :return: void
        """
