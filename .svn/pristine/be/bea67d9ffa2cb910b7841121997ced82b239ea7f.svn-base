
import datetime

from m4.dao.AbstractSession import AbstractSession
from m4.dao.FactoryDAO import FactoryDAO
from m4.dao.FactoryScheduleDAO import FactoryScheduleDAO
from m4.dao.BomDAO import BomDAO
from ..dao.InventoryDAO import InventoryDAO
from ..dao.ResourceDAO import ResourceDAO
from ..dao.ProcessDAO import ProcessDAO
from ..dao.BorDAO import BorDAO
from ..dao.RouteDAO import RouteDAO
from ..constraint.ScheduleConstraint import ScheduleConstraint
from m4.process.Router import Router
from ..operator.Inventory import Inventory
from ..operator.Resource import Resource
from ..operator.Process import Process
from m4.operator.Factory import Factory
from m4.process.Item import Item
from ..util.DateTimeUtility import DateTimeUtility

from m4.dao.DemandDAO import DemandDAO


class FactoryBuilder:
    # Demand
    _demand_list: list = []

    # Route 관련
    _routes: list = []  # OK
    _work_order_item_list: list = []    # OK
    _curr_to_next_route_dict: dict = {}   # OK
    _item_to_finished_item_dict: dict = {}     # OK     ****
    _start_location: str = ''
    _end_location: str = ''

    @classmethod
    def build(cls, plan_version_dict: dict, simulation_dict: dict, session: AbstractSession):

        instance: Factory = Factory()

        factory_info, bom, route_master, work_order_master = cls.get_dao_data(session)

        schedule_constraint = cls._init_schedule_constraint(simulation_dict, session)

        inventories = cls._init_inventories(plan_version_dict, simulation_dict, session)

        cls._init_inv_start_end_location(simulation_dict, session)    # 임시

        resources = cls._init_resources(simulation_dict, session)

        processes = cls._init_processes(resources, simulation_dict, session)

        # Work Order 정보 초기화
        work_order_item_list = cls._init_work_orders(work_order_master=work_order_master)

        # Route 관련 정보들 초기화
        next_to_curr_item_dict = cls._create_next_to_curr_item_dict(route_master=route_master)
        item_route_list, item_route_error_list = cls._create_work_order_route(work_order_item_list=work_order_item_list,
                                                                              to_from_item_dict=next_to_curr_item_dict)
        item_to_final_item_dict = cls._create_item_to_finished_item_dict(item_route_list=item_route_list)


        # 공장 내 Route 객체들을 초기화
        _next_to_curr_item_dict = cls._create_next_to_curr_item_dict(route_master=route_master)
        _item_to_final_item_dict = cls._create_route_group(route_master=route_master)
        routes = cls._init_routes(route_master=route_master,
                                  inventories=inventories,
                                  processes=processes)

        # Backward Tick 을 위한 Backward 방향 Router Sequence
        _next_to_curr_item_dict = cls._create_next_to_curr_item_dict(route_master=route_master)
        route_sequence = cls._get_route_sequence(routers=routes)

        # cls._init_routes(route_master=route_master)
        # work_order_master: list = cls._init_work_orders(work_order_master=work_order_master)

        instance.init(info=factory_info,
                      schedule_constraint=schedule_constraint,
                      inventories=inventories,
                      processes=processes,
                      work_order_list=work_order_master,
                      next_to_curr_item_dict=next_to_curr_item_dict,
                      item_to_final_item_dict=item_to_final_item_dict,
                      next_to_curr_location_dict=route_sequence,
                      routes=routes,
                      router_sequence=route_sequence)

        return instance

    @classmethod
    def _init_schedule_constraint(cls, simulation_dict, session: AbstractSession):
        """
        :param simulation_dict: simulation_dict 정보
        :param session: Abstract Session
        :return: ScheduleConstraint
        """
        dao = FactoryScheduleDAO.instance()
        factory_schedule_id = simulation_dict['FACTRY_SCHDL_ID']
        max_priority = dao.select_max_priority(session, factory_schedule_id=factory_schedule_id)['data'][0][0]
        factory_schedule_data = dao.map(dao.select_constraint(session, factory_schedule_id=factory_schedule_id))

        schedule_constraint: ScheduleConstraint = ScheduleConstraint()
        schedule_constraint.init(factory_schedule_data, max_priority)

        return schedule_constraint

    @classmethod
    def _init_inventories(cls, plan_version_dict: dict, simulation_dict: dict, session: AbstractSession):
        """
        :param simulation_dict: simulation_dict 정보
        :param session: Abstract Session
        :return: dict
        """
        # InventoryDAO로 부터 정보 받아오기
        simulation_id = simulation_dict['SIM_ID']
        plan_start_date = DateTimeUtility.convert_str_to_date(plan_version_dict['START_DT_HMS'])
        dao: InventoryDAO = InventoryDAO.instance()
        inventory_data = dao.map(dao.select_route_inventory(session, simulation_id=simulation_id))
        item_dict: dict = dao.hash_map(dao.select_route_item(session, simulation_id=simulation_id), "INV_ID")
        item_constraint_dict: dict = dao.hash_map(dao.select_route_item_constraint(session, simulation_id=simulation_id), "INV_ID")

        inventories: dict = {}
        for inv in inventory_data:
            inventory = Inventory()
            item_constraint_data: list = item_constraint_dict.get(inv['INV_ID'], [])
            # if item_constraint_data is None:
            #     item_constraint_data = []
            inventory.init(inv, item_constraint_data)
            items: list = item_dict.get(inv['INV_ID'], [])
            for info in items:
                item: Item = Item()

                due_date: object = info.get('DUE_DT', None)
                due_date = \
                    DateTimeUtility.convert_str_to_date(due_date) if isinstance(due_date, str) else\
                    due_date if isinstance(due_date, datetime.datetime) else \
                    None

                item.init(work_order_id=info.get('WORK_ORDER_ID', ''),
                          order_item_id=info.get('ORDER_ITEM_ID', ''),
                          item_id=info.get('ITEM_ID', ''),
                          location_id=info.get('LOC_ID', ''),
                          quantity=info.get('QTY', ''),
                          due_date=due_date)
                inventory.put(time_index=0, date=plan_start_date, item=item, move_time=0)

            inventories[inv['INV_ID']] = inventory
        return inventories

    @classmethod
    def _init_inv_start_end_location(cls, simulation_dict, session: AbstractSession):
        """
        :param simulation_dict: simulation_dict 정보
        :param session: Abstract Session
        :return: dict
        """
        simulation_id = simulation_dict['SIM_ID']
        dao: InventoryDAO = InventoryDAO.instance()
        inventory_data = dao.map(dao.select(session))

        for inv in inventory_data:
            if inv['INV_TYP'] == 'PDINV':
                FactoryBuilder._end_location = inv['INV_ID']
            elif inv['INV_TYP'] == 'RMINV':
                FactoryBuilder._start_location = inv['INV_ID']

    @classmethod
    def _init_resources(cls, simulation_dict, session: AbstractSession):
        """
        :param simulation_dict: simulation_dict 정보
        :param session: Abstract Session
        :return: dict
        """
        # ResourceDAO로 부터 정보 받아오기
        simulation_id = simulation_dict['SIM_ID']
        dao: ResourceDAO = ResourceDAO.instance()
        resource_data = dao.map(dao.select_route_resource(session, simulation_id=simulation_id))
        constraint_dict: dict = dao.hash_map(dao.select_route_constraint(session, simulation_id=simulation_id), "RESC_ID")
        constraint_max_priority_dict = dao.hash_map(dao.select_route_constraint_max_priority(session, simulation_id=simulation_id), "RESC_ID")

        resources: dict = {}
        for res in resource_data:
            resource: Resource = Resource()

            constraint_data: list = constraint_dict.get(res['RESC_ID'], [])
            constraint_max_priority_data = constraint_max_priority_dict.get(res['RESC_ID'])
            constraint_max_priority = 0 if constraint_max_priority_data is None else constraint_max_priority_data[0]['PRIORITY']
            resource.init(res, constraint_data, constraint_max_priority)

            resources[res['RESC_ID']] = resource

        return resources

    @classmethod
    def _init_processes(cls, resources: dict, simulation_dict, session: AbstractSession):
        """
        :param resources: resources 객체
        :param simulation_dict: simulation_dict 정보
        :param session: Abstract Session
        :return: dict
        """

        # ProcessDAO로 부터 정보 받아오기
        simulation_id = simulation_dict['SIM_ID']
        dao: ProcessDAO = ProcessDAO.instance()
        process_data = dao.map(dao.select_route_process(session, simulation_id=simulation_id))
        bor_dict: dict = dao.hash_map(dao.select_route_bor(session, simulation_id=simulation_id), "PROC_ID")

        processes: dict = {}
        for proc in process_data:
            print(proc)
            process: Process = Process()
            process.init(proc)
            bor_data: list = bor_dict.get(proc["PROC_ID"], [])
            for bor in bor_data:
                print(bor)
                process.add_process_resource(bor, resources[bor["RESC_ID"]])

            processes[proc["PROC_ID"]] = process

        return processes

    @classmethod
    def _get_route_sequence(cls, routers: list):
        last_routers: list = cls._get_last_router(routers=routers)
        router_sequence: dict = {1: last_routers}
        routers = set(routers).difference(set(last_routers))
        while routers:
            curr_depth: int = max(router_sequence.keys())
            current_routers: list = router_sequence[curr_depth]
            prior_routers: list = [
                router
                for current_router in current_routers
                for router in cls._get_prior_routers(router=current_router, routers=routers)]
            router_sequence[curr_depth + 1] = prior_routers
            routers = routers.difference(set(prior_routers))
        return router_sequence

    @classmethod
    def _get_last_router(cls, routers: list):
        last_routers: list = []
        for obj in routers:
            router: Router = obj
            if not cls._get_next_routers(router=router, routers=routers):
                last_routers.append(obj)
        return last_routers

    @classmethod
    def _get_next_routers(cls, router: Router, routers: list):
        next_routers: list = []
        for obj in routers:
            tmp_router: Router = obj
            if tmp_router.current_route in router.next_route_list:
                next_routers.append(tmp_router)
        return next_routers

    @classmethod
    def _get_prior_routers(cls, router: Router, routers: list):
        prior_routers: list = []
        for obj in routers:
            tmp_router: Router = obj
            if router.current_route in tmp_router.next_route_list:
                prior_routers.append(tmp_router)
        return prior_routers

    # ===================================================== Router =====================================================

    @classmethod
    def _init_work_orders(cls, work_order_master: list) -> list:
        """

        :param work_order_master:
        :return:
        """

        work_order_item_list = cls._create_work_order_item_list(work_order_master=work_order_master)
        return work_order_item_list

    @classmethod
    def _create_work_order_item_list(cls, work_order_master: list):
        work_order_item_list: list = []
        for work_order_item in work_order_master:
            if work_order_item['ORDER_ITEM_ID'] not in work_order_item_list:
                work_order_item_list.append(work_order_item['ORDER_ITEM_ID'])

        work_order_item_list = sorted(work_order_item_list)

        return work_order_item_list

    ############################################################################################
    # Route 관련 Method
    ############################################################################################
    @classmethod
    def _init_routes(cls, route_master: list, inventories: dict, processes: dict) -> list:
        """

        :param route_master:
        :return:
        """
        # Pointer 리스트
        entity_pointers: dict = inventories.copy()
        entity_pointers.update(processes)

        # Location 정보 setting
        route_loc_dict = cls._create_route_loc_list(route_master=route_master)

        # Previous & Next Route Setting
        prev_route_dict, next_route_dict = cls._create_prev_next_route_dict(route_master=route_master,
                                                                            route_loc_list=list(route_loc_dict.keys()),
                                                                            entity_pointers=entity_pointers)

        # Location Type Setting
        route_type_dict = cls._create_route_type_dict(route_master=route_master)

        #
        route_loc_group_dict = cls._create_route_group(route_master=route_master)

        # Route 인스턴스 리스트 세팅
        routes: list = []
        for key, val in route_loc_group_dict.items():
            route_id = route_loc_dict[key]
            route_location = entity_pointers[key]
            curr_to_next_route_dict = cls._create_curr_to_next_route_dict(bom_route_list=val, entity_pointers=entity_pointers)

            previous_route_list = prev_route_dict.get(route_location.id, [])
            next_route_list = next_route_dict.get(route_location.id, [])

            route = Router()
            route.init(route_id=route_id,
                       route_location=route_location,
                       route_type=route_type_dict[route_location.id],
                       previous_route_list=previous_route_list,
                       next_route_list=next_route_list,
                       curr_to_next_route_dict=curr_to_next_route_dict)
            routes.append(route)

        # End Location Route Setting
        route = Router()
        end_location = FactoryBuilder._end_location
        previous_route_list = prev_route_dict.get(end_location, [])
        route.init(route_id=end_location,
                   route_location=entity_pointers[end_location],
                   route_type=route_type_dict[end_location],
                   previous_route_list=previous_route_list,
                   next_route_list=[],
                   curr_to_next_route_dict={})
        routes.append(route)

        return routes

    @classmethod
    def _create_curr_to_next_loc_dict(cls, route_master: list, inventories: dict, processes: dict):
        curr_to_next_loc_dict = {}

        for route in route_master:
            if route['CURR_LOC_ID'] in inventories.keys():
                current_location = inventories[route['CURR_LOC_ID']]
            elif route['CURR_LOC_ID'] in processes.keys():
                current_location = processes[route['CURR_LOC_ID']]
            else:
                raise AssertionError(
                    ""
                )

            if route['NEXT_LOC_ID'] in inventories.keys():
                next_location = inventories[route['NEXT_LOC_ID']]
            elif route['NEXT_LOC_ID'] in processes.keys():
                next_location = processes[route['NEXT_LOC_ID']]
            else:
                raise AssertionError(
                    ""
                )

            if next_location not in curr_to_next_loc_dict.keys():
                curr_to_next_loc_dict.update({next_location: [current_location]})
            else:
                temp_list = curr_to_next_loc_dict[next_location]
                if current_location not in temp_list:
                    temp_list.append(current_location)
                curr_to_next_loc_dict.update({next_location: temp_list})

        return curr_to_next_loc_dict

    @classmethod
    def _create_next_to_curr_item_dict(cls, route_master: list) -> dict:
        """
        각 제품의 To From 정보를 Dictionay 형태로 만드는 처리
        :param route_master: Route Master Data
        :return: None
        """
        to_from_item_dict: dict = {}
        for route in route_master:
            if (route['NEXT_ITEM_ID'] not in to_from_item_dict.keys()) and (route['NEXT_ITEM_ID'] != route['ITEM_ID']):
                to_from_item_dict.update({route['NEXT_ITEM_ID']: route['ITEM_ID']})
        return to_from_item_dict

    @classmethod
    def _create_work_order_route(cls, work_order_item_list: list, to_from_item_dict: dict):

        item_route_list = []
        item_route_error_list = []

        for work_order_item in work_order_item_list:
            work_order_route = [work_order_item]
            while "311110000000" not in work_order_route[-1]:   # 311110000000: RM ITEM_ID (hard coding)
                if work_order_route[-1] in to_from_item_dict.keys():
                    work_order_route.append(to_from_item_dict[work_order_route[-1]])
                else:
                    item_route_error_list.append(work_order_route)
                    break
            item_route_list.append(work_order_route)

        return item_route_list, item_route_error_list

    @classmethod
    def _create_item_to_finished_item_dict(cls, item_route_list: list):
        """
        반제품 item id ~ final item id에 대한 Dictionary 생성
        :param item_route_list: 정상적인 item route 정보
        :return: None
        """
        item_to_final_item_dict: dict = {}

        for item_route in item_route_list:
            for item in item_route[1:]:
                if item not in item_to_final_item_dict.keys():
                    item_to_final_item_dict.update({item: item_route[0]})
        return item_to_final_item_dict

    @classmethod
    def _create_route_type_dict(cls, route_master: list):
        route_type_dict = {}

        for route in route_master:
            if route['CURR_LOC_ID'] not in route_type_dict:
                route_type_dict.update({route['CURR_LOC_ID']: route['CURR_LOC_ID_TYP']})
            if route['NEXT_LOC_ID'] not in route_type_dict:
                route_type_dict.update({route['NEXT_LOC_ID']: route['NEXT_LOC_ID_TYP']})

        return route_type_dict

    @classmethod
    def _create_route_group(cls, route_master: list):
        route_loc_group_dict: dict = {}

        for route in route_master:
            if route['CURR_LOC_ID'] not in route_loc_group_dict.keys():
                route_loc_group_dict.update({route['CURR_LOC_ID']: [route]})
            else:
                temp_list = route_loc_group_dict[route['CURR_LOC_ID']]
                temp_list.append(route)
                route_loc_group_dict[route['CURR_LOC_ID']] = temp_list

        return route_loc_group_dict

    @classmethod
    def _create_curr_to_next_route_dict(cls, bom_route_list: list, entity_pointers: dict):
        """

        :param bom_route_list:
        :return:
        """
        # curr_to_next_route_dict = {}
        # for route in bom_route_list:
        #     next_entity: object = route['NEXT_LOC_ID']
        #     if route['NEXT_LOC_ID'] in entity_pointers.keys():
        #         next_entity = entity_pointers[route['NEXT_LOC_ID']]
        #     curr_to_next_route_dict.update({route['ITEM_ID']: (route['NEXT_ITEM_ID'], next_entity)})
        #

        curr_to_next_route_dict = {}
        for route in bom_route_list:
            if route['ITEM_ID'] not in curr_to_next_route_dict.keys():
                value = (route['NEXT_ITEM_ID'], entity_pointers[route['NEXT_LOC_ID']])
                curr_to_next_route_dict.update({route['ITEM_ID']: [value]})
            else:
                temp_list = curr_to_next_route_dict[route['ITEM_ID']]
                value = (route['NEXT_ITEM_ID'], entity_pointers[route['NEXT_LOC_ID']])
                temp_list.append(value)
                curr_to_next_route_dict.update({route['ITEM_ID']: temp_list})

        return curr_to_next_route_dict

    @classmethod
    def _create_route_loc_list(cls, route_master: list):
        """

        :param route_master:
        :return: location_route
        """
        to_from_location_dict = {}
        for route in route_master:
            if route['NEXT_LOC_ID'] not in to_from_location_dict.keys():
                to_from_location_dict.update({route['NEXT_LOC_ID']: route['CURR_LOC_ID']})

        location_route = ['SALES']  # 마지막 Route (Hard Coding)
        while location_route[-1] != 'RM':   # Location Start Route (Hard Coding)
            if location_route[-1] in to_from_location_dict.keys():
                location_route.append(to_from_location_dict[location_route[-1]])

        route_naming_dict = {}
        idx = 0
        for location in location_route:
            route_naming_dict.update({location: 'ROUTE' + str(len(location_route) - idx)})
            idx += 1

        return route_naming_dict

    @classmethod
    def _create_prev_next_route_dict(cls, route_master: list, route_loc_list: list, entity_pointers: dict):
        prev_route_dict = {}
        next_route_dict = {}
        for route_loc in route_loc_list:
            for route in route_master:
                # Check Previous Route
                if route_loc == route['NEXT_LOC_ID']:
                    if route_loc not in prev_route_dict.keys():
                        value = entity_pointers[route['CURR_LOC_ID']]
                        prev_route_dict.update({route_loc: [value]})
                    else:
                        temp_list = prev_route_dict[route_loc]
                        if entity_pointers[route['CURR_LOC_ID']] not in temp_list:
                            temp_list.append(entity_pointers[route['CURR_LOC_ID']])
                # Check Next Route
                if route_loc == route['CURR_LOC_ID']:
                    if route_loc not in next_route_dict.keys():
                        value = entity_pointers[route['NEXT_LOC_ID']]
                        next_route_dict.update({route_loc: [value]})
                    else:
                        temp_list = next_route_dict[route_loc]
                        if entity_pointers[route['NEXT_LOC_ID']] not in temp_list:
                            temp_list.append(entity_pointers[route['NEXT_LOC_ID']])

        return prev_route_dict, next_route_dict

    # =================================================================================================================

    @classmethod
    def get_dao_data(cls, session: AbstractSession):

        factory_dao: FactoryDAO = FactoryDAO.instance()
        factory_info = factory_dao.map(factory_dao.select_one(session=session))[0]

        bom_dao: BomDAO = BomDAO.instance()
        bom = bom_dao.map(bom_dao.select_bom_routing(session=session))

        # RouteDAO로 부터 정보 받아오기
        route_dao: RouteDAO = RouteDAO.instance()
        route_master = route_dao.map(route_dao.select_master(session=session))

        # DemandDAO로 부터 정보 받아오기
        demand_dao: DemandDAO = DemandDAO.instance()
        work_order_master = demand_dao.map(demand_dao.select_master(session=session))

        return factory_info, bom, route_master, work_order_master


    # @classmethod
    # def _get_router_sequence(cls, routers: list, inventories: dict, to_from_location_dict: dict):
    #     """
    #
    #     :return:
    #     """
    #     router_sequence: dict = dict()
    #     last_operators: list = cls._get_last_operators(inventories=inventories)
    #     prior_operators: list = [
    #         prior_operator
    #         for last_operator in last_operators
    #         for prior_operator in to_from_location_dict[last_operator]
    #     ]
    #     depth: int = 0
    #     while len(prior_operators) > 0:
    #         depth += 1
    #         tmp_routers: list = [router for router in routers if router.route_location in prior_operators]
    #         router_sequence[depth] = tmp_routers
    #
    #         tmp_prior_operators: list = []
    #         for last_operator in prior_operators:
    #             if last_operator not in to_from_location_dict.keys():
    #                 continue
    #             for prior_operator in to_from_location_dict[last_operator]:
    #                 tmp_prior_operators.append(prior_operator)
    #         prior_operators = tmp_prior_operators.copy()
    #
    #     return router_sequence
