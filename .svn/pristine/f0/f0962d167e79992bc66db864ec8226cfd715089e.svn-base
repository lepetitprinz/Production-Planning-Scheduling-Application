import sys
import datetime

from m4.constraint.ScheduleConstraint import ScheduleConstraint
from ..operator.Resource import Resource
from m4.process.ProcessLot import ProcessLot
from ..process.ProcessLots import ProcessLots
from m4.process.Item import Item


class ProcessResource(object):
    """
    Process Resource Object
    각 공정 단계 별 생산 장비를 구현한 클래스
    Process 에 종속되며
    Route 로부터 자신이 속한 Process 에 작업이 할당되었을 경우
    실제 처리 동작을 수행하도록 설계
    """
    STATUS_IDLE: str = "IDLE"
    STATUS_PROCESSING: str = "PROC"
    STATUS_DOWN: str = "DOWN"

    def __init__(self):
        """
        생성자 :
        """

        # 2-1. Public
        self.process_id: str = ""                       # Process ID
        self.resource_id: str = ""                      # Resource ID
        self.name: str = ""                             # BOR 명칭

        # 2-2. Private
        self._resource: Resource = None
        self._priority: int = 0
        self._production_efficiency: float = 0.0
        self._process_precision: float = 0.0
        self._min_lot_size: float = 0.0
        self._max_lot_size: float = 0.0
        self._process_time: float = 0.0
        self._setup_time: float = 0.0
        self._queue_time: float = 0.0
        self._wait_time: float = 0.0
        self._move_time: float = 0.0

        self._process_lots: ProcessLots = ProcessLots()        # Resource 의 실제 작업을 수행하는 객체

    def init(self, info: dict, resource: Resource):
        """

        :param info:
        :param resource:
        :return:
        """

        self.process_id = info['PROC_ID']
        self.resource_id = info['RESC_ID']
        self.resource_id = info['BOR_NM']

        self._resource = resource
        self._priority: int = info['PRIORITY']
        self._production_efficiency: float = info['PROD_EFFCNCY']
        self._process_precision: float = info['PROC_PRECSN']
        self._min_lot_size: float = info['MIN_LOT_SIZE']
        self._max_lot_size: float = sys.float_info.max if info['MAX_LOT_SIZE'] is None or info['MAX_LOT_SIZE'] == 0 else info['MAX_LOT_SIZE']
        self._process_time: float = info['PROC_TM']
        self._setup_time: float = info['PRE_PROC_SETUP_TM']
        self._queue_time: float = 0
        self._wait_time: float = info['POST_PROC_WAIT_TM']
        self._move_time: float = 0

    def check(self):
        """

        :return:
        """
        print(f"\t\t\t\t\t\tChecking {self.__class__.__name__} {self.id} ...")

    def put(self, item: Item, run_time: dict):
        process_lot: ProcessLot = ProcessLot()
        process_lot.init(item=item)
        self._process_lots.append(process_lot)

    def tick(self):
        """

        :return:
        """
        for obj in self._process_lots:
            process_lot: ProcessLot = obj
            process_lot.tick()

    def fetch(self):
        items: list = []
        for obj in self._process_lots:
            process_lot: ProcessLot = obj
            if not process_lot.has_next:
                pass
        return items

    def set_priority(self, priority: int):
        self._priority = priority

    def set_production_efficiency(self, production_efficiency: float):
        self._production_efficiency = production_efficiency

    def set_process_precision(self, process_precision: float):
        self._process_precision = process_precision

    def set_min_lot_size(self, min_lot_size: float):
        self._min_lot_size = min_lot_size

    def set_max_lot_size(self, max_lot_size: float):
        self._max_lot_size = max_lot_size

    def set_process_time(self, process_time: float):
        self._process_time = process_time

    def set_pre_process_queue_time(self, pre_process_queue_time: float):
        self._queue_time = pre_process_queue_time

    def set_pre_process_setup_time(self, pre_process_setup_time: float):
        self._setup_time = pre_process_setup_time

    def set_post_process_wait_time(self, post_process_wait_time: float):
        self._wait_time = post_process_wait_time

    def set_post_process_move_time(self, post_process_move_time: float):
        self._move_time = post_process_move_time
