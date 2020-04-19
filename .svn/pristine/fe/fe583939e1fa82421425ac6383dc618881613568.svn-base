
import datetime

from m4.common.SingletonInstance import SingletonInstance
from ..constraint.AbstractConstraint import AbstractConstraint
from ..constraint.ScheduleConstraint import ScheduleConstraint
from ..backward.BackwardStepPlan import BackwardStepPlan
from m4.operator.Factory import Factory


class FactoryManager(SingletonInstance):

    def __init__(self):
        self._factory: Factory = None
        self._optimizer: object = None
        self._work_order: object = None

    def init(self, factory: Factory):
        self._factory = factory

    def set_backward_plan(self, orders: dict):
        self._factory.set_backward_plan(orders=orders)

    def run_factory(self, run_time: dict):
        """

        :param run_time:
        :return:
        """
        factory_time_constraint: object = self._factory.get_time_constraints(run_time=run_time)

        if factory_time_constraint is None:
            print(f"\t\t시간 제약 없음")
            self._factory.run(run_time=run_time)

        elif factory_time_constraint == run_time:
            print(f"\t\t달력 시간 제약 : "
                  f"{run_time['is_off_day']} / {run_time['constraint_name']} / {run_time['constraint_type']}")
            self._factory.run(run_time=run_time)

        elif isinstance(factory_time_constraint, AbstractConstraint):
            print(f"\t\t{factory_time_constraint}")
            self._factory.run(run_time=run_time, time_constraint=factory_time_constraint)
