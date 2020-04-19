
from abc import *


class AbstractSetup(metaclass=ABCMeta):
    """
    Machine, Warehouse 인스턴스에 종속되는 작업 관련 정보
        MachineSetup    - Machie 작업 관련 정보
        WarehouseSetup  - Warehouse 작업 관련 정보
    """

    # Setup 클래스를 상속받는 자손 클래스들이 공유할 Static 변수들
    staticVar: object = None                # Comment

    # Setup 클래스 Static Constants
    CONSTANT_VARIABLE: object = None        # Comment

    def __init__(self):
        """
        생성자 :
        """

        # 1. Public
        self.memberVar: object = None       # Comment

        # 2. Private
        self._privateVar: object = None     # Comment

    @abstractmethod
    def do_something(self):
        pass

    @abstractmethod
    def _do_my_thang(self):
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
