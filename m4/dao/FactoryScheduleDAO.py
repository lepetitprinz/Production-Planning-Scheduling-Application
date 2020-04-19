from m4.common.SingletonInstance import SingletonInstance
from m4.dao.AbstractDAO import AbstractDAO
from m4.dao.AbstractSession import AbstractSession


class FactoryScheduleDAO(AbstractDAO, SingletonInstance):
    """
    Factory Calendar Data Access Object
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
        return session.select("select * from FS_FACTRY_SCHDL", params)

    def select_constraint(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 리스트 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        return session.select(
            """
            SELECT TO_DATE(T1.START_DT_HMS, 'YYYYMMDDHH24MISS') START_DATE, 
                   TO_DATE(T1.END_DT_HMS, 'YYYYMMDDHH24MISS') END_DATE,
                   T1.FACTRY_SCHDL_ID AS SCHDL_ID, T1.PRIORITY,
                   T2.TM_CONST_ID, T2.TM_CONST_NM,T2.TM_CONST_TYP, T2.PRD_TYP,
                   TO_DATE(T2.START_DT_HMS, 'YYYYMMDDHH24MISS') LOWER_BOUND, 
                   TO_DATE(T2.END_DT_HMS, 'YYYYMMDDHH24MISS') UPPER_BOUND
              FROM FS_FACTRY_SCHDL_CONST T1
                   JOIN FS_TM_CONST T2
                   ON (T1.TM_CONST_ID = T2.TM_CONST_ID)
             WHERE T1.FACTRY_SCHDL_ID IN (SELECT FACTRY_SCHDL_ID FROM FS_FACTRY_SCHDL WHERE FACTRY_SCHDL_ID = :factory_schedule_id)
            """, params)

    def select_max_priority(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 리스트 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        return session.select(
            """
            SELECT MAX(T1.PRIORITY) AS MAX_PRIORITY
              FROM FS_FACTRY_SCHDL_CONST T1
                   JOIN FS_TM_CONST T2
                   ON (T1.TM_CONST_ID = T2.TM_CONST_ID)
             WHERE T1.FACTRY_SCHDL_ID IN (SELECT FACTRY_SCHDL_ID FROM FS_FACTRY_SCHDL WHERE FACTRY_SCHDL_ID = :factory_schedule_id)
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
