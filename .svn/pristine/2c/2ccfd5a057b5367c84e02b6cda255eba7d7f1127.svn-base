
import numpy as np

from m4.process.AbstractRouteNode import AbstractRouteNode
from ..process.Item import Item
from ..constraint.CapacityConstraint import CapacityConstraint


class Inventory(AbstractRouteNode):
    """
    Inventory Object
    각 공정 단계 별 중간 제품 보관 창고를 구현한 클래스
    Route 로부터 Lot 이 할당되었을 상황에서의
    실제 처리 동작을 수행하도록 설계
    """
    def __init__(self):
        """
        생성자 :
        """

        # 2-1. Public
        self.id: str = ""                       # Inventory 일련번호
        self.name: str = ""                     # Inventory 명칭
        self.plant_id: str = ""

        # 2-2. Private
        self.constraints: CapacityConstraint = None
        # Item별로 재고
        self._stock: dict = {}

    def init(self, info: dict, item_constraint_data: list):
        self.id = info['INV_ID']
        self.name = info['INV_NM']
        self.plant_id = info['PLANT_ID']

        self.constraints = CapacityConstraint()
        self.constraints.init(info['MAX_QTY'], item_constraint_data)

    def check(self, item_id: str, production_need_qty: float):
        """
        check Constraint
        Inventory : CapaConstraint를 체크
        """
        return self.constraints.check(item_id, self._stock, production_need_qty)

    def fetch(self):
        """
        get and remove item quantity
        :return : Item
        """
        pass

    def put(self, item: Item):
        """
        put item
        Inventory : stocks에 item을 추가
        Process : Resource에 ProcessLot을 생성(ProcessLot안에 Lot이 존재)
        """
        items: list = self._stock.get(item.item_id, [])
        items.append(item)
        self._stock[item.item_id] = items

    def run(self):
        """
        tick이 발생했을때 Timer의 age를 증가
        """
        pass

    def get_item_list(self):
        return self._stock
