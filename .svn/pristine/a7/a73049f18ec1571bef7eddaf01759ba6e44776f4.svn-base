
from m4.transfer.AbstarctTransfer import AbstractTransfer
from m4.transfer.TimeConstraint import TimeConstraint
from m4.transfer.CapaConstraint import CapaConstraint
from m4.transfer.Optimizer import Optimizer


class InitialTransfer(AbstractTransfer):
    """
    Initial Transfer Object
    Lot 을 처음 시작지로부터 출발시키는 이벤트를 담당
    """

    # Static 변수들
    staticVar2: object = None                           # Comment

    # Static Constants
    CONSTANT_VARIABLE2: object = None                   # Comment

    def __init__(self):
        """
        생성자 :
        """

        # Transfer 클래스 공통 멤버 변수들을 상속
        super().__init__()

        # 1. Public
        self.timeConstraint: TimeConstraint = None      # Time Constraint
        self.capaConstraint: CapaConstraint = None      # Capa Constraint
        self.optimizer: Optimizer = None                # Optimizer

        # 2. Private
        self._privateVar: object = None                 # Comment

    def pick_finished_lot(self):
        pass

    def transfer_lot(self):
        pass

    def optimize(self):
        """
        다음 작업 할당을 위한 결정에 앞서
        self.optimizer 에게 .optimize() 동작을 수행
        최적으로 판단되는 순서로 Lot 을 출발시키기 위함
        :return: void
        """
        pass
