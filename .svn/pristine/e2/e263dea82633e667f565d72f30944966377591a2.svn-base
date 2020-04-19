import datetime

from ..constraint.AbstractConstraint import AbstractConstraint
from ..constraint.ScheduleConstraint import ScheduleConstraint
from ..operator.Inventory import Inventory
from ..operator.Process import Process
from ..process.AbstractRouteNode import AbstractRouteNode
from ..process.Router import Router
from ..process.Item import Item
from ..backward.BackwardStepPlan import BackwardStepPlan


class Factory(object):
    """
    Factory Object

    """

    def __init__(self):

        # 멤버 변수 목록
        self.id: str = ""  #
        self.name: str = ""  #
        self.location_id: str = ""  #

        # 2-2. Private 멤버 변수 목록
        self._schedule_constraint: ScheduleConstraint = None  # 공장 비가용 계획 캘린더 인스턴스 사전 {CalendarID: Calendar}
        self._routers: dict = {}  # Route 객체 리스트 = inventory 및 process 간 연결 관계 정의
        self._inventories: dict = {}  # Inventory 객체 리스트
        self.processes: dict = {}  # Process 객체 리스트

        # Demand
        # self._demand_list: list = []

        # Route 관련
        self._work_order_list: list = []
        self._router_sequence: dict = {}
        self._next_to_curr_item_dict: dict = {}
        self._item_to_final_item_dict: dict = {}
        self._next_to_curr_location_dict: dict = {}

    def init(self,
             info: dict,
             schedule_constraint: ScheduleConstraint,
             inventories: dict,
             processes: dict,
             work_order_list: list,
             next_to_curr_item_dict: dict,
             item_to_final_item_dict: dict,
             next_to_curr_location_dict: dict,
             routes: list,
             router_sequence: dict):

        # 공장 정보 설정
        self._init_info(info=info)

        # 공장 비가용 Calendar 정보 세팅
        self._init_schedule_constraint(schedule_constraint=schedule_constraint)

        # 공장 내 Inventory 객체들을 초기화
        self._init_inventories(inventories=inventories)

        # 공장 내 Process 객체들을 초기화 : Propagate
        self._init_processes(processes=processes)

        # 공장 내 Route 객체들을 초기화
        self._init_routes(routes=routes)

        # Work Order 정보 초기화
        self._init_work_orders(work_order_list=work_order_list)

        #
        self._init_next_to_curr_item_dict(to_from_item_dict=next_to_curr_item_dict)

        #
        self._init_item_to_final_item_dict(item_to_final_item_dict=item_to_final_item_dict)

        #
        self._init_next_to_curr_location_dict(to_from_location_dict=next_to_curr_location_dict)

        #
        self._init_router_sequence(router_sequence=router_sequence)

        # 최초 출발지 Inventory 에 Work Order Item 인스턴스들을 할당
        # self._init_initial_items(work_order_items=work_order_items)

    def set_backward_plan(self, orders: dict):

        sequence_indices: list = sorted(self._router_sequence.keys())
        sequence_depth: int = max(sequence_indices)

        for obj in self._routers:
            router: Router = obj
            router_orders: list = orders.get(router.route_location.id, [])
            router.set_production_orders(production_orders=router_orders)

        for obj in self._starting_routers:
            router: Router = obj
            router_orders: list = orders.get(router.route_location.id, [])
            for obj2 in router_orders:
                step_plan: BackwardStepPlan = obj2
                item: Item = Item()
                item.init(info=step_plan)
                router.route_location.put(item=item)

        # for index in sequence_indices:
        #     for obj in self._router_sequence[index]:
        #         router: Router = obj
        #         prior_routers: list = \
        #             [] if index == sequence_depth else \
        #             [pr for pr in self._router_sequence[index + 1]
        #              if router.route_location in pr.get_next_locations()]
        #
        #         if len(prior_routers) == 0:
        #             for router_order in router_orders:
        #                 item: Item = Item()
        #                 item.init(info=router_order.__dict__)
        #                 router.route_location.put(item=item)

    def run(self, run_time: dict, time_constraint: object = None):
        """

        :param run_time:
        :param time_constraint:
        :return:
        """
        self._run_reverse(run_time=run_time, time_constraint=time_constraint)

    def _run_reverse(self, run_time: dict, time_constraint: object = None):
        for obj in self.processes.values():
            process: Process = obj
            process.tick()

        for route_step in sorted(self._router_sequence.keys()):
            for obj in self._router_sequence[route_step]:
                router: Router = obj
                router.run(run_time=run_time)

    def get_time_constraints(self, run_time: dict):
        """

        :param run_time:
        :return:
        """

        if run_time['is_off_day']:
            return run_time
        else:
            current_time_constraint: AbstractConstraint = self._get_current_schedules(run_time=run_time['date'])
            return current_time_constraint

    def get_router_by_location_id(self, route_id: str):
        """

        :param route_id:
        :return:
        """
        if route_id in self._routers.keys():
            return self._routers[route_id]
        else:
            return None

    def get_process(self, process_id: str):
        """

        :param process_id:
        :return:
        """
        if process_id in self.processes.keys():
            return self.processes[process_id]
        else:
            return None

    def get_inventory(self, inventory_id: str):
        """

        :param inventory_id:
        :return:
        """
        return self._inventories.get(inventory_id, None)

    def get_previous_location(self, next_location: str):
        """

        :return:
        """
        return self._next_to_curr_location_dict[next_location]

    def _get_current_schedules(self, run_time: datetime.datetime):
        """

        :param run_time:
        :return:
        """

        return self._schedule_constraint.check(run_time)

    def _init_work_orders(self, work_order_list: list):
        """

        :param work_order_item_list:
        :return:
        """
        self._work_order_list = work_order_list

    def _init_initial_items(self, work_order_items: list):
        """

        :param work_order_items:
        :return:
        """
        starting_routers: list = self._get_initial_routers()
        if len(starting_routers) == 0:
            raise AssertionError(
                ""
            )
        elif len(starting_routers) == 1:
            starting_router: Router = starting_routers[0]
            starting_inventory: Inventory = starting_router.route_location
            for item in work_order_items:
                starting_inventory.put_initial_item(item=item)
        else:
            # 2 군데 이상의 Starting Inventory 가 있는 경우
            # 구현 필요
            pass

    def _get_initial_routers(self):
        """
        <Hard Coding>
        구현 필요
        self._routers 리스트로부터 가장 출발점 Router 들을 반환
        :return:
        """
        return [router for router in self._routers
                if isinstance(router.route_location, Inventory) and router.route_location.start_flag is True]

    def _init_next_to_curr_item_dict(self, to_from_item_dict: dict):
        """

        :param to_from_item_dict:
        :return:
        """
        self._next_to_curr_item_dict = to_from_item_dict

    def _init_item_to_final_item_dict(self, item_to_final_item_dict: dict):
        """

        :param item_to_final_item_dict:
        :return:
        """
        self._item_to_final_item_dict = item_to_final_item_dict

    def _init_next_to_curr_location_dict(self, to_from_location_dict: dict):
        """

        :param _init_to_from_location_dict:
        :return:
        """
        self._next_to_curr_location_dict = to_from_location_dict

    def _init_routes(self, routes: list):
        """

        :param routes:
        :return:
        """
        self._routers = routes

    def _init_router_sequence(self, router_sequence: dict):
        """

        :param router_sequence:
        :return:
        """
        self._router_sequence = router_sequence

    def _init_processes(self, processes: dict):
        """

        :param process_master:
        :return:
        """
        self.processes = processes

    def _init_inventories(self, inventories: dict):
        """

        :param inventories:
        :return:
        """
        self._inventories = inventories

    def _init_info(self, info: dict):
        """

        :param info:
        :return:
        """

        self.id = info['PLANT_ID']
        self.name = info['PLANT_NM']
        self.location_id = info['LOC_ID']

    def _init_schedule_constraint(self, schedule_constraint: ScheduleConstraint):
        """

        :param schedule_constraint:
        :return:
        """
        self._schedule_constraint = schedule_constraint

    def _init_loc_to_route_dict(self, loc_to_route_dict: dict):
        """

        :param loc_to_route_dict:
        :return:
        """
        self._loc_to_route_dict = loc_to_route_dict

    @property
    def _starting_routers(self) -> list:
        sequence_indices: list = sorted(self._router_sequence.keys())
        sequence_depth: int = max(sequence_indices)

        routers: list = []
        for index in sequence_indices:
            for obj in self._router_sequence[index]:
                router: Router = obj
                prior_routers: list = \
                    [] if index == sequence_depth else \
                    [pr for pr in self._router_sequence[index + 1]
                     if router.route_location in pr.next_locations]

                if len(prior_routers) == 0:
                    routers.append(router)
        return routers
