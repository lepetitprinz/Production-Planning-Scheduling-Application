import datetime

from m4.constraint.AbstractConstraint import AbstractConstraint
from m4.constraint.TimeConstraintDay import TimeConstraintDay
from m4.constraint.TimeConstraintDaily import TimeConstraintDaily
from m4.constraint.TimeConstraintWeekly import TimeConstraintWeekly
from m4.constraint.TimeConstraintMonthly import TimeConstraintMonthly


class ScheduleConstraint(AbstractConstraint):
    """
    Schedule Constraint Object
    Schedule Constraint (비가용 계획) 정보 클래스
    Schedule Constraint 처리 관련 속성 및 동작들이 정의됨
    """
    PRD_TYP: dict = {
        'DAY': TimeConstraintDay,
        'DAILY': TimeConstraintDaily,
        'WEEKLY': TimeConstraintWeekly,
        'MONLY': TimeConstraintMonthly
    }

    def __init__(self):
        """
        Schedule Constraint 생성자
        """
        super().__init__("SCHDL", "Schedule Constraint", "SCHDL_CONST")

        # time constraints - priority 별로 저장
        self._time_constraints: list = []

    def init(self, schedule_data: list, max_priority: int):
        if max_priority > 0:
            # schedule constraint 배열에 priority별로 설정
            self._time_constraints = [[] for i in range(max_priority + 1)]

            for info in schedule_data:
                self._time_constraints[info['PRIORITY']].append(self._create_time_constraint(info))

    @staticmethod
    def _create_time_constraint(info: dict):
        constraint = ScheduleConstraint.PRD_TYP[info['PRD_TYP']]()
        constraint.init(info)
        return constraint

    def check(self, date: datetime.datetime):

        for time_constraints in self._time_constraints:
            for const in time_constraints:
                ret: AbstractConstraint = const.check(date)
                if ret is not None:
                    return ret
        return None
