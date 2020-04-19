
import datetime


class TimeUtility:
    """
    Time Utility
    시간 관련 처리를 위한 유틸리티성 static 메서드들을 정의
    """

    # CONSTANTS
    _DATE_STR_FORMAT: str = ""  # DATE 정보가 문자열로 주어질 경우, datetime 변환을 위한 format 정보
    _TIME_UNIT_TYPES: list = [  # timestep 길이 설정 시 허용 가능 단위 문자열 목록 : milisec, microsec 허용 안됨
        'weeks',                # 주 단위
        'days',                 # 일 단위
        'hours',                # 시간 단위
        'minutes',              # 분 단위
        'seconds'               # 초 단위
    ]

    @staticmethod
    def check_from_to(start_date: datetime.datetime, end_date: datetime.datetime, equal_flag: bool = False):
        """
        시작 시간이 종료 시간 이전인지 검사
        :param start_date: datetime.datetime = 시작 시간
        :param end_date: datetime.datetime = 종료 시간
        :param equal_flag: bool = 부등호에 등호 포함할 지 여부
        :return: bool = 시작 < 종료 여부
        """
        check: bool = start_date < end_date or (equal_flag and start_date == end_date)
        return check

    @staticmethod
    def derive_timedelta(time_length: int, uom: str):
        """
        uom 단위의 time_length 길이 정보를 timedelta 객체로 반환
        :param time_length: 시간 길이 정수 값
        :param uom: str = 시간 길이 단위 문자열 TimeUtility._TIME_UNIT_TYPES 참조
        :return: datetime.timedelta
        """
        kwargs = {uom: time_length}
        rslt_timedelta: datetime.timedelta = datetime.timedelta(**kwargs)

        return rslt_timedelta

    @staticmethod
    def check_timestep_uom(uom: str):
        """
        timestep 설정 시 지정된 uom(Unit of Measure) 문자열 값이 허용 값인지 판단
        :param uom: str (timestep 설정 단위 문자열: weeks, days, hours, minutes, seconds)
        :return: bool (True=허용 단위, False=비허용 단위)
        """
        is_available_uom: bool = uom in TimeUtility._TIME_UNIT_TYPES
        return is_available_uom

    @staticmethod
    def check_date_info(date_info: object):
        """
        넘겨 받은 시작 일자 정보의 값 형식 점검 및 datetime 변환 작업 결과를 반환합니다.
        :param date_info: 시작일자 정보 값, 일반적인 object 를 가정, datetime 인지 str 인지를 검사,
                          이 외의 처리 불가 형식의 경우 Assertion 에러 표출
        :return: datetime.datetime
        """

        if isinstance(date_info, datetime.datetime):
            # start_date 가 datetime.datetime 객체일 경우: 별도 처리 없이 통과
            pass
        elif isinstance(date_info, str):
            # start_date 가 str 객체일 경우: datetime.datetime 객체로 변환
            date_info: datetime.datetime = TimeUtility.convert_str_to_date(date_string=date_info)
        else:
            # start_date 가 datetime 혹은 str 둘 중 어느 것에도 해당되지 않을 경우
            raise AssertionError(
                f"date_info 파라메터 에 {type(date_info)} 타입 값이 할당되었습니다."
            )
        return date_info

    @staticmethod
    def convert_str_to_date(date_string: str):
        """
        문자열 형식으로 주어진 날짜 정보를 datetime.datetime 객체로 변환하여 반환합니다.
        :param date_string: str: 날짜 정보 문자열
        :return: datetime.datetime
        """
        date_obj: datetime.datetime = datetime.datetime.strptime(date_string, TimeUtility._DATE_STR_FORMAT)
        return date_obj

    @staticmethod
    def set_date_str_format(format_string: str):
        """
        TimeUtility 클래스의 private static 상수 _DATE_STR_FORMAT 값을 설정
        :param format_string: str (날짜 문자열 형식    ex: %Y-%m-%D %H:%M:%S)
        :return:
        """
        TimeUtility._DATE_STR_FORMAT = format_string
