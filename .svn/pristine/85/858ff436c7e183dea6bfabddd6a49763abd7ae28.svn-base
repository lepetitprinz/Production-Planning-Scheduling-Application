import datetime

class BackwardStepPlan(object):

    def __init__(self):
        self.work_order_id:str = ''
        self.finished_item_id: str = ''
        self.item_id: str = ''
        self.step: int = 0
        self.plant_id: str = ''
        self.location_id: str = ''
        self.work_order_qty: int = 0
        self.due_date: str = ''

        self.peg_qty: int = 0
        self.remain_production_qty: int = 0
        # self.peg_item_list: list = []

    def init(self,
             work_order_id: str,
             finished_item_id: str,
             work_order_qty: int,
             remain_production_qty: int,
             step: int,
             item_id: str,
             location_id: str,
             due_date: str):

        self.work_order_id = work_order_id
        self.finished_item_id = finished_item_id
        self.item_id = item_id
        self.step = step
        self.location_id = location_id
        self.work_order_qty = work_order_qty
        self.remain_production_qty = remain_production_qty
        self.due_date = due_date

    def peg(self, peg_qty: int):
        self.peg_qty = peg_qty
        self.remain_production_qty -= peg_qty