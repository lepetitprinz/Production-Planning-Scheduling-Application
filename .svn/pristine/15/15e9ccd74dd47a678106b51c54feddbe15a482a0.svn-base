
from m4.entity.ProcessLot import ProcessLot
from m4.entity.MachineSetup import MachineSetup


class Machine(object):
    """
    Machine Object
    각 공정 단계 별 생산 장비를 구현한 클래스
    Process 에 종속되며
    Machine Transfer 로부터 자신이 속한 Process 에 작업이 할당되었을 경우
    실제 처리 동작을 수행하도록 설계
    """

    #  Static 변수들
    staticVar: object = None                    # Comment

    # Static Constants
    CONSTANT_VARIABLE: object = None            # Comment

    def __init__(self):
        """
        생성자 :
        """

        # 2-1. Public
        self.id: str = ""                       # Machine 일련번호
        self.status: str = ""                   # Machine 의 현재 상태. PROC / IDLE / DOWN
        self.macSetup: MachineSetup = None      # Machine 의 작업에 필요한 정보들을 모은 객체

        # 2-2. Private
        self._processLot: ProcessLot = None     # Machine 의 실제 작업을 수행하는 객체

    def do_something(self):
        """
        Write Me Up and Comment Here
        :return: void
        """
        pass

    def _do_my_thang(self):
        """
        Write Me Up and Comment Here
        :return: void
        """
        pass
