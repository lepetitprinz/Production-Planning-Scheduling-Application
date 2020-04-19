
import numpy as np

from m4.entity.WarehouseSetup import WarehouseSetup


class Warehouse(object):
    """
    Warehouse Object
    각 공정 단계 별 중간 제품 보관 창고를 구현한 클래스
    Process 에 종속되며
    Warehouse Transfer 로부터 자신이 속한 Process 에 작업이 할당되었을 경우
    실제 처리 동작을 수행하도록 설계
    """

    # Warehouse 인스턴스들이 공유할 Static 변수들
    staticVar2: object = None                           # Comment

    # Static Constants
    CONSTANT_VARIABLE2: object = None                   # Comment

    def __init__(self):
        """
        생성자 :
        """

        # 2-1. Public
        self.id: str = ""                               # Warehouse 일련번호
        self.currentCapacity: float = 0.0               # Warehouse 의 남은 보관 가용량
        self.capacity: float = 0.0                      # Warehouse 의 총 보관 가용량
        self.warehouseSetup: WarehouseSetup = None      # Warehouse 의 작업에 필요한 정보들을 모은 객체

        # 2-2. Private : getter 및 setter 를 통해서만 접근 및 변경하도록

    def do_something(self):
        pass

    def _do_my_thang(self):
        pass
