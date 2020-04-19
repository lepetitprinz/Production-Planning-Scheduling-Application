from m4.process.AbstractProcess import AbstractProcess


class EndProcess(AbstractProcess):
    """
    종료 단계 Process 를 구현
    End Transfer 가 직전 Process 로부터 전달해 준 Lot 을
    최종 생산물을 의미하는 Product 객체로 처리하여 내보내는 단계
    즉, End Process 가 전달받은 Lot 은
    전달된 시점에서 모든 공정을 거쳐 완료 처리됨
    """

    # StartProcess 인스턴스들이 공유할 Static 변수들
    staticVar2: object = None           # Comment

    # StartProcess 인스턴스들이 공유할 Static 상수들
    CONSTANT_VARIABLE2: object = None   # Comment

    def __init__(self):

        # 1. AbstractProcess 클래스에 정의된 멤버 변수들을 상속
        super().__init__()

        # 1. Public

        # 2. Private
        self._products: list = []       # 모든 공정을 거쳐온 Product 들의 리스트

    def tick_duration(self):
        pass

    def receive_job(self):
        pass

    def assign_job_to_entity(self, entity: object):
        pass

    def leave_lot(self):
        pass
