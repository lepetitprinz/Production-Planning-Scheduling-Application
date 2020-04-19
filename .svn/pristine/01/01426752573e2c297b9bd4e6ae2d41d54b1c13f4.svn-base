from m4.dao.AbstractSession import AbstractSession
from m4.dao.DemandDAO import DemandDAO
from m4.dao.RouteDAO import RouteDAO
from m4.dao.InventoryItemDAO import InventoryItemDAO
from m4.dao.WorkInProgressDAO import WorkInProgressDAO


class BackwardBuilder:

    @classmethod
    def get_dao_data(cls, simulation_dict: dict, session: AbstractSession):
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

        return work_order_master, route_master, inventory_item_master, wip_master

    @classmethod
    def build(cls, plan_version_dict: dict, simulation_dict: dict, session: AbstractSession):

        work_order_master, route_master, inventory_item_master, wip_master = \
            cls.get_dao_data(simulation_dict=simulation_dict, session=session)

        return work_order_master, route_master, inventory_item_master, wip_master
