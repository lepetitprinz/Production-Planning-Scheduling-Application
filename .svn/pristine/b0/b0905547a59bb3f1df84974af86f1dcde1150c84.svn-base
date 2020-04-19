import datetime

from m4.constraint.ScheduleConstraint import ScheduleConstraint


class Resource(object):
    """
    Resource Object
    각 공정 단계 별 생산 장비를 구현한 클래스
    Process 에 종속되며
    Route 로부터 자신이 속한 Process 에 작업이 할당되었을 경우
    실제 처리 동작을 수행하도록 설계
    """
    STATUS_IDLE: str = "IDLE"
    STATUS_PROCESSING: str = "PROC"
    STATUS_DOWN: str = "DOWN"

    def __init__(self):
        """
        생성자 :
        """

        # 2-1. Public
        self.id: str = ""                               # Resource ID
        self.name: str = ""                             # Resource 명칭
        self.plant_id: str = ""                         # Plant ID

        # 2-2. Private
        self._status: str = Resource.STATUS_IDLE        # Resource 의 현재 상태. PROC / IDLE / DOWN
        self._constraints: ScheduleConstraint = None

    def init(self, info: dict, schedule_data: list, max_priority: int):
        """

        :param info:
        :return:
        """
        self.id = info['RESC_ID']
        self.name = info['RESC_NM']
        self.plant_id = info['PLANT_ID']

        self._constraints: ScheduleConstraint = ScheduleConstraint()
        self._constraints.init(schedule_data, max_priority)

    def check(self, date: datetime.datetime):
        """

        :return:
        """
        return self._constraints.check(date)

    def get_status(self):
        return self._status

    def set_status(self, status: str):
        self._status = status
