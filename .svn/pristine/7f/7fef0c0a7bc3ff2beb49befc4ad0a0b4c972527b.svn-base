
import datetime


class ConvertUtility:
    """
    Convert Utility
    데이터 객체 간 타입 변환을 위한 유틸리티성 메서드들을 정의
        - AbstractDao.select_one() 의 결과로 반환되는
            {'columns': [str], 'data': [tuple]}  ==>  [{col1: val1, col2: val2, ...}]
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
    def dao_dict_to_list_with_dict(dao_dict: dict):
        """
        AbstractDao.select_one() 의 결과로 반환되는 dict 를 list<dict> 형식 변환하여 반환
            {'columns': [str], 'data': [tuple]}  ==>  [{col1: val1, col2: val2, ...}]
        :param dao_dict: dict = AbstractDao.select_one() 의 결과로 반환되는 dict
        :return: list<dict> = [{col1: val1, col2: val2, ...}]
        """

        # 칼럼명 대 칼럼 인덱스 번호 dict
        column_to_index: dict = {
            column_name: dao_dict['columns'].index(column_name)
            for column_name in dao_dict['columns']
        }

        # 변환 작업
        result = [
            {
                column: data_row[column_to_index[column]]
                for column in column_to_index.keys()
            }
            for data_row in dao_dict['data']
        ]

        return result
