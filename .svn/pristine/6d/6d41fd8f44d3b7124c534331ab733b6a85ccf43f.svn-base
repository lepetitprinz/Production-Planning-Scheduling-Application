import datetime
from math import floor

# from m4.backward.BackwardManager import BackwardManager
from m4.backward.BackwardStepPlan import BackwardStepPlan


class BackwardWorkOrder(object):

    def __init__(self):
        # self.backwardManager: BackwardManager = None
        self.work_order_id: str = ''
        self.finished_item_id: str = ''
        self.location_id: str = ''
        self.work_order_qty: int = 0
        self.priority: int = 1
        self.dtl_priority: int = 1

        self.due_date: str = ''
        self.item_route_chain_dict: dict = {}
        self.remain_production_qty: int = 0

    def init(self, work_order: dict, item_route_chain_dict: dict):
        """

        :return:
        """
        # self.backwardManager = backward_Manager
        self.work_order_id = work_order['WORK_ORDER_ID']
        self.finished_item_id = work_order['ORDER_ITEM_ID']
        self.location_id = 'SALES'      # Hard Coding
        # self.location_id = self._get_end_location()
        self.work_order_qty = work_order['ORDER_QTY']
        self.priority = work_order['PRIORITY']
        self.dtl_priority = work_order['DTL_PRIORITY']
        self.due_date = work_order['DUE_DT']

        self.item_route_chain_dict = item_route_chain_dict

    def process(self, peg_available_item_dict: dict, backward_step_plan_by_loc: dict, peg_result_dict: dict):
        """

        :return:
        """
        self.backward_step_plan_list = self._create_backward_step_plan_list(peg_available_item_dict=peg_available_item_dict,
                                                                            backward_step_plan_by_loc=backward_step_plan_by_loc,
                                                                            peg_result_dict=peg_result_dict)

        return self.backward_step_plan_list

    def _create_backward_step_plan_list(self,
                                        peg_available_item_dict: dict,
                                        backward_step_plan_by_loc: dict,
                                        peg_result_dict: dict):
        """

        :param inventory_item_list:
        :param wip_list:
        :return:
        """
        after_peg_item_dict = peg_available_item_dict
        # Backward Process 초기 setting
        backward_step_plan_list = []
        step = 1
        curr_loc_id = self.location_id
        curr_item_id = self.finished_item_id
        self.remain_production_qty = self.work_order_qty

        # Set End Location Step
        plan: BackwardStepPlan = BackwardStepPlan()
        plan.init(work_order_id=self.work_order_id,
                  finished_item_id=self.finished_item_id,
                  work_order_qty=self.work_order_qty,
                  remain_production_qty=self.remain_production_qty,
                  step=step,
                  location_id=curr_loc_id,
                  item_id=curr_item_id,
                  due_date=self.due_date
                  )

        backward_step_plan_list.append(plan)

        self._set_backward_step_plan_by_loc(plan=plan, backward_step_plan_by_loc=backward_step_plan_by_loc)

        for i in range(len(self.item_route_chain_dict)):
            plan: BackwardStepPlan = BackwardStepPlan()
            step += 1
            (curr_loc_id, curr_item_id) = self.item_route_chain_dict[(curr_loc_id, curr_item_id)]

            # Location 및 Item 정보 setting
            plan.init(work_order_id=self.work_order_id,
                      finished_item_id=self.finished_item_id,
                      work_order_qty=self.work_order_qty,
                      remain_production_qty=self.remain_production_qty,
                      step=step,
                      location_id=curr_loc_id,
                      item_id=curr_item_id,
                      due_date=self.due_date)

            # Pegging
            if self.remain_production_qty > 0:
                peg_qty, after_peg_item_dict = self._pegging(location_id=curr_loc_id,
                                                             item_id=curr_item_id,
                                                             peg_available_item_dict=after_peg_item_dict,
                                                             peg_result_dict=peg_result_dict)

                # Update Pegging
                plan.peg(peg_qty=peg_qty)

            backward_step_plan_list.append(plan)
            self._set_backward_step_plan_by_loc(plan=plan, backward_step_plan_by_loc=backward_step_plan_by_loc)

        return backward_step_plan_list

    def _pegging(self, location_id: str, item_id: str, peg_available_item_dict: dict, peg_result_dict: dict):
        peg_qty = 0
        key = (location_id, item_id)
        peg_available_item_list = peg_available_item_dict.get(key, [])
        peg_result_item_list = peg_result_dict.get(key, [])

        if peg_available_item_list != []:
            for peg_available_item, peg_result_item in zip(peg_available_item_list, peg_result_item_list):
                if self.remain_production_qty >= peg_available_item['STOCK_QTY']:
                    self.remain_production_qty -= peg_available_item['STOCK_QTY']
                    peg_qty += peg_available_item['STOCK_QTY']

                    peg_result_item['WORK_ORDER_ID'] = self.work_order_id
                    peg_result_item['ORDER_ITEM_ID'] = self.finished_item_id
                    peg_available_item['STOCK_QTY'] = 0
                    # peg_available_item_list.remove(peg_available_item)

                else:
                    peg_qty += self.remain_production_qty
                    peg_result_item['WORK_ORDER_ID'] = self.work_order_id
                    peg_result_item['ORDER_ITEM_ID'] = self.finished_item_id
                    peg_available_item['STOCK_QTY'] = round(peg_available_item['STOCK_QTY']- self.remain_production_qty, 3)     # 자리수 Hard Coding
                    self.remain_production_qty = 0

        else:
            return peg_qty, peg_available_item_dict

        return peg_qty, peg_available_item_dict

    def _set_backward_step_plan_by_loc(self, plan: BackwardStepPlan, backward_step_plan_by_loc: dict):

        if plan.location_id not in backward_step_plan_by_loc.keys():
            backward_step_plan_by_loc.update({plan.location_id: [plan]})
        else:
            temp_list = backward_step_plan_by_loc[plan.location_id]
            temp_list.append(plan)
            backward_step_plan_by_loc.update({plan.location_id: temp_list})

    def _get_end_location(self):
        end_location = ''

        return end_location
