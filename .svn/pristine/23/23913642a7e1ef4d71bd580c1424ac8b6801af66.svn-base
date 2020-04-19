import copy

from m4.common.SingletonInstance import SingletonInstance
from m4.backward.BackwardWorkOrder import BackwardWorkOrder


class BackwardManager(SingletonInstance):
    def __init__(self):
        # Master Data
        self._work_order_list: list = []
        self.route_list: list = []
        self.inventory_item_list: list = []
        self.wip_list: list = []

        self._production_order_list: list = []

        self._work_order_item_list: list = []
        self._work_order_route_dict: dict = {}
        self._to_from_item_dict: dict = {}
        self._route_to_from_dict: dict = {}
        self._work_order_route_chain_dict: dict = {}
        self.peg_available_item_dict: dict = {}
        self.peg_result_dict: dict = {}

        # Item + 위치 별 재공/재공 item list
        self.stock_wip_by_loc_dict: dict = {}
        self.backward_step_plan_result: list = []
        self.backward_step_plan_by_loc: dict = {}

    def init(self,
             work_order_list: list,
             route_list: list,
             inventory_item_list: list,
             wip_list: list):

        # DB로 부터 받은 데이터 Setting
        self._work_order_list = work_order_list
        self.route_list = route_list
        self.inventory_item_list = inventory_item_list
        self.wip_list = wip_list

        self._production_order_list = self._create_production_order_list()

        # Backward Process에서 필요한 정보 생성
        self._work_order_item_list = self._create_work_order_item_list()
        self._route_to_from_dict = self._create_route_to_from_dict()
        self._to_from_item_dict = self._create_to_from_item_dict()
        self._work_order_route_chain_dict = self._create_work_order_route_chain_dict()
        peg_available_item_dict = self._create_peg_available_item_dict(inventory_item_list=inventory_item_list,
                                                                       wip_list=wip_list)
        self.peg_available_item_dict = peg_available_item_dict
        self.peg_result_dict = copy.deepcopy(peg_available_item_dict)
        # self._work_order_route_dict = self._create_work_order_route_dict()

    def run(self):
        """

        :return:
        """
        # 각 Work Order 별로 Backward Plan 계산
        for production_order in self._production_order_list:
            backward_work_order = BackwardWorkOrder()
            item_route_chain_dict = self._work_order_route_chain_dict[production_order['ORDER_ITEM_ID']]
            backward_work_order.init(work_order=production_order,
                                     item_route_chain_dict=item_route_chain_dict)
            backward_step_plan_list = backward_work_order.process(peg_available_item_dict=self.peg_available_item_dict,
                                                                  backward_step_plan_by_loc=self.backward_step_plan_by_loc,
                                                                  peg_result_dict=self.peg_result_dict)
            self.backward_step_plan_result.append(backward_step_plan_list)

        return self.backward_step_plan_result, self.backward_step_plan_by_loc, self.peg_result_dict

    def _create_work_order_item_list(self):
        """

        :return work_order_item_list:
        """
        work_order_item_list = []

        for work_order in self._work_order_list:
            if work_order['ORDER_ITEM_ID'] not in work_order_item_list:
                work_order_item_list.append(work_order['ORDER_ITEM_ID'])

        return work_order_item_list

    def _create_production_order_list(self):
        """

        :return production_order_list:
        """
        work_order_list = self._work_order_list.copy()
        production_order_list = sorted(work_order_list, key=lambda x: (x['PRIORITY'], x['DTL_PRIORITY']))

        return production_order_list

    def _create_to_from_item_dict(self):
        """

        :return to_from_item_dict:
        """
        to_from_item_dict = {}

        for route in self.route_list:
            if (route['NEXT_ITEM_ID'] not in to_from_item_dict.keys()) and (route['NEXT_ITEM_ID'] != route['ITEM_ID']):
                to_from_item_dict.update({route['NEXT_ITEM_ID']: route['ITEM_ID']})

        return to_from_item_dict

    def _create_work_order_route_dict(self):
        """

        :return work_order_route_dict:
        """
        work_order_route_dict = {}

        for work_order_item in self._work_order_item_list:
            work_order_route = [work_order_item]
            while "311110000000" not in work_order_route[-1]:  # 311110000000: RM ITEM_ID (hard coding)
                if work_order_route[-1] in self._to_from_item_dict.keys():
                    work_order_route.append(self._to_from_item_dict[work_order_route[-1]])
                else:
                    break
            work_order_route_dict.update({work_order_route[0]: work_order_route})

        return work_order_route_dict

    def _create_route_to_from_dict(self):
        """

        :return route_to_from_dict:
        """
        route_to_from_dict = {}

        for route in self.route_list:
            if (route['NEXT_LOC_ID'], route['NEXT_ITEM_ID']) not in route_to_from_dict.keys():
                route_to_from_dict.update({(route['NEXT_LOC_ID'], route['NEXT_ITEM_ID']): (route['CURR_LOC_ID'], route['ITEM_ID'])})

        return route_to_from_dict

    def _create_work_order_route_chain_dict(self):
        """

        :return work_order_route_chain_dict:
        """
        work_order_route_chain_dict = {}
        end_location = 'SALES'  # hard coding

        for work_order in self._work_order_list:
            route_chain_list = []
            key = (end_location, work_order['ORDER_ITEM_ID'])
            value = self._route_to_from_dict.get(key)
            route_chain_list.append([key, value])

            while route_chain_list[-1][1][0] != 'RM':
                key = route_chain_list[-1][1]
                value = self._route_to_from_dict.get(key)
                if value != None:
                    route_chain_list.append([key, value])
                else:
                    print('Route 누락')
                    break

            route_chain_dict = {}
            for route_chain in route_chain_list:
                route_chain_dict.update({route_chain[0]: route_chain[1]})

            work_order_route_chain_dict.update({work_order['ORDER_ITEM_ID']: route_chain_dict})

        return work_order_route_chain_dict

    def _create_peg_available_item_dict(self, inventory_item_list: list, wip_list: list):
        peg_available_item_dict = {}

        for inventory_item in inventory_item_list:
            key = (inventory_item['INV_ID'], inventory_item['ITEM_ID'])
            if key not in peg_available_item_dict.keys():
                peg_available_item_dict.update({key: [inventory_item]})
            else:
                temp_list = peg_available_item_dict[key]
                temp_list.append(inventory_item)
                peg_available_item_dict.update({key, temp_list})

        for wip_item in wip_list:
            key = (wip_item['PROC_ID'], wip_item['ITEM_ID'])
            if key not in peg_available_item_dict.keys():
                peg_available_item_dict.update({key: [wip_item]})
            else:
                temp_list = peg_available_item_dict[key]
                temp_list.append(wip_item)
                peg_available_item_dict.update({key, temp_list})

        return peg_available_item_dict
