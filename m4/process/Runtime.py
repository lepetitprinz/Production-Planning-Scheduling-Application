import sys
import datetime

from m4.process.Item import Item


class Runtime(object):

    def __init__(self, item: Item, time_index: int, date: datetime.datetime, length: int = sys.maxsize):
        self.item: Item = item
        self.time_index: int = time_index
        self.date: datetime.datetime = date

        self._length: int = length
        self._current: int = 0

    def run(self):
        if self._current == self._length:
            return
        self._current += 1

    def is_end(self):
        return self._current == self._length

    def get_item(self):
        return self.item

    def reset(self, time_index: int, date: datetime.datetime, length: int = sys.maxsize):
        self.time_index: int = time_index
        self.date: datetime.datetime = date

        self._length: int = length
        self._current: int = 0

    def get_current(self):
        return self._current

    def get_length(self):
        return self._length

    def archive(self, time_index: int, date: datetime.datetime):
        self.item.archive(time_index=time_index, date=date)
