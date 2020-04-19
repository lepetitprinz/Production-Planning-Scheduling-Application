import datetime

from m4.constraint.AbstractConstraint import AbstractConstraint


class TimeConstraintMonthly(AbstractConstraint):
    """
    Time Constraint Monthly
    """
    def __init__(self):
        """
        생성자 :
        """
        super().__init__("", "", "DAILY_CONST")

        self._start_date: datetime.datetime = None
        self._end_date: datetime.datetime = None
        self._factory_schedule_id: str = None
        self._priority: int = -1
        self._time_constraint_id: str = None
        self._time_constraint_name: str = None
        self._time_constraint_type: str = None
        self._time_constraint_period_type: str = None
        self._lower_bound: datetime.timedelta = None
        self._upper_bound: datetime.timedelta = None

    def init(self, info: dict):
        super()._id: str = info['TM_CONST_ID']
        super()._name: str = info['TM_CONST_NM']

        self._start_date: datetime.datetime = info['START_DATE']
        self._end_date: datetime.datetime = info['END_DATE']
        self._factory_schedule_id: str = info['SCHDL_ID']
        self._priority: int = info['PRIORITY']
        self._time_constraint_type: str = info['TM_CONST_TYP']
        self._time_constraint_period_type: str = info['PRD_TYP']
        date = info['LOWER_BOUND']
        self._lower_bound: datetime.timedelta = datetime.timedelta(days=date.day, hours=date.hour, minutes=date.minute, seconds=date.second)
        date = info['UPPER_BOUND']
        self._upper_bound: datetime.timedelta = datetime.timedelta(days=date.day, hours=date.hour, minutes=date.minute, seconds=date.second)

    def check(self, date: datetime.datetime):
        if self._start_date <= date < self._end_date:
            timedelta = datetime.timedelta(days=date.day, hours=date.hour, minutes=date.minute, seconds=date.second)
            if self._lower_bound <= timedelta < self._upper_bound:
                return self
        return None

    def get_factory_schedule_id(self):
        return self._factory_schedule_id

    def get_priority(self):
        return self._priority

    def get_time_constraint_type(self):
        return self._time_constraint_type

    def get_time_constraint_period_type(self):
        return self._time_constraint_period_type
