import datetime

from m4.manager.AbstractDuration import AbstractDuration
from m4.util.TimeUtility import TimeUtility


class DurationDaily(AbstractDuration):
    """
    Machine Transfer Object
    Initial 과 End 사이 시점에서 Lot 을 Machine 으로 보내는 이벤트를 담당
    """

    # Static 변수들
    staticVar2: object = None           # Comment

    # Static Constants
    CONSTANT_VARIABLE2: object = None   # Comment

    def __init__(self):
        """
        생성자 :
        """

        # 1. AbstractProcess 클래스에 정의된 멤버 변수들을 상속
        super().__init__()

        # 2-1. Public
        self.memberVar1: object = None

        # 2-2. Private
        self._sequence: list = []

    def clip_duration(self, from_date: datetime.datetime, to_date: datetime.datetime):
        pass

    def get_current_duration(self):
        pass

    def set_time(self, start_date: object, end_date: object):

        #
        start_date = TimeUtility.check_date_info(date_info=start_date)
        end_date = TimeUtility.check_date_info(date_info=end_date)

        # 시작 시간이 종료 시간 이전인지 검사
        is_it_correct: bool = TimeUtility.check_from_to(start_date=start_date, end_date=end_date, equal_flag=False)
        if not is_it_correct:
            raise AssertionError(
                f"{start_date} < {end_date} : {is_it_correct}"
            )
