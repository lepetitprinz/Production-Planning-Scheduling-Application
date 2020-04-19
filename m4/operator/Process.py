import datetime

from m4.process.AbstractRouteNode import AbstractRouteNode
from ..operator.Resource import Resource
from ..operator.ProcessResource import ProcessResource
from ..process.ProcessException import ProcessException
from ..process.Item import Item


class Process(object):
    """
    Process Object
    각 공정 구현한 클래스
    Route로부터 Lot 이 할당되었을 상황에서의
    실제 처리 동작을 수행하도록 설계
    """

    def __init__(self):
        """
        생성자 :
        """

        # 2-1. Public
        self.id: str = ""                       # Process 일련번호
        self.name: str = ""                     # Process 명칭

        # 2-2. Private
        self._process_resources: dict = {}              # Process Resource 인스턴스 목록

    def init(self, info: dict):
        self.id = info['PROC_ID']
        self.name = info['PROC_NM']

    def add_process_resource(self, info: dict, resource: Resource):
        process_resource = ProcessResource()
        process_resource.init(info, resource)
        self._process_resources[info['RESC_ID']] = process_resource

    def get_process_resources(self):
        """

        :param resource_id:
        :return:
        """
        return self._process_resources

    def get_process_resource(self, resource_id: str):
        """

        :param resource_id:
        :return:
        """
        return self._process_resources.get(resource_id, None)

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
        for obj in self._process_resources.values():
            resource: ProcessResource = obj
            is_available: bool = resource.is_available(date, item_id, quantity, move_time)
            if is_available:
                return resource.id
        return None

    def fetch(self, time_index: int, date: datetime.datetime, item_id: str, work_order_id: str, quantity: float = 0):
        """
        get and remove item quantity
        :param : item_id
        :param : quantity
        :return : Item
        """
        product_quantity: float = 0
        for obj in self._process_resources.values():
            resource: ProcessResource = obj
            product_quantity += resource.get_quantity(item_id, work_order_id)

        if quantity != 0:
            if product_quantity < quantity:
                return None
            elif product_quantity > quantity:
                raise ProcessException(f"[Process {self.id}:{self.name}] : {item_id}:{work_order_id} - product quantity exceed fetch quantity")

        items = []
        for obj in self._process_resources.values():
            resource: Resource = obj
            ret: list = resource.fetch(time_index, date, item_id, work_order_id, quantity)
            items.extend(ret)

        self._logger.info(f"[Process {self.id}:{self.name}] : {item_id}:{work_order_id} - fetched {quantity} from {len(items)} items")

        return items

    def put(self, time_index: int, date: datetime.datetime, item: Item, move_time: int, resource_id: str):
        """
        put item
        Inventory, ProcessResource의 ProcessLot의 moves에 Item 추가
        :param : item
        """
        resource: Resource = self._process_resources[resource_id]
        resource.put(time_index, date, item, move_time, resource_id)

    def run(self, time_index: int, date: datetime.datetime):
        """
        FactorySimulator에서 tick이 발생했을때 aging 처리 전파
        """
        for obj in self._process_resources.values():
            resource: ProcessResource = obj
            resource.run(time_index, date)
