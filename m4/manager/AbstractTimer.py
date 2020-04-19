
from abc import *


class AbstractTimer(metaclass=ABCMeta):
    """
    Timer Object
    Aging 처리가 필요한 클래스를 위한 상위 클래스
    Aging 관련 속성 및 동작들이 정의됨
        - Setup : Machine 인스턴스의 SetupType 멤버 변수 값이 변경될 때 소요되는 시간을 구현하기 위해 Timer 클래스를 상속
        - Lot   : Machine 인스턴스가 자신에게 할당된 Lot 을 처리하는 데 소요되는 시간
                  Warehouse 인스턴스가 자신에게 할당된 Lot 을 처리하는 데 소요되는 시간 구현하기 위해 Timer 클래스를 상속
    """

    # Timer 클래스를 상속받는 자손 클래스들이 공유할 Static 변수들
    staticVar: object = None                # Comment

    # Timer 클래스 Static Constants
    CONSTANT_VARIABLE: object = None        # Comment

    def __init__(self):
        """
        생성자 : Timer 클래스를 상속받는 자손 클래스들이 공통으로 가질 멤버 변수들
        """

        # 1. Public

        # 2. Private
        self._privateVar: object = None     # private 변수 쓰는 법
        self._duration: object = 0.0        # Duration 길이를 의미 : Type ?
        self._fromTime: object = None       # Duration Tick 차감 시작 시점 : Type ?
        self._toTime: object = None         # Duration Tick 차감 완료 시점 : Type ?

    def tick(self):
        """
        Duration 을 1 Tick 만큼 차감하는 처리
        :return: void
        """
        pass

    def finish_duration(self):
        """
        Duration Tick 이 모두 차감되었음을 알리는 처리
        :return: bool ? (signal 을 줄 지 ? 뭔가 정보들을 담고 있는 객체를 줄 지 ?)
        """
        pass

    def get_private_var(self):
        """
        Private Variable Getter
        :return: self._privateVar.__class__
        """
        return self._privateVar

    def set_private_var(self, value: object):
        """
        Private Variable Value Setter
        :param value: self._privateVar.__class__
        :return: void
        """
        self._privateVar = value
