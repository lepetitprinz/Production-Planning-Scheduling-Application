import datetime

from m4.manager.AbstractDuration import AbstractDuration
from m4.util.TimeUtility import TimeUtility


class DurationOnce(AbstractDuration):
    """
    Duration Once Object
    일회성 Duration 정보 처리 구현을 위한 클래스
    """

    # Static 변수들
    staticVar2: object = None  # Comment

    # Static Constants
    CONSTANT_VARIABLE2: object = None  # Comment

    def __init__(self):
        """
        생성자 :
        """

        # 1. AbstractDuration 클래스에 정의된 멤버 변수들을 상속
        super().__init__()

        # 2-1. Public
        self.memberVar1: object = None

        # 2-2. Private
        self._sequence: list = []

    def rebuild_duration(self):
        pass

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

        # (start_date, end_date) 튜플을 ._sequence 리스트에 추가
        self._sequence.append((start_date, end_date))

        # ._sequence 리스트 재정렬
        self._sequence.sort()
