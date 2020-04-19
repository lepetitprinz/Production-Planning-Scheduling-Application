import math

from m4.common.SingletonInstance import SingletonInstance
from m4.ApplicationConfiguration import ApplicationConfiguration
from m4.dao.AbstractDataSource import AbstractDataSource
from m4.dao.AbstractSession import AbstractSession
from m4.dao.PlanVersionDAO import PlanVersionDAO
from m4.dao.SimulationDAO import SimulationDAO
from m4.manager.FactoryBuilder import FactoryBuilder
from m4.manager.FactoryManager import FactoryManager
from m4.manager.ScheduleManager import ScheduleManager
from m4.manager.SimulationMonitor import SimulationMonitor
from m4.backward.BackwardBuilder import BackwardBuilder
from m4.backward.BackwardManager import BackwardManager

from m4.util.LogHandler import LogHandler


class FactorySimulator(SingletonInstance):

    def __init__(self):
        # logger
        self._logger = LogHandler.instance().get_logger()
        # 생산 일정 계획 버전 정보
        self._plan_version_dict: dict = None
        # 시뮬레이션 정보
        self._simulation_dict: dict = None
        # Schedule Manager Object
        self._scheduleManager = ScheduleManager()  # Simulator 전체 runTime 범위 관리하는 ScheduleManager 객체
        # self._run_time: dict = {}                  # Simulator 의 현재 runTime 위치 (int)

        self.backward_step_plan_result: list = []
        self.backward_step_plan_by_loc: dict = {}
        self.backward_step_peg_result: dict = {}

    def init(self, plan_version_id: str, simulation_id: str, config: ApplicationConfiguration, data_source: AbstractDataSource):
        session: AbstractSession = data_source.get_session()

        plan_version_dao = PlanVersionDAO.instance()
        self._plan_version_dict = plan_version_dao.map(plan_version_dao.instance().select_one(session, plan_version_id=plan_version_id))[0]
        simulation_dao = SimulationDAO.instance()
        self._simulation_dict = simulation_dao.map(simulation_dao.instance().select_one(session, simulation_id=simulation_id))[0]

        # ScheduleManager 객체 setup
        self._scheduleManager.init(self._plan_version_dict, self._simulation_dict, session)

        # FactoryBuilder.build(self._plan_version_dict, self._simulation_dict, session)

        factory_manager: FactoryManager = FactoryManager.instance()
        factory_manager.init(FactoryBuilder.build(plan_version_dict=self._plan_version_dict,
                                                  simulation_dict=self._simulation_dict,
                                                  session=session))

        #
        monitor: SimulationMonitor = SimulationMonitor.instance()
        monitor.init(factory_manager, data_source)

        session.close()

    def set_backward_plan(self):

        factory_manager: FactoryManager = FactoryManager.instance()
        factory_manager.set_backward_plan(orders=self.backward_step_plan_by_loc,
                                          plan_version_dict=self._plan_version_dict)
        factory_manager.set_backward_peg_result(peg_result=self.backward_step_peg_result)

    def backward(self, data_source: AbstractDataSource):
        """

        :return:
        """
        session: AbstractSession = data_source.get_session()
        ########################################################################
        # Backward Process
        ########################################################################
        # 싱글톤 BackwardManager 인스턴스 가져오기
        backward_manager: BackwardManager = BackwardManager.instance()
        work_order_list, route_list, inventory_item_list, wip_list = \
            BackwardBuilder.build(plan_version_dict=self._plan_version_dict,
                                  simulation_dict=self._simulation_dict,
                                  session=session)

        # Initialize Backward Process
        backward_manager.init(work_order_list=work_order_list,
                              route_list=route_list,
                              inventory_item_list=inventory_item_list,
                              wip_list=wip_list)

        # Execute Backward Process
        backward_step_plan_result, backward_step_plan_by_loc, backward_step_peg_result = backward_manager.run()
        self.backward_step_plan_result = backward_step_plan_result
        self.backward_step_plan_by_loc = backward_step_plan_by_loc
        self.backward_step_peg_result = backward_step_peg_result

    def run(self):
        """
        실제 Simulation 을 구동하는 메서드
        :return: void
        """

        print("\nFactorySimulator.run()")

        # 싱글톤 FactoryManager 인스턴스 가져오기
        factory_manager: FactoryManager = FactoryManager.instance()

        # 싱글톤 SimulationMonitor 인스턴스 가져오기
        monitor: SimulationMonitor = SimulationMonitor.instance()

        # 시뮬레이션 시작 전 상황 snapshot
        monitor.snapshot()

        # number_of_digits = 콘솔 출력용 자릿수 값
        # 예를 들어 calendar 갯수가 86400 개라고 하면,
        # number_of_digits 값은 5 가 됨.
        # 콘솔에 출력 시 00000 ~ 86400 으로 캘린더 번호의 자릿수를 맞추기 위한 변수
        horizon: int = self._scheduleManager.length()
        number_of_digits: int = math.floor(math.log(horizon, 10)) + 1

        # 다음 시간 정보가 있는 한 계속 시간을 앞으로 보내도록 설계
        while self._scheduleManager.has_next():
            time: dict = self._scheduleManager.next()
            self._logger.debug(time)

            # 현재 캘린더의 리스트 내 위치 index 를 문자열 Formatting     ex: 00000 ~ 86400
            # idx_string: str = "%0{}d".format(number_of_digits) % time["index"]

            # 현재 RunTime 정보를 Console 에 출력
            # self._logger.debug(f"[{idx_string}] {time['date']}")

            # FactoryManager 인스턴스를 통해 Factory 상황을 1 tick
            factory_manager.run_factory(run_time=time)

            # 현재 RunTime 에서의 시뮬레이션 상황 snapshot 저장
            monitor.snapshot()
