import os
import configparser
from m4.common.SingletonInstance import SingletonInstance


class ApplicationConfiguration(SingletonInstance):
    """
    어플리케이션 설정 정보
        1. 어플리케이션 설치 정보 : file(m4.properties)
        2. 데이터베이스 실행 설정 정보
        3. 데이터베이스 코드 정보
    """
    # properties file path : working directory path
    PROPERTIES_FILE_PATH: str = \
        os.path.dirname(
                os.path.dirname(__file__)
        )

    # 어플리케이션 설치 정보, 어플리케이션 initialize 시 db로부터 추가 설정를 add
    _config: configparser.ConfigParser = None

    def __init__(self):
        self._config = configparser.ConfigParser()

    def init(self, properties_file):
        """
        ApplicationConfiguration 초기화
        :param properties_file : 어플리케이션 설치 정보 파일명
        """
        self._config.read(os.path.join(self.PROPERTIES_FILE_PATH, properties_file))

    def find(self, section, name):
        """
        섹션명, 설정명으로 설정 검색
        :param section: 섹션명(그룹)
        :param name: 설정명(코드명)
        :return: 설정값(코드값)
        """
        return self._config[section][name]

    def find_section(self, section):
        """
         섹션명으로 설정 검색
         :param section : 섹션명(그룹)
         :return: 섹션 내의 설정명(코드명), 설정값(코드값) 리스트
        """
        return self._config.items(section)

    def add(self, section, items):
        """
         설정(코드) 정보 추가
         :param section : 섹션명(그룹)
         :param items : 섹션 내의 설정명(코드명), 설정값(코드값) 리스트
        """
        # parser.add_section('bug_tracker')
        # parser.set('bug_tracker', 'url', 'http://localhost:8080/bugs')
        # parser.set('bug_tracker', 'username', 'dhellmann')
        # parser.set('bug_tracker', 'password', 'secret')
        pass
