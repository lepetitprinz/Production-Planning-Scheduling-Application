from m4.common.SingletonInstance import SingletonInstance
from m4.dao.AbstractDAO import AbstractDAO
from m4.dao.AbstractSession import AbstractSession


class ProcessDAO(AbstractDAO, SingletonInstance):
    """
    Process Data Access Object
    """

    def select(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 리스트 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        pass

    def select_one(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 1개 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        return session.select("select * from CM_PLANT", params)

    def select_route_process(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 리스트 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        return session.select(
            """
               SELECT *
               FROM FS_PROC
               WHERE PROC_ID IN (select CURR_LOC_ID AS PROC_ID from FS_ROUTE where sim_id = :simulation_id and CURR_LOC_ID_TYP = 'PROC')
                  OR PROC_ID IN (select NEXT_LOC_ID AS PROC_ID from FS_ROUTE where sim_id = :simulation_id and NEXT_LOC_ID_TYP = 'PROC')
            """,
            params)

    def select_route_bor(self, session: AbstractSession, **params):
        """
        세션 인스턴스를 통해 Data Source로부터 리스트 데이터를 조회
        :param session: AbstractSession 인스턴스
        :param params: sql 파라미터 데이터
        :return: {"columns" : columns, "data" : list}
        """
        return session.select(
            """
               SELECT *
               FROM FS_BOR
               WHERE PROC_ID IN (select CURR_LOC_ID AS PROC_ID from FS_ROUTE where sim_id = :simulation_id and CURR_LOC_ID_TYP = 'PROC')
                  OR PROC_ID IN (select NEXT_LOC_ID AS PROC_ID from FS_ROUTE where sim_id = :simulation_id and NEXT_LOC_ID_TYP = 'PROC')
            """,
            params)

    def execute(self, session: AbstractSession, data_list: list):
        """
        세션 인스턴스를 통해 Data Source에 대한 CUD를 실행
        :param session: AbstractSession 인스턴스
        :param sql_template: sql template string
        :param data_list: CUD 대상 데이터
        :return: True/False
        """
        pass
