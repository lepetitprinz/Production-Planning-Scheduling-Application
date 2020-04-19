
import math

from m4.common.SingletonInstance import SingletonInstance
from m4.ApplicationConfiguration import ApplicationConfiguration
from m4.dao.AbstractDataSource import AbstractDataSource
from m4.dao.AbstractSession import AbstractSession
from m4.manager.FactoryBuilder import FactoryBuilder
from m4.manager.FactoryManager import FactoryManager
from m4.manager.ScheduleManager import ScheduleManager
from m4.manager.SimulationMonitor import SimulationMonitor


class FactorySimulator(SingletonInstance):

    def __init__(self):

        # 2-2. Private
        self._scheduleManager: ScheduleManager = ScheduleManager()  # Simulator 전체 시간 범위 ScheduleManager 객체
        self._runTime: dict = {}                                    # Simulator 의 현재 runTime 위치 (int)

    def init(self, config: ApplicationConfiguration, data_source: AbstractDataSource):
        session: AbstractSession = data_source.get_session()

        factory_manager = FactoryManager.instance()
        factory_manager.init(FactoryBuilder.build(session))

        monitor: SimulationMonitor = SimulationMonitor.instance()
        monitor.init(factory_manager, data_source)

        # RuntimeManager 객체 setup
        self._scheduleManager.init(session)

        session.close()

    def run(self):

        # 싱긅톤 SimulationMonitor 인스턴스 가져오기
        monitor: SimulationMonitor = SimulationMonitor.instance()

        # 시뮬레이션 시작 전 상황 snapshot
        monitor.snapshot()

        # number_of_digits = 콘솔 출력용 자릿수 값
        # 예를 들어 calendar 갯수가 86400 개라고 하면,
        # number_of_digits 값은 5 가 됨.
        # 콘솔에 출력 시 00000 ~ 86400 으로 캘린더 번호의 자릿수를 맞추기 위한 변수
        number_of_timesteps: int = self._scheduleManager.get_full_axis_length()
        number_of_digits: int = math.floor(math.log(number_of_timesteps, 10)) + 1

        # 시뮬레이션 시작에 앞서, self._runTime 값을 self._calendar 의 가장 첫 시작 값으로 설정
        self.initialize_runtime()

        # 시뮬레이션 종료 여부를 판단하기 위해, 다음 runTime 이 있는 지 확인을 위한 bool 변수 선언
        has_next_runtime: bool = True

        # 다음 시간 정보가 있는 한 계속 시간을 앞으로 보내도록 설계
        while has_next_runtime:

            # 현재 캘린더의 리스트 내 위치 index 를 문자열 Formatting     ex: 00000 ~ 86400
            idx_string: str = '%0{}d'.format(number_of_digits) % \
                              self._scheduleManager.get_index(run_time=self._runTime)

            print(f"\t[{idx_string}]"               # 각 Calendar 번호: int
                  f"\t{self._runTime['DATE']}"      # 각 Calendar 의 날짜 정보: datetime
                  f"\t{self._runTime['WORK_YN']}"   # 각 Calendar 의 업무 가능 여부: bool
                  )

            # 현재 RunTime 에서의 시뮬레이션 상황 snapshot 저장
            monitor.snapshot()

            # 다음 runTime 이 있는 지 확인 (has_next_runtime: bool)
            # 있으면 True 반환 및 self._runTime을 다음 runTime 값으로 업데이트
            # 없으면 False 반환 및 self._runTime 유지
            has_next_runtime = self.tick_one_time()

    def tick_one_time(self):
        """
        현재 self._runTime 값을 1 Time Step 만큼 미래로 업데이트,
        self._runtimeManager 에 정의된 시간 축을 따라 업데이트 됨
        추후 이 tick 메서드 내부 혹은 전후에서
        Factory 내 각 Entity 들의 Time tick 또한 연동되도록 설계 필요
        :return: bool = 다음 runtime 이 없다면 False, 있다면 True / run_time 메서드에서 참조될 Flag 성 정보
        """

        # 현재 self._runTime 다음 runtime get
        next_runtime: dict = self._scheduleManager.get_next_time(run_time=self._runTime)

        # 다음 runtime 이 비었으면 False
        has_next_runtime: bool = next_runtime != {}

        # 다음 runtime 이 있을 경우에만 현재 ScheduleSimulator 의 self._runTime 값을 업데이트
        if has_next_runtime:
            self._runTime = next_runtime

        return has_next_runtime

    def initialize_runtime(self):
        """
        시뮬레이션 시간 진행을 시작하기에 앞서,
        현재 self._runTime 값을 self._runtimeManager 에 세팅된 시작점으로 세팅하는 처리
        :return: void
        """

        # 시뮬레이션 시작에 앞서, self._runTime 값을 self._calendar 의 가장 첫 시작 값으로 설정
        self._runTime: dict = self._scheduleManager.get_first_time()
