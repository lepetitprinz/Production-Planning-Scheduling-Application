import sys
from m4.constraint.AbstractConstraint import AbstractConstraint
from m4.constraint.ItemConstraint import ItemConstraint


class CapacityConstraint(AbstractConstraint):
    """
    Capacity Constraint Object
    """

    def __init__(self):
        """
        Capacity Constraint 생성자
        """
        super().__init__("CAPA", "Capacity Constraint", "CAPA_CONST")
        self.max_quantity: float = None
        # item constraints - item 별로 저장
        self.item_constraints: dict = {}

    def init(self, max_quantity: float, item_constraint_data: list):
        self.max_quantity = sys.float_info.max if max_quantity is None or max_quantity == 0 else max_quantity
        for const in item_constraint_data:
            item_constraint: ItemConstraint = ItemConstraint()
            item_constraint.init(const)
            self.item_constraints[const['ITEM_ID']] = item_constraint

    def check(self, item_id: str, stock: dict, quantity: float):
        total_quantity: float = 0
        for items in stock.values():
            for item in items:
                total_quantity = total_quantity + item.get_quantity()

        if total_quantity + quantity > self.max_quantity:
            return self

        item_constraint: ItemConstraint = self.item_constraints.get(item_id)
        # item constraint가 있는 경우
        if item_constraint is not None:
            return item_constraint.check(item_id, stock.get(item_id), quantity)

        return None
