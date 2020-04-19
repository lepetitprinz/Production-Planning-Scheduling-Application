
import logging


class Logger(object):
    """
    Logger Object
    시뮬레이터 구동 중 발생하는 이벤트들에 대한 Log 기록을 담당하는 클래스
    """

    # Static 변수들
    # Log Level 목록 : 기본 로그 레벨 설정 과정에서 참조
    # ex: WARNING 으로 설정할 경우 INFO, DEBUG 등은 출력하지 않음
    NAME_TO_LEVEL = {
        'CRITICAL': logging.CRITICAL,   #
        'FATAL':    logging.FATAL,      #
        'ERROR':    logging.ERROR,      #
        # 'WARN':     logging.WARN,     # Deprecate 될 Level 이라 제외
        'WARNING':  logging.WARNING,    #
        'INFO':     logging.INFO,       #
        'DEBUG':    logging.DEBUG,      #
        # 'NOTSET':   logging.NOTSET,   # 이 값으로 세팅해도 의미가 없으므로 제외
    }

    # Private Static Constants : Calendar 인스턴스들끼리 공유하는 static 상수들
    _CONSTANT: str = ""

    def __init__(self):
        """
        생성자 :
        """

        # 2-1. Public

        # 2-2. Private
        self._logger: logging.Logger = None     # Logger 인스턴스 할당을 위한 변수 선언

    def init(self, logger_name: str, logger_level: str, log_file_path: str):
        """
        !!!! 정리 필요 !!!
        :param logger_name:
        :param logger_level:
        :param log_file_path: logger 의 File Handler 가 로그를 기록할 .log 파일 위치
        :return:
        """

        # 세팅에 앞서 넘겨받은 파라메터 검사
        if logger_level not in Logger.NAME_TO_LEVEL.keys():
            raise KeyError(
                f"Logger 모듈의 기본 레벨 파라메터 문자열은 아래의 목록 중 하나여야 합니다."
                f"\t>>{str(Logger.NAME_TO_LEVEL)}"
            )

        # Logger 인스턴스를 생성자에서 선언해 둔 변수에 할당
        self._logger = logging.getLogger(name=logger_name)

        # Logger 의 각 Handler 인스턴스들에게 세팅해 줄 Formatter 인스턴스를 생성
        formatter: logging.Formatter = logging.Formatter()

        # Stream Handler 등록 : DB,소켓,큐 등에 로그 찍기 위한 Handler 인스턴스
        stream_handler: logging.StreamHandler = logging.StreamHandler()
        stream_handler.setLevel(level=Logger.NAME_TO_LEVEL[logger_level])
        stream_handler.setFormatter(formatter)
        self._logger.addHandler(stream_handler)

        # File Handler 등록 : .log 파일로 로그 찍기 위한 Handler 인스턴스
        file_handler: logging.FileHandler = logging.FileHandler(filename=log_file_path)

    def setup_root_logger(self):
        """

        :return:
        """
        

    def log(self):
        # Log Level 목록
        # NAME_TO_LEVEL = {
        #     'CRITICAL': logging.CRITICAL,  #
        #     'FATAL': logging.FATAL,  #
        #     'ERROR': logging.ERROR,  #
        #     'WARN': logging.WARNING,  #
        #     'WARNING': logging.WARNING,  #
        #     'INFO': logging.INFO,  #
        #     'DEBUG': logging.DEBUG,  #
        #     'NOTSET': logging.NOTSET,  #
        # }
        self._logger.critical()
        self._logger.fatal()
        self._logger.error()
        self._logger.warn()
        self._logger.warning()
        self._logger.info()
        self._logger.debug()
