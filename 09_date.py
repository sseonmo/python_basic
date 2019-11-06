# 날짜 다루기
# 시간(time) 모듈
# ### 컴퓨터에서 시간 표현 방법
# - timp Stamp
# - UTC : 협정세계시
# - 그리니치 평균시
# - LST(Local Standard Time, 지방표준시)
# - 일광절약 시간제(Daylight Saving Tiem, DTS) : 흔히 summer time 가고 쓰임
# ## struct_time 시퀀스객체
# ## tiem 모듈
#

# import time
import time
from time import localtime, strftime, strptime

print(time.time())  # 1573004119.4509113
print(time.gmtime())
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=6, tm_hour=1, tm_min=35, tm_sec=19, tm_wday=2, tm_yday=310, tm_isdst=0)
print(time.localtime())
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=6, tm_hour=10, tm_min=35, tm_sec=19, tm_wday=2, tm_yday=310, tm_isdst=0)

t = time.gmtime(1234567890)
print(t)
# time.struct_time(tm_year=2009, tm_mon=2, tm_mday=13, tm_hour=23, tm_min=31, tm_sec=30, tm_wday=4, tm_yday=44, tm_isdst=0)
print(t.tm_mon)  # 2
print(t.tm_hour)  # 23
print(time.asctime(t))  # Fri Feb 13 23:31:30 2009
print(time.mktime(t))  # 1234535490.0

"""

"""
# strftime
print(strftime('%B %dth %A %I:%M'))  # November 06th Wednesday 02:45
print(strftime('%B %dth %A %I:%M', localtime()))  # November 06th Wednesday 02:45
print(strftime('%Y-%m-%d %H:%M:%S', localtime()))  # 2019-11-06 14:46:37

# stfptime
timeString = time.ctime()
print(strptime(timeString))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=6, tm_hour=14, tm_min=49, tm_sec=11, tm_wday=2, tm_yday=310, tm_isdst=-1)
print(strptime(timeString, '%a %b %d %H:%M:%S %Y'))
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=6, tm_hour=14, tm_min=51, tm_sec=41, tm_wday=2, tm_yday=310, tm_isdst=-1)
# print(strptime(timeString, '%a %b %d %H:%M:%S %y'))
# ValueError: unconverted data remains: 19 : format type이 안맞을경우

"""
### datetime 
- 기념일과 같은 날짜, 시간 연산을 위하여 사용

#### datetime 주요클래스
- datetime.date
	> 일반적으로 사용되는 그레고리안 달력의 년, 월, 일을 표현
- datetime.time
	> 시간을 시, 분 , 초, 마이크로 초, 시간대(time zone)로 표현
- datetime.datetime
	> date 클래스와 time클래스의 조합으로 구성
- datetime.timedelta
	> 두 날짜 혹은 시간 사이의 기간을 표현

#### date 클래스
- 생성자 : datetime.date(year, month, day)

#### time 클래스
- 생성자 : datetime.time(hour[, minute[, second[, microsecond[, tzinfo]]]])
- 시, 분, 초, 마이크로초, 시간대 정보를 입력받아 time 객체를 생성

#### timedelta 클래스
- 두 날짜 혹은 시간 사이의 기간을 표현
- 생성자 : timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
"""
import datetime

print(datetime.date(2019, 11, 6))   # 2019-11-06
print(datetime.time(17))    #   17:00:00

from datetime import timedelta, datetime
td_1 = timedelta(hours=7)
td_2 = timedelta(days=-3)
print(td_1 + td_2)  # -3 days, 7:00:00
print(td_1 - td_2)  # 3 days, 7:00:00
print(td_1 * 4)  # 1 day, 4:00:00
print(td_1 // 3)  # 2:20:00
print(td_1 > td_2)  # True
print(td_1 < td_2)  # False
print(timedelta(hours=24) == timedelta(seconds=86400))  # True
dt = datetime.today()
print(dt)   # 2019-11-06 16:43:08.543246
print(dt.strftime('%Y-%m-%d %H:%M:%S')) # 2019-11-06 16:44:02