import datetime
from collections import defaultdict
from itertools import chain

from m4.util.LogHandler import LogHandler
from m4.process.AbstractRouteNode import AbstractRouteNode
from m4.process.ProcessException import ProcessException
from ..process.Item import Item
from ..process.Runtime import Runtime
from ..constraint.CapacityConstraint import CapacityConstraint


class Inventory(object):
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
        # logger
        self._logger = LogHandler.instance().get_logger()
        self._constraints: CapacityConstraint = None

        # Item별로 재고
        self._moves: list = []
        self._stock: dict = {}

    def init(self, info: dict, item_constraint_data: list):
        self.id = info['INV_ID']
        self.name = info['INV_NM']
        self.plant_id = info['PLANT_ID']

        self._constraints = CapacityConstraint()
        self._constraints.init(info['MAX_QTY'], item_constraint_data)

    def _get_moves_dict(self):
        ret: dict = defaultdict(list)
        for item in self._moves:
            ret[item.item_id].append(item)
        return ret

    def check_availables(self, date: datetime.datetime, item_id: str, quantity: float, move_time: int):
        """
        check Available status
        Inventory : CapaConstraint를 체크
        Process : ProcessResource의 queue 사이즈 체크, Time/Capa Constraint 체크
        :param : item_id
        :param : quantity
        :param : move_time
        :return : Inventory일 경우 가용 여부, Process일 경우 Resource ID
        """
        moves_dict: dict = self._get_moves_dict()
        items = defaultdict(list)
        for key, val in chain(self._stock.items(), moves_dict.items()):
            items[key].append(val)

        if self._constraints.check(item_id, items, quantity) is None:
            return self.id

        return None

    def fetch(self,
              time_index: int,
              date: datetime.datetime,
              item_id: str,
              work_order_id: str,
              quantity: float = 0):
        """
        get and remove item quantity
        :param : item_id
        :param : quantity
        :return : Item
        """
        stock_items: list = self._stock.get(item_id, [])

        stock_quantity: float = 0
        for item in stock_items:
            if item.work_order_id != work_order_id:
                continue
            stock_quantity += item.get_quantity()

        if quantity != 0:
            if stock_quantity < quantity:
                return None
            elif stock_quantity > quantity:
                raise ProcessException(
                    f"[Inventory {self.id}:{self.name}] : {item_id}:{work_order_id} - stock quantity exceed fetch quantity")

        items = []
        for item in stock_items:
            if item.work_order_id != work_order_id:
                continue
            items.append(item)
            stock_items.remove(item)

        self._logger.info(
            f"[Inventory {self.id}:{self.name}] : {item_id}:{work_order_id} - fetched {quantity} from {len(items)} items")

        return items

    def put(self, time_index: int, date: datetime.datetime, item: Item, move_time: int):
        """
        put item
        Inventory, ProcessResource의 ProcessLot의 moves에 Item 추가
        :param : item
        """
        # item archive 처리
        item.archive(time_index, date)

        if move_time != 0:
            runtime: Runtime = Runtime(item, time_index, date, move_time)
            self._moves.append(runtime)
            return

        items: list = self._stock.get(item.item_id, [])
        items.append(item)
        self._stock[item.item_id] = items

    def run(self, time_index: int, date: datetime.datetime):
        """
        FactorySimulator에서 tick이 발생했을때 aging 처리 전파
        """
        pass

    def get_item_dict(self):
        return self._stock

    def set_item_dict(self, stock_dict):
        self._stock = stock_dict
