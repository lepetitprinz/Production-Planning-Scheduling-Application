from m4.dao.DemandDao import DemandDao
from m4.process.AbstractProcess import AbstractProcess


class StartProcess(AbstractProcess):
    """
    시작 단계 Process 를 구현
    Demand Dao 인스턴스로부터 Demand 정보에 접근하여
    Initial Transfer 가 Constraint, Optimizer 의 결과로
    다음 Process 로 보내기로 결정한 Lot 을
    출발시키는 지점
    """

    # StartProcess 인스턴스들이 공유할 Static 변수들
    staticVar2: object = None           # Comment

    # StartProcess 인스턴스들이 공유할 Static 상수들
    CONSTANT_VARIABLE2: object = None   # Comment

    def __init__(self):

        # 1. AbstractProcess 클래스에 정의된 멤버 변수들을 상속
        super().__init__()

        # 1. Public
        self.demand: DemandDao = None   # Demand 데이터

        # 2. Private

    def tick_duration(self):
        pass

    def receive_job(self):
        pass

    def assign_job_to_entity(self, entity: object):
        pass

    def leave_lot(self):
        pass
