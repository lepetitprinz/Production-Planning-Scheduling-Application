from m4.process.AbstractProcess import AbstractProcess


class Process(AbstractProcess):
    """
    시작과 종료 사이 중간 단계 모든 Process 를 구현
    Warehouse 및 Machine 을 하나 이상 갖고 있으며,
    (단, Warehouse 와 Machine 을 동시에 가질 수 없음)
    Initial, Machine, Warehouse Transfer 등으로부터 작업을 받아다
    자신에게 속한 각 Warehouse 및 Machine 에게 할당하고
    Tick 이 전부 차감되어 완료 처리된 작업은 다음 단계로 이동시킴
    """

    # StartProcess 인스턴스들이 공유할 Static 변수들
    staticVar2: object = None           # Comment

    # StartProcess 인스턴스들이 공유할 Static 상수들
    CONSTANT_VARIABLE2: object = None   # Comment

    def __init__(self):

        # 1. AbstractProcess 클래스에 정의된 멤버 변수들을 상속
        super().__init__()

        # 1. Public
        self.Entities: list = []        # 현재 Process 에 속한 Warehouse 및 Machine 객체들의 리스트

        # 2. Private

    def tick_duration(self):
        pass

    def receive_job(self):
        pass

    def assign_job_to_entity(self, entity: object):
        pass

    def leave_lot(self):
        pass
