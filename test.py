import nowtime

set = nowtime.now().get("jst", "hour")
print(set)

'''
while True:
    nt_y = nowtime.get("jst", "year")
    nt_mo = nowtime.get("jst", "month")
    mt_d = nowtime.get("jst", "day")
    nt_h = nowtime.get("jst", "hour")
    nt_m = nowtime.get("jst", "minute")
    nt_s = nowtime.get("jst", "second")
    print(str(nt_y) + "年" + str(nt_mo) + "月" + str(mt_d) + "日" + str(nt_h) + "時" + str(nt_m) + "分" + str(nt_s) + "秒")
    time.sleep(1)
'''