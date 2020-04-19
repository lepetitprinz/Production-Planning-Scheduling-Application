import os
import configparser
from m4.common.SingletonInstance import SingletonInstance
from m4.dao.AbstractDataSource import AbstractDataSource
from m4.dao.AbstractSession import AbstractSession
from m4.dao.CommonCodeDAO import CommonCodeDAO


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
    _config: configparser.RawConfigParser = None

    def __init__(self):
        self._config = configparser.RawConfigParser()
        self._config.optionxform = str

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

    def _add(self, section, items):
        """
         설정(코드) 정보 추가
         :param section : 섹션명(그룹)
         :param items : 섹션 내의 설정명(코드명), 설정값(코드값) 리스트
        """
        self._config.add_section(section)
        for item in items:
            self._config.set(section, item[0], item[1])

    def init_code(self, data_source: AbstractDataSource):
        """
         공통 코드 정보 설정
         self._config 객체에 section, item 생성
         :param data_source : Data Source
        """
        session: AbstractSession = data_source.get_session()

        dao: CommonCodeDAO = CommonCodeDAO.instance()
        group_codes = dao.map(dao.select_group_code(session, use_yn="Y"))
        codes = dao.map(dao.select(session, use_yn="Y"))

        for group_code in group_codes:
            section = group_code["COMN_GRP_CD"]
            items = []
            for code in codes:
                if section == code["COMN_GRP_CD"]:
                    items.append((code["COMN_CD"], code["COMN_CD_NM"]))
            self._add(section, items)

        session.close()
