from m4.constraint.AbstractConstraint import AbstractConstraint
from m4.process.Item import Item


class ItemConstraint(AbstractConstraint):
    """
    Item Constraint
    """
    def __init__(self):
        """
        생성자 :
        """
        self.inv_id: str = None

        self._item_id: str = None
        self._max_quantity: float = None
        self._load_rate: float = None

    def init(self, info: dict):
        self.inv_id: str = info['INV_ID']
        self._item_id: str = info['ITEM_ID']
        self._max_quantity: float = info['MAX_QTY']
        self._load_rate: float = info['LOAD_RATE']

    def check(self, item_id: str, stock: list, quantity: float):
        if stock is None:
            return True

        total_quantity: float = 0
        for item in stock:
            total_quantity = total_quantity + item.get_quantity()
        if item_id == self._item_id and 0 < total_quantity + quantity <= self._max_quantity*self._load_rate:
            return True

        return False

    def get_item_id(self):
        return self._item_id


