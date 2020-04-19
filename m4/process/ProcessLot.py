
import sys
import datetime
import numpy as np

from ..process.Lot import Lot
# from ..process.Runtime import Runtime
from ..process.ProcessQueue import ProcessQueue
from ..process.Item import Item


class ProcessLot(object):
    """
    Process Lot Object
    Machine 객체에 종속되어 Machine 이 할당받은 Lot 을 처리하는 이벤트를 수행하는 클래스
    Setup 객체와 Lot 객체를 포함하며
    Machine 이 Lot 인스턴스를 처리할 때
    Machine 의 Setup Type 변경이 필요할 경우 이를 수행한 후에 하도록 설계
    """

    # Static Variables
    staticVar2: object = None               # Comment

    # Static Constants
    _STEP = {
        0: "SETUP",
        1: "PROCESS",
        2: "FINISHED"
    }

    def __init__(self):
        """
        생성자 :
        """

        # 2-2. 소요 시간 정보
        # self._before_move_time: int = 0     # 전달받아 올 장소로부터 현재 위치까지의 이동 소요 시간
        # self._before_que_time: int = -1     # Item 이 Process 의 Queue 에 도착한 후 앞서 들어간 Item 의 처리를 기다린 경과 시간
        self._current: int = -1             # 현재 처리중인 Item 이 시작된 후부터 경과 시간  >> SETUP/PROCESS 상태 판단에 필요
        self._setup_time: int = 0           # (현재 처리중인 Item 에 따라 다름) Setup 소요 시간
        self._process_time: int = 0         # (현재 처리중인 Item 에 따라 다름) Process 소요 시간

        # MOVE -> QUE -> (SETUP) -> PROCESS
        self._moves: list = []                      # 현재 Process 위치로 오는 중인 Item 들의 시간 정보를 관리하는 dict
        self._queue: ProcessQueue = ProcessQueue()  # 이전 Router 로부터 도착한 Item 들의 QUEUE 대기열
        self._lot: Lot = None                  # 현재 처리중인 Item, Idle 일 경우 None

        # 다음 Router로 보낼 처리 완료 Item 들을 보관
        self._wait_items: dict = dict()             # { ItemCode : [..., Item, ...] }

        #
        self._status_change: bool = False

    def init(self, info: dict):
        """
        Hard Coded for Test
        :return: void
        """
        pass

        # 도착 소요 시간 정보 세팅
        # self._before_move_time = 1

    def put(self, lot: Lot):

        if lot.get_length() > 0:

            lot.archive(time_index=0, date=0)
            lot.archive(time_index=0, date=0)

            self._moves.append(lot)

            return

        if not self._queue.has_items:

            lot.archive(time_index=0, date=0)

            self._queue.put(lot=lot)

            return

        # if self.status not in ["SETUP", "PROCESS"]:
        #     self._item

    def receive_arrived(self):
        for obj in self.arrived_items:
            lot: Lot = self._moves.pop(self._moves.index(obj))
            lot.reset(time_index=1, date=None, length=lot.queue_time)

            lot.archive(time_index=1, date=1)

            self._queue.put(lot=lot)

    def run(self):

        for run_time in self._moves:
            run_time.run()

        self._queue.run()

        if self.has_arrived:
            self.receive_arrived()

        if self.status == "IDLE":
            if self._queue.has_items:
                self.assign_lot()

        elif self.status in ["SETUP", "PROCESS"]:
            self._current += 1

        elif self.status == "FINISHED":
            self.finish_process()

    def is_available(self, date: datetime.datetime, item_id: str, quantity: float, move_time: int):
        _available: bool = self.status == "IDLE"
        return _available

    def assign_lot(self):

        self._lot: Lot = self._queue.fetch()
        self._lot.reset(time_index=2, date=None, length=self._lot.setup_time)

        self._lot.archive(time_index=2, date=2)

        self._setup_time = self._lot.setup_time
        self._process_time = self._lot.process_time

        self._reset_current()

    def finish_process(self):
        if self.status != "FINISHED":
            return
        self._add_finished_item()
        self._lot = None

    def _add_finished_item(self):

        item: Item = self._lot.get_item()

        item.archive(time_index=5, date=5)

        self._wait_items.update(
            {item.item_id: self._wait_items.get(item.item_id, []) + [item]}
        )

    def get(self, item_code: str):
        return self._wait_items.get(item_code, [])

    def fetch(self, item_code: str):
        if not self.get(item_code=item_code):
            return []
        return self._wait_items.pop(item_code)

    def _reset_current(self):
        self._current = 0

    @property
    def has_arrived(self):
        return len(self.arrived_items) > 0

    @property
    def arrived_items(self):
        return [run_time for run_time in self._moves if run_time.get_current() == run_time.get_length()]

    @property
    def status(self):
        if self._lot is None:
            return "IDLE"
        for i in range(0, len(self._time_thresholds)):
            if self._current <= self._time_thresholds[i]:
                return self._STEP.get(i)

    @property
    def _time_thresholds(self) -> list:
        return list(map(int, np.cumsum([self._setup_time, self._process_time, sys.float_info.max])))
