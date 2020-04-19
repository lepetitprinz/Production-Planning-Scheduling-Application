from m4.common.SingletonInstance import SingletonInstance
from m4.dao.AbstractDAO import AbstractDAO
from m4.dao.AbstractSession import AbstractSession


class ResourceCalendarDAO(AbstractDAO, SingletonInstance):
    """
    Resource Calendar Data Access Object
    """

    def select(self, session: AbstractSession, **params):
        pass

    def select_one(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 1개 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        return session.select("select * from FS_FACTORY", params)

    def select_list(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 리스트 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        return session.select(
            """
                SELECT MST.FACTRY_SCHDL_ID   AS CAL_ID
                     , MST.FACTRY_SCHDL_NM   AS CAL_NAME
                     , J01.TM_CONST_ID      AS DUR_ID
                     , J01.PRIORITY         AS DUR_PRIORITY
                     , J01.START_DT_HMS     AS DUR_APPLY_START_DATE
                     , J01.END_DT_HMS       AS DUR_APPLY_END_DATE
                     , J02.TM_CONST_TYP     AS DUR_TYPE
                     , J02.PRD_TYP          AS DUR_CYCLE_TYPE
                     , J02.START_DT_HMS     AS DUR_START_DATE
                     , J02.END_DT_HMS       AS DUR_END_DATE
                FROM FS_FACTRY_SCHDL MST
                LEFT OUTER JOIN FS_FACTRY_SCHDL_CONST J01
                ON MST.FACTRY_SCHDL_ID = J01.FACTRY_SCHDL_ID
                LEFT OUTER JOIN FS_TM_CONST J02
                ON J01.TM_CONST_ID = J02.TM_CONST_ID
                ORDER BY J01.PRIORITY
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
