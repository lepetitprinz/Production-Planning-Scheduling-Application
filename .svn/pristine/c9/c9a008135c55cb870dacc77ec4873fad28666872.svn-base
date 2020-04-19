
import datetime
from abc import *

from m4.util.TimeUtility import TimeUtility


class AbstractDuration(metaclass=ABCMeta):
    """
    Duration Object
    Calendar (비가용 계획) 인스턴스가 가질
    비가용 계획 구간 정보 리스트는 Duration 인스턴스(들)로 구성
    Duration 처리 관련 속성 및 동작들이 정의됨
    """

    # Duration 클래스 공통 Static 변수들
    staticVar: object = None  # Comment

    def __init__(self):
        """
        생성자 : Duration 클래스를 상속받는 자손 클래스들이 공통으로 가질 멤버 변수들
        """

        # 2-1. Public
        self.id: str = ""                           # Duration ID

        # 2-2. Private
        self._intervals: list = []                  # 비가용 계획 구간 리스트 [(시작 시간, 종료 시간)] : DailyOnce 는 하나의 튜플만 가짐

    def init(self, id_name: str, cycle_type: str):
        """

        :param id_name:
        :param cycle_type:
        :return:
        """

        # 2-1. Public
        self.id = id_name

        # 2-2. Private
        self._set_cycle_type(cycle_type=cycle_type)

    @abstractmethod
    def clip_duration(self,
                      from_date: datetime.datetime,
                      to_date: datetime.datetime):
        """

        :param from_date:
        :param to_date:
        :return:
        """
        pass

    @abstractmethod
    def get_current_duration(self):
        pass

    @abstractmethod
    def set_time(self, start_date: object, end_date: object):
        pass

    def _set_cycle_type(self, cycle_type: str):
        """

        :param cycle_type:
        :return:
        """
        self._cycleType = cycle_type
