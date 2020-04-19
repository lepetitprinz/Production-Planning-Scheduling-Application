import sys
import datetime

from m4.process.Item import Item
from m4.process.Runtime import Runtime


class Lot(Runtime):

    def __init__(self, item: Item, time_index: int, date: datetime.datetime, length: int = sys.maxsize):

        #  Runtime 들이 가지는 공통 변수들
        super().__init__(item, time_index, date, length)

        # Lot 만이 가지는 고유한 변수들
        self.move_time: int = 0
        self.queue_time: int = 0
        self.setup_time: int = 0
        self.process_time: int = 0

    def init(self, move_time: int, queue_time: int, setup_time: int, process_time: int):
        self.move_time = move_time
        self.queue_time = queue_time
        self.setup_time = setup_time
        self.process_time = process_time
