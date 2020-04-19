
import datetime
from abc import *


class AbstractCalendar(metaclass=ABCMeta):
    """
    Calendar Object
    Calendar (비가용 계획) 정보 클래스의 상위 클래스
    Calendar 처리 관련 속성 및 동작들이 정의됨
    Calendar 의 성격에 따라 상속받는 클래스를 달리 구현
    """

    # AbstractCalendar 클래스를 상속받는 자손 클래스들이 공유할 Static 변수들
    staticVar: object = None                # Comment

    # AbstractCalendar 클래스 Static Constants
    _CALENDAR_LOCATIONS: list = [           # Policy 의 Location 값으로 가질 수 있는 문자열 목록
        'FACTORY',                          # 공장 전체에 적용
        'MACHINE',                          # 특정 머신에 적용
        'WAREHOUSE'                         # 특정 창고에 적용
    ]

    def __init__(self):
        """
        생성자 : Calendar 클래스를 상속받는 자손 클래스들이 공통으로 가질 멤버 변수들
        """

        # 1. Public
        self.id: str = ""               #

        # 2. Private
        self._location: str = ""        # 'FACTORY', 'MACHINE', 'WAREHOUSE'
        self._priority: int = 0         # 해당 Calendar 의 우선순위 값
        self._durations: list = []      # 해당 Calendar 에 정의된 비가용 시간 Duration(들)의 리스트

    @abstractmethod
    def init(self, location: str, cause: str, priority: int):
        """

        :return: void
        """
        self._set_location(location=location)
        self._set_cause(cause=cause)
        self._set_level(level=priority)

    def append_durations(self):
        pass

    def _append_duration(self):
        pass
