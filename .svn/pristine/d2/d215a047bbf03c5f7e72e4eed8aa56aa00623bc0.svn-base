import logging
import logging.config
import json

from m4.common.SingletonInstance import SingletonInstance
from m4.ApplicationConfiguration import ApplicationConfiguration


class LogHandler(SingletonInstance):
    """
    logging.Logger를 관리하는 Handler 클래스
    """

    # logging.Logger 인스턴스
    _logger: logging.Logger = None  # Logger 인스턴스 할당을 위한 변수 선언

    def __init__(self):
        pass

    def init(self, config: ApplicationConfiguration):
        """
            Logger Configuration, Logger 설정파일인 ./resources/m4_log.json 파일을 읽어들여서 설정함
        :param config: Application Configuration
        :return: void
        """

        with open(config.find("Server", "log.file"), "rt") as f:
            config = json.load(f)

        logging.config.dictConfig(config)
        self._logger = logging.getLogger()

    def get_logger(self):
        return self._logger
