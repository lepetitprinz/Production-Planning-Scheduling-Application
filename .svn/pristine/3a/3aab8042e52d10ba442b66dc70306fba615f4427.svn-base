from m4.process.AbstractRouteNode import AbstractRouteNode
from ..operator.Resource import Resource
from ..operator.ProcessResource import ProcessResource
from ..process.Item import Item


class Process(AbstractRouteNode):
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
        self.id: str = ""                       # Inventory 일련번호
        self.name: str = ""                     # Inventory 명칭

        # 2-2. Private
        self._process_resources: dict = {}              # Resource 인스턴스 목록

    def init(self, info: dict):
        self.id = info['PROC_ID']
        self.name = info['PROC_NM']

    def add_process_resource(self, info: dict, resource: Resource):
        process_resource = ProcessResource()
        process_resource.init(info, resource)
        self._process_resources[info['RESC_ID']] = process_resource

    def get_process_resource(self, resource_id: str):
        """

        :param resource_id:
        :return:
        """
        return self._process_resources.get(resource_id, None)

    def check(self):
        """
        check Constraint
        Inventory : CapaConstraint를 체크
        Process : Resource에 empty 상태인 체크, Time/Capa Constraint 체크
        """
        print(f"\t\t\t\t\tChecking Process ...")
        for obj in self._process_resources.values():
            # super().__init__()

            resource: Resource = obj
            resource.check()

    def tick(self):
        """

        :return:
        """
        for obj in self._process_resources.values():
            resource: ProcessResource = obj
            resource.tick()

    def get_resource(self, resource_id: str):
        """

        :param resource_id:
        :return:
        """
        return self._process_resources.get(resource_id, None)

    def fetch(self):
        """
        get and remove item quantity
        :return : Item
        """
        pass

    def put(self, item: Item, run_time: dict):
        """
        put item
        Inventory : stocks에 item을 추가
        Process : Resource에 ProcessLot을 생성(ProcessLot안에 Lot이 존재)
        """
        for obj in self._process_resources:
            resource: ProcessResource = obj
            resource.put(item=item, run_time=run_time)

    def run(self):
        """
        tick이 발생했을때 Timer의 age를 증가
        """
        pass
