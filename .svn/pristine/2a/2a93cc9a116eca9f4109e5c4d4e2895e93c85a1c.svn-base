
import datetime

from ..dao.AbstractSession import AbstractSession
from ..dao.CalendarDAO import CalendarDAO
from ..util.DateTimeUtility import DateTimeUtility
from m4.util.LogHandler import LogHandler


class ScheduleManager(object):
    """
    Schedule Manager Object
    FactorySimulator 객체에 종속되어
    전체 시간의 흐름을 제어하기 위한 클래스,
    시뮬레이션 시간 축 정보를 처리
    """

    def __init__(self):
        # logger
        self._logger = LogHandler.instance().get_logger()
        # 생산 일정 계획 버전 정보
        self._plan_version_dict: dict = None
        # 시뮬레이션 정보
        self._simulation_dict: dict = None
        # 시작 시각
        self._start_date: datetime.datetime = None
        # 종료 시각
        self._end_date: datetime.datetime = None
        # 시간 스텝
        self._delta: int = 0
        # 전체 스텝
        self._horizon: int = 0
        # 시간 배열
        self._time_sequence: list = []
        # 시간 배열 크기
        self._length: int = 0
        # 현재 스텝
        self._current: int = -1

    def init(self, plan_version_dict, simulation_dict, session: AbstractSession):
        """
        ScheduleManager initialize
        :param plan_version_dict : 생산 일정 계획 버전 정보
        :param simulation_dict : 시뮬레이션 정보
        :param session: AbstractSession 인스턴스
        :return: void
        """
        self._plan_version_dict = plan_version_dict
        self._simulation_dict = simulation_dict

        # 설정 정보 Key 로부터 시작일시 종료일시 지정
        start_date_str: str = plan_version_dict['START_DT_HMS']
        end_date_str: str = plan_version_dict['END_DT_HMS']

        # 시작 및 종료 일시, 시간 간격, 전체 시간 크기 설정
        self._start_date: datetime.datetime = DateTimeUtility.convert_str_to_date(start_date_str)
        self._end_date: datetime.datetime = DateTimeUtility.convert_str_to_date(end_date_str)
        self._delta = int(self._create_timedelta(plan_version_dict['UNIT_TM'], plan_version_dict['UNIT_TM_TYP']).total_seconds())
        self._horizon = self._create_horizon(self._start_date, self._end_date)

        # CM_CALENDAR 테이블을 시뮬레이션 기간에 맞게 달력 휴일 정보 조회
        dao: CalendarDAO = CalendarDAO.instance()
        calendar_constraint = dao.map(dao.select_calendar_constraint(session, start_date=start_date_str, end_date=end_date_str, off_day_yn='Y'))

        self._time_sequence = self._create_time_sequence(self._start_date, self._delta, self._horizon, calendar_constraint)
        self._length = len(self._time_sequence)
        self._current = -1

    @staticmethod
    def _create_timedelta(time_step, uom):
        """
        Python 시간 표현에 의한 datetime의 timedelta를 계산
        :param: time_step - time step
        :param: uom - 날짜 표현 코드
        :return: datetime.timedelta
        """
        time_delta: datetime.timedelta = DateTimeUtility.create_timedelta(
            time_step=time_step,
            time_uom=DateTimeUtility.get_python_uom(uom=uom)
        )
        return time_delta

    @staticmethod
    def _create_horizon(start_date, end_date):
        """
        시작 및 종료 시점 정보로부터 시작부터 종료 시점 사이의 전체 시간 간격을 초 단위로 계산
        :param: start_date - 시작 일시
        :param: end_date - 종료 일시
        :return: int
        """
        horizon: datetime.timedelta = end_date - start_date
        return int(horizon.total_seconds())

    @staticmethod
    def _find_constraint(date: datetime.datetime, date_constraint: list):
        """
        date 파라미터 조건에 맞는 date constraint [START_DATE, END_DATE}, [LOWER_BOUND, UPPER_BOUND} 범위의 constraint 조회
        :param: date - 조회 조건 일시
        :param: date_constraint - date constraint
        :return: dict
        """
        for const in date_constraint:
            if const["START_DATE"] <= date < const["END_DATE"]:
                if const["LOWER_BOUND"] <= date < const["UPPER_BOUND"]:
                    return {"is_off_day": True, "constraint_name": const["TM_CONST_NM"], "constraint_type": const["TM_CONST_TYP"]}
        return {}

    def _create_time_sequence(self, start_date, delta, horizon, date_constraint):
        """
        ScheduleManager time sequence를 생성
        전체 일정(start_date, start_date + horizon) 범위에서 delta 간격으로 datetime 생성
        date constraint의 공휴일, 주말 constraint 반영
        :param: start_date - 시작 일시
        :param: delta - step seconds
        :param: horizon - 전체 seconds
        :param: date_constraint - date constraint
        :return: list
        """
        time_sequence = []
        # 0초를 기점으로 self._horizonSec 초까지 self._timestep 간격으로 더해가며 차례로 세팅
        for idx, sec in enumerate(range(0, horizon + delta, delta)):
            date: datetime.datetime = start_date + datetime.timedelta(seconds=sec)

            const = self._find_constraint(date, date_constraint)
            time = {"index": idx, "date": date, "seconds": sec, "is_off_day": False}
            time.update(const)

            # 각 Calendar 정보를 리스트에 순서대로 append 처리
            time_sequence.append(time)

        return time_sequence

    def current(self):
        """
        time sequence의 현재 위치에서 time을 가져옴
        :return: dict
        """
        return self._time_sequence[self._current] if -1 < self._current < self._length else None

    def next(self):
        """
        time sequence의 현재 위치에서 next time을 가져옴
        :return: dict
        """
        self._current = self._current + 1
        return self.current()

    def has_next(self):
        """
        time sequence의 현재 위치에서 next time이 있는지 체크
        time sequence의 next time을 가져오려면 has_next() 호출 후 'True'일 경우 next()를 호출
        :return: boolean
        """
        return self._current + 1 < self._length

    def goto_first(self):
        """
        time sequence의 최초 위치로 이동
        :return: void
        """
        self._current = -1

    def length(self):
        """
        time sequence 크기
        :return: int
        """
        return self._length
