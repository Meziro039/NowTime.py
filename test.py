import nowtime
import time

while True:
    n = nowtime.get
    nt_year = n("jst", "year")
    nt_month = n("jst", "month")
    nt_day = n("jst", "day")
    nt_hour = n("jst", "hour")
    nt_min = n("jst", "minute")
    nt_sec = n("jst", "second")

    print("Time:" + str(nt_year) + "年" + str(nt_month) + "月" + str(nt_day) + "日" + str(nt_hour) + "時" + str(nt_min) + "分" + str(nt_sec) + "秒")
    time.sleep(1)