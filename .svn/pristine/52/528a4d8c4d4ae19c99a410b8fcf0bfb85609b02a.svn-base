
from abc import *

from m4.transfer.AbstarctTransfer import AbstractTransfer


class AbstractProcess(metaclass=ABCMeta):
    """
    Process Object
    Factory 에 정의된 각 Process(공정) 들의 상위 클래스
    공정 단계에 따라 다르게 구현
        Start Process   : 시작 단계 Process
        Process         : 중간 단계 Process
        End Process     : 완료 단계 Process
    """

    # Process 클래스를 상속받는 자손 클래스들이 공유할 Static 변수들
    staticVar: object = None

    # Process 클래스 Static Constants
    CONSTANT_VARIABLE: object = None

    def __init__(self):
        """
        생성자 : Process 클래스를 상속받는 자손 클래스들이 공통으로 가질 멤버 변수들
        """

        # 1. Public
        self.processId: str = ""                        # Process ID

        # 2. Private
        self._fromTransfer: AbstractTransfer = None     # The Transfer Object which Gives a New Lot to this Process
        self._entities: list = []                       # The List of Entity Objects   : list<Machine> / list<Warehouse>
        self._toTransfer: AbstractTransfer = None       # The Transfer Object to which this Process Give a Finished Lot
        self._privateVar: object = None                 # Private Variable

    @abstractmethod
    def tick_duration(self):
        """
        Tick 1 Time Unit for each Entities in this Process
        :return: void
        """
        pass

    @abstractmethod
    def receive_job(self):
        """
        Receive a New Job from Transfer
        :return: void
        """
        pass

    @abstractmethod
    def assign_job_to_entity(self, entity: object):
        """
        Assign a New Job from Transfer to an Currently Available Entity
        :param entity: Warehouse or Machine Instance
        :return: void
        """
        pass

    @abstractmethod
    def leave_lot(self):
        """
        작업이 끝난 Lot 들을 내보내는 처리.
        내보낸 Lot 들은 현재 Process 내에서 삭제되며,
        동시에 다음 Process 로의 전달을 위해 Transfer 객체가 받아감
        :return: list<Lot>
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
