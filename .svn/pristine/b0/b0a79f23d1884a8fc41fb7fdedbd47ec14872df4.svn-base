from m4.common.SingletonInstance import SingletonInstance
from m4.dao.AbstractDAO import AbstractDAO
from m4.dao.AbstractSession import AbstractSession


class CalendarDAO(AbstractDAO, SingletonInstance):
    """
    Factory Calendar Data Access Object
    """

    def select(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 리스트 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터 Keyword Arguments
        :return: {"columns" : columns, "data" : list}
        """
        return session.select("select * from CM_CALNDR", params)

    def select_one(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 1개 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        return session.select("select * from CM_CALNDR", params)

    def select_calendar_constraint(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 달력 휴일 constraint 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        return session.select(
            """
                SELECT
                    to_date(:start_date, 'YYYYMMDDHH24MISS') START_DATE,
                    to_date(:end_date, 'YYYYMMDDHH24MISS') END_DATE,
                    0 AS PRIORITY,
                    DECODE(HLDAY_YN,'Y',CAL.DESCR,'주말') TM_CONST_NM,
                    'NOML' TM_CONST_TYP,
                    'DAY' PRD_TYP,
                    to_date(yyyymmdd, 'yyyymmdd') LOWER_BOUND,
                    to_date(yyyymmdd, 'yyyymmdd')+1 UPPER_BOUND                    
                FROM CM_CALNDR cal
                WHERE 1 = 1
                AND YYYYMMDD >= substr(:start_date, 1, 8)
                AND YYYYMMDD <= substr(:end_date, 1, 8)
                AND OFF_DAY_YN  = :off_day_yn
                ORDER BY YYYYMMDD
            """, params)

    def execute(self, session: AbstractSession, sql_template: str, data_list: list):
        """
        세션 인스턴스를 통해 Data Source에 대한 CUD를 실행
        :param session: AbstractSession 인스턴스
        :param sql_template: sql template string
        :param data_list: CUD 대상 데이터
        :return: True/False
        """
        pass
