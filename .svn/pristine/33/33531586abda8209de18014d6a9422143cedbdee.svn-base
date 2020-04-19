# -*- coding: utf-8 -*-

import numpy as np
import datetime
import calendar
import cx_Oracle

from m4.ApplicationConfiguration import ApplicationConfiguration


# calendar.setfirstweekday(6)

def get_quarter(datetime_object: datetime.datetime) -> int:
    month: int = datetime_object.month
    if month < 4:
        return 1
    elif month < 7:
        return 2
    elif month < 10:
        return 3
    else:
        return 4


def get_half(datetime_object: datetime.datetime) -> int:
    month: int = datetime_object.month
    if month < 7:
        return 1
    else:
        return 2


def get_week_of_month(datetime_object: datetime.datetime):
    year: int = datetime_object.year
    month: int = datetime_object.month
    day: int = datetime_object.day
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x == day)[0][0] + 1
    return week_of_month


def generate_full_calendar(start_year: int, end_year: int) -> list:

    header = "YYYYMMDD/" \
             "WEEK/" \
             "PART_WEEK/" \
             "YR_MON/" \
             "YR/" \
             "MON/" \
             "HALF_YEAR/" \
             "QTR/" \
             "YR_PASSG_WEEK_NUM/" \
             "MON_PASSG_WEEK_NUM/" \
             "HLDAY_YN/" \
             "MON_START_DT/" \
             "MON_END_DT/" \
             "WEEK_NM/" \
             "WEEK_ENG_NM/" \
             "WEEK_START_DT/" \
             "WEEK_END_DT/" \
             "PART_WEEK_START_DT/" \
             "PART_WEEK_END_DT".split("/")

    full_calendars: list = []

    start_day: datetime.datetime = datetime.datetime(
        year=start_year, month=1, day=1
    )
    end_day: datetime.datetime = datetime.datetime(
        year=end_year, month=12, day=calendar.monthrange(year=end_year, month=12)[1]
    )

    print(f"start_day = {start_day}")
    print(f"end_day = {end_day}")

    print(f"{str(header)}")

    tmp_day: datetime.datetime = start_day
    while tmp_day <= end_day:

        former_7day: datetime.datetime = tmp_day - datetime.timedelta(days=7)

        if tmp_day.year >= start_year:
            yyyymmdd: str = tmp_day.strftime("%Y%m%d")
            yr: int = tmp_day.year
            mon: int = tmp_day.month
            yr_mon: str = tmp_day.strftime("%Y%m")
            mon_start_dt: str = tmp_day.replace(day=1).strftime("%Y%m%d")
            mon_end_dt: str = tmp_day.replace(
                day=calendar.monthrange(
                    year=tmp_day.year, month=tmp_day.month
                )[1]
            ).strftime("%Y%m%d")
            half_year: int = get_half(tmp_day)
            qtr: int = get_quarter(tmp_day)
            yr_passg_week_num: int = \
                int(former_7day.strftime("%W")) + 1 if int(tmp_day.strftime("%W")) == 0 else \
                int(tmp_day.strftime("%W"))
            week: str = "{}{}".format(yr, "%02d" % yr_passg_week_num)
            week_nm: str = "W{}".format(week)
            week_eng_nm: str = "W{}".format(week)
            week_start_dt: str = (
                    tmp_day -
                    datetime.timedelta(
                        days=tmp_day.weekday()
                    )
            ).strftime("%Y%m%d")
            week_end_dt: str = (
                    tmp_day +
                    datetime.timedelta(
                        days=(6 - tmp_day.weekday())
                    )
            ).strftime("%Y%m%d")
            part_week: str = "{}{}".format(week,
                                           "" if week_start_dt[-4:-2] == week_end_dt[-4:-2] else
                                           "A" if yr_mon[-2:] == week_start_dt[-4:-2] else
                                           "B" if yr_mon[-2:] == week_end_dt[-4:-2] else
                                           "<ERROR>")
            part_week_start_dt: str = \
                "" if part_week[-1] not in ["A", "B"] else \
                week_start_dt if part_week[-1] == "A" else \
                mon_start_dt if part_week[-1] == "B" else \
                "<ERROR>"
            part_week_end_dt: str = \
                "" if part_week[-1] not in ["A", "B"] else \
                mon_end_dt if part_week[-1] == "A" else \
                week_end_dt if part_week[-1] == "B" else \
                "<ERROR>"
            mon_passg_week_num: int = get_week_of_month(tmp_day)
            hlday_yn: str = \
                "Y" if tmp_day.weekday() in [5, 6] else \
                "N"

            full_calendars.append(
                [
                    yyyymmdd,               # YYYYMMDD
                    week,                   # WEEK
                    part_week,              # PART_WEEK
                    yr_mon,                 # YR_MON
                    yr,                     # YR
                    mon,                    # MON
                    half_year,              # HALF_YEAR
                    qtr,                    # QTR
                    yr_passg_week_num,      # YR_PASSG_WEEK_NUM
                    mon_passg_week_num,     # MON_PASSG_WEEK_NUM
                    hlday_yn,               # HLDAY_YN
                    mon_start_dt,           # MON_START_DT
                    mon_end_dt,             # MON_END_DT
                    week_nm,                # WEEK_NM
                    week_eng_nm,            # WEEK_ENG_NM
                    week_start_dt,          # WEEK_START_DT
                    week_end_dt,            # WEEK_END_DT
                    part_week_start_dt,     # PART_WEEK_START_DT
                    part_week_end_dt,       # PART_WEEK_END_DT
                ]
            )

        tmp_day += datetime.timedelta(days=1)

    return full_calendars


if __name__ == '__main__':
    full_calendar: list = generate_full_calendar(start_year=2010, end_year=2040)
    for row in full_calendar:
        print(row)

    config: ApplicationConfiguration = ApplicationConfiguration.instance()
    config.init('m4.properties')
    uri_map = dict(config.find_section("DatabaseSource"))
    tns: str = cx_Oracle.makedsn(
        host=uri_map["ds.connection.host"],
        port=uri_map["ds.connection.port"],
        sid=uri_map["ds.connection.sid"]
    )
    _pool: cx_Oracle.SessionPool = cx_Oracle.SessionPool(
        user=uri_map["ds.connection.id"],
        password=uri_map["ds.connection.password"],
        dsn=tns,
        min=1, max=20, increment=1, threaded=True
    )
    _connection = _pool.acquire()
    cursor = _connection.cursor()
    cursor.executemany(
        """
        """,
        full_calendar)
    _connection.commit()
    _pool.release(_connection)
