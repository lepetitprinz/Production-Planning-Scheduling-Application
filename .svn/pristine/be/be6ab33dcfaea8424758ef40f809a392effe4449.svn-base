
import numpy as np
import datetime

from m4.ApplicationConfiguration import ApplicationConfiguration


class DateTimeUtility:
    """
    Time Utility
    시간 관련 처리를 위한 유틸리티성 static 메서드들을 정의
    """
    _TIME_UNIT_TYPES: dict = {                  # timestep 길이 설정 시 허용 가능 단위 문자열 목록 : milisec, microsec 허용 안됨
        'MON': 'months',
        'WEEK': 'weeks',
        'DAY': 'days',
        'HOUR': 'hours',
        'MI': 'minutes',
        'SEC': 'seconds'
    }

    @classmethod
    def create_timedelta(cls, time_uom: str, time_step: int):
        """
        uom 단위의 time_step 정보를 timedelta 객체로 반환
        :param time_uom: str = 시간 길이 단위 문자열 DateTimeUtility._TIME_UNIT_TYPES 참조
        :param time_step: 시간 길이 정수 값
        :return: datetime.timedelta
        """
        kwargs = {time_uom: time_step}
        timedelta: datetime.timedelta = datetime.timedelta(**kwargs)

        return timedelta

    @classmethod
    def get_python_uom(cls, uom: str):
        """
        _TIME_UNIT_TYPES 의 Key 값으로부터 (DB 에 저장된 TimeStep 단위 정보 문자열)
        Value 값을 가져오는 메서드 (Key 에 대응되는 datetime.timedelta 의 argument 명칭)
        :return:
        """
        return DateTimeUtility._TIME_UNIT_TYPES[uom]

    @classmethod
    def convert_str_to_date(cls, date_string: str, fmt: str = "%Y%m%d%H%M%S"):
        """
        문자열 형식으로 주어진 날짜 정보를 datetime.datetime 객체로 변환하여 반환합니다.
        :param date_string: str: 날짜 정보 문자열
        :param fmt: str: datetime 변환을 위한 format 정보
        :return: datetime.datetime
        """
        date_obj: datetime.datetime = datetime.datetime.strptime(date_string, fmt)
        return date_obj
