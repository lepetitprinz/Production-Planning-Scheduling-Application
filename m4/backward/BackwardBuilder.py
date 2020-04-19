from m4.dao.AbstractSession import AbstractSession
from m4.dao.DemandDAO import DemandDAO
from m4.dao.RouteDAO import RouteDAO
from m4.dao.InventoryItemDAO import InventoryItemDAO
from m4.dao.WorkInProgressDAO import WorkInProgressDAO
from m4.dao.ProcessDAO import ProcessDAO

class BackwardBuilder:

    @classmethod
    def build(cls, plan_version_dict: dict, simulation_dict: dict, session: AbstractSession):
        return cls._get_dao_data(simulation_dict=simulation_dict, session=session)

    @classmethod
    def create_time_dict(cls, route_list: list, bor_list: list):
        setup_time_dict = cls._create_setup_time_dict(bor_list=bor_list)
        proc_time_dict = cls._create_proc_time_dict(bor_list=bor_list)
        move_time_dict = cls._create_move_time_dict(route_list=route_list)

        return setup_time_dict, proc_time_dict, move_time_dict

    @classmethod
    def _get_dao_data(cls, simulation_dict: dict, session: AbstractSession):
        simulation_id = simulation_dict['SIM_ID']

        # DemandDAO로 부터 정보 받아오기
        demand_dao: DemandDAO = DemandDAO.instance()
        work_order_master = demand_dao.map(demand_dao.select_master(session=session))

        # RouteDAO로 부터 정보 받아오기
        route_dao: RouteDAO = RouteDAO.instance()
        route_master = route_dao.map(route_dao.select_master(session=session))

        # InventoryItemDAO로 부터 정보 받아오기
        inventory_item_dao: InventoryItemDAO = InventoryItemDAO()
        inventory_item_master = inventory_item_dao.map(inventory_item_dao.select_master(session=session))

        # WorkInProgressDAO로 부터 정보 받아오기
        wip_dao: WorkInProgressDAO = WorkInProgressDAO()
        wip_master = wip_dao.map(wip_dao.select_master(simulation_id=simulation_id, session=session))

        # ProcessDAO로 부터 정보 받아오기
        bor_dao: ProcessDAO = ProcessDAO()
        bor_master = bor_dao.map(bor_dao.select_route_bor(session=session))

        return work_order_master, route_master, inventory_item_master, wip_master, bor_master

    @classmethod
    def _create_setup_time_dict(cls, bor_list: list):
        setup_time_dict = {}
        for bor in bor_list:
            key = (bor['PROC_ID'], bor['RESC_ID'])
            value = bor['PRE_PROC_SETUP_TM']
            setup_time_dict.update({key: value})

        return setup_time_dict

    @classmethod
    def _create_proc_time_dict(cls, bor_list: list):
        proc_time_dict = {}
        for bor in bor_list:
            key = (bor['PROC_ID'], bor['RESC_ID'])
            value = bor['PROC_TM']
            proc_time_dict.update({key: value})

        return proc_time_dict

    @classmethod
    def _create_move_time_dict(cls, route_list: list):
        move_time_dict = {}
        for route in route_list:
            key = (route['CURR_LOC_ID'], route['NEXT_LOC_ID'])
            if key not in move_time_dict.keys():
                move_time_dict.update({key: route['MOVE_TM']})

        return move_time_dict