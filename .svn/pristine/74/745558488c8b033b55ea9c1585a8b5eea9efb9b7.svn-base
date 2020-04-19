
from m4.process.Item import Item


class ComingItems(dict):
    """
    { Remaining Ticks : [...Items...] }
    """

    def __init__(self):
        super(ComingItems, self).__init__()

        self._moving_time: int = 0

    def init(self, moving_time: int):
        self._moving_time = moving_time

    def receive(self, item: Item):
        new_list = self.get(self._moving_time, [])
        new_list.append(item)
        self.update({self._moving_time: new_list})

    def tick(self):
        if not self.has_items:
            return

        first_arriving_time: int = min(self.keys())
        if first_arriving_time > 0:
            self.update({
                (first_arriving_time - 1): self.get(first_arriving_time - 1, []) + self.pop(first_arriving_time)})
        for remaining_tick in sorted(self.keys())[1:]:
            self.update({
                (remaining_tick - 1): self.get(remaining_tick - 1, []) + self.pop(remaining_tick)})

    def fetch_arriving_items(self):
        return self.pop(0) if 0 in self.keys() else []

    def get_arriving_items(self) -> list:
        return self.get(0, [])

    @property
    def has_items(self):
        return len(self) > 0
