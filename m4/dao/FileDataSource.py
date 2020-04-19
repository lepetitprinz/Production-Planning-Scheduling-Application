from m4.dao.AbstractDataSource import AbstractDataSource


class FileDataSource(AbstractDataSource):
    """
    File Data Source
    File System Connection 담당 클래스
    """

    # Static Variables
    staticVar2: object = None               # Comment

    # Static Constants
    CONSTANT_VARIABLE2: object = None       # Comment

    def __init__(self):
        """
        생성자 : FileDataSource 클래스 멤버 변수들
        """

        # 1. Data Source 클래스의 모든 멤버 변수들을 상속
        super().__init__()

        # 2-1. Public
        self.connectionConfig: dict = self._get_connection_config()     # 접속 관련 설정 값들을 보관하기 위한 Dictionary

        # 2-2. Private
        self._privateVar: object = None     # Comment

    def get_io_buffer_data(self):
        """
        File IO Buffer 로부터 Contents Array 를 가져오는 처리.
        :return: Array-like Object  ex: pandas.DataFrame / list<list> / ...
        """
        pass

    def write_io_buffer_data(self, out_file: str = ""):
        """
        Write Out the Data to File on Local Disk
        :param out_file: Output File Path
        :return: void
        """
        pass

    def _get_connection_config(self):
        """
        m4.properties 파일로부터 FileSystem 접속 관련 설정 값들 받아오는 처리
        Question 생성자에서 한 번만 호출되도록 ??
        :return: dict ?
        """
        return super()._get_connection_config()

    def _get_connection(self):
        """
        File Connection 체결 처리   : _io.open()
        :return: _io._IOBase
        """
        pass

    def _release_connection(self, connection: object):
        """
        File Connection Close 처리    : _io._IOBase.close()
        :param connection: _io._IOBase
        :return:
        """
        pass
