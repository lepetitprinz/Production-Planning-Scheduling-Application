
import os
import math
import datetime
import unittest

from m4.manager.ScheduleManager import ScheduleManager
from m4.util.TimeUtility import TimeUtility


class ScheduleManagerTestCase(unittest.TestCase):
    def setUp(self) -> None:

        # 테스트용 Calendar 인스턴스 생성
        self.scheduleManager: ScheduleManager = ScheduleManager()

    def test_uom_timedelta(self):
        """
        시간 길이 단위 파라메터 테스트
        :return: void
        """

        print("\n시간 길이 UOM 단위 반영 테스트")

        ten_hours_delta: datetime.timedelta = TimeUtility.derive_timedelta(time_length=10, uom="hours")
        print(f"{10} {'hours'} = {type(ten_hours_delta)} : {ten_hours_delta}")

        one_week_delta: datetime.timedelta = TimeUtility.derive_timedelta(time_length=1, uom="weeks")
        print(f"{1} {'weeks'} = {type(one_week_delta)} : {one_week_delta}")

        one_microsec_delta: datetime.timedelta = TimeUtility.derive_timedelta(time_length=1, uom="microseconds")
        print(f"{1} {'microseconds'} = {type(one_microsec_delta)} : {one_microsec_delta}")

    def test_setup_with_datetime(self):
        """
        start_date 파라메터를 datetime 형식으로 넘겨 줄 경우에 대한 테스트
        :return: void
        """

        print(f"\nTest Setup with datetime")

        # start_date 및 end_date 가 datetime 인스턴스로 넘어올 경우를 상정
        start_date: datetime.datetime = datetime.datetime(year=2020, month=3, day=23)
        end_date: datetime.datetime = datetime.datetime(year=2020, month=3, day=30)

        timestep_length: int = 1
        timestep_uom: str = "days"

        # start_date 파라메터가 datetime 인스턴스로 넘어올 경우 별도의 처리 없이 진행되도록 설계
        self.scheduleManager.init(start_date=start_date, end_date=end_date,
                                  time_step_length=timestep_length, time_step_uom=timestep_uom)

        # Test 정보 출력
        print(f"\tSTART_DATE : {start_date}")
        print(f"\tEND_DATE : {end_date}")
        print(f"\tTIME_STEP : {timestep_length} {timestep_uom}")
        print(f"\tHORIZON : {self.scheduleManager._horizonLen} {'seconds'}")

        # 실제 세팅된 캘린더 목록을 Loop 돌면서 확인
        full_calendar: list = self.scheduleManager.get_full_axis()

        # number_of_digits = 콘솔 출력용 자릿수 값
        # 예를 들어 calendar 갯수가 86400 개라고 하면,
        # number_of_digits 값은 5 가 됨.
        # 콘솔에 출력 시 00000 ~ 86400 으로 캘린더 번호의 자릿수를 맞추기 위한 변수
        number_of_digits: int = math.floor(math.log(len(full_calendar), 10)) + 1

        # Calendar 들을 순서대로 하나씩 꺼내며 Loop
        for obj in full_calendar:
            cal: dict = obj  # 현재 캘린더
            print(f"\t{'%0{}d'.format(number_of_digits) % full_calendar.index(obj)}"  # 각 Calendar 번호: int
                  f"\t{cal['DATE']}"        # 각 Calendar 의 날짜 정보: datetime
                  f"\t{cal['WORK_YN']}")    # 각 Calendar 의 업무 가능 여부: bool

    def test_setup_with_str(self):
        """
        start_date 파라메터를 str 형식으로 넘겨 줄 경우에 대한 테스트
        :return: void
        """

        print(f"\nTest Setup with str")

        # start_date 값이 아래와 같이 문자열로 넘어 올 경우를 상정
        # datetime 변환 시 format이 필요하므로 변환 처리를 위한 format 문자열도 함께 설정
        start_date_format: str = "%Y-%m-%d %H:%M:%S"
        start_date: str = "2020-03-23 00:00:00"

        # Calendar 클래스의 static 메서드를 통해 캘린더 인스턴스 공통으로 사용될 날짜 문자열의 형식을 지정
        TimeUtility.set_date_str_format(format_string=start_date_format)

        # start_date 및 end_date 가 datetime 인스턴스로 넘어올 경우를 상정
        start_date: datetime.datetime = datetime.datetime(year=2020, month=3, day=23)
        end_date: datetime.datetime = datetime.datetime(year=2020, month=3, day=30)

        timestep_length: int = 6
        timestep_uom: str = "hours"

        # start_date 파라메터가 datetime 인스턴스로 넘어올 경우 별도의 처리 없이 진행되도록 설계
        self.scheduleManager.init(start_date=start_date, end_date=end_date,
                                  time_step_length=timestep_length, time_step_uom=timestep_uom)

        # Test 정보 출력
        print(f"\tSTART_DATE : {start_date}")
        print(f"\tEND_DATE : {end_date}")
        print(f"\tTIME_STEP : {timestep_length} {timestep_uom}")
        print(f"\tHORIZON : {self.scheduleManager._horizonLen} {'seconds'}")

        # 실제 세팅된 캘린더 목록을 Loop 돌면서 확인
        full_calendar: list = self.scheduleManager.get_full_axis()

        # number_of_digits = 콘솔 출력용 자릿수 값
        # 예를 들어 calendar 갯수가 86400 개라고 하면,
        # number_of_digits 값은 5 가 됨.
        # 콘솔에 출력 시 00000 ~ 86400 으로 캘린더 번호의 자릿수를 맞추기 위한 변수
        number_of_digits: int = math.floor(math.log(len(full_calendar), 10)) + 1

        # Calendar 들을 순서대로 하나씩 꺼내며 Loop
        for obj in full_calendar:
            cal: dict = obj  # 현재 캘린더
            print(f"\t{'%0{}d'.format(number_of_digits) % full_calendar.index(obj)}"  # 각 Calendar 번호: int
                  f"\t{cal['DATE']}"        # 각 Calendar 의 날짜 정보: datetime
                  f"\t{cal['WORK_YN']}")    # 각 Calendar 의 업무 가능 여부: bool

    def test_setup_with_str_microsec_step(self):
        """
        start_date 파라메터를 str 형식으로 넘겨 줄 경우에 대한 테스트
        timestep 단위가 지원되지 않는 단위로 설정되었을 경우에 대한 테스트 : 이 테스트에서는 microseconds
        :return: void
        """

        print(f"\nTest Setup with str and microseconds TimeStep")

        # start_date 값이 아래와 같이 문자열로 넘어 올 경우를 상정
        # datetime 변환 시 format이 필요하므로 변환 처리를 위한 format 문자열도 함께 설정
        start_date_format: str = "%Y-%m-%d %H:%M:%S"

        # Calendar 클래스의 static 메서드를 통해 캘린더 인스턴스 공통으로 사용될 날짜 문자열의 형식을 지정
        TimeUtility.set_date_str_format(format_string=start_date_format)

        # start_date 및 end_date 가 datetime 인스턴스로 넘어올 경우를 상정
        start_date: datetime.datetime = datetime.datetime(year=2020, month=3, day=23)
        end_date: datetime.datetime = datetime.datetime(year=2020, month=3, day=30)

        timestep_length: int = 1
        timestep_uom: str = "microseconds"

        # start_date 파라메터가 datetime 인스턴스로 넘어올 경우 별도의 처리 없이 진행되도록 설계
        try:
            self.scheduleManager.init(start_date=start_date, end_date=end_date,
                                      time_step_length=timestep_length, time_step_uom=timestep_uom)
        except AssertionError:
            print(f"\ttime_step_uom 파라메터로 {timestep_uom} 는 설정할 수 없습니다")

        # Test 정보 출력
        print(f"\tSTART_DATE : {start_date}")
        print(f"\tEND_DATE : {end_date}")
        print(f"\tTIME_STEP : {timestep_length} {timestep_uom}")
        print(f"\tHORIZON : {self.scheduleManager._horizonLen} {'seconds'}")


if __name__ == '__main__':
    tester: ScheduleManagerTestCase = ScheduleManagerTestCase()
    tester.test_uom_timedelta()
    tester.test_setup_with_datetime()
    tester.test_setup_with_str_microsec_step()
