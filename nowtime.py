import datetime

# 変数定義
nowtime = 0
dt_now = 0
tz_set = "0"
filter_set = "0"
offset_which = "0" # plus or minus
offset = 0
year = 0
month = 0
day = 0
hour = 0
minute = 0
second = 0
uruu = "0" # y or n
max_month = [0]
filter_box = [0]

def change():
    # Global
    global nowtime
    global dt_now
    global tz_set
    global filter_set
    global offset_which
    global offset
    global year
    global month
    global day
    global hour
    global minute
    global second
    global uruu
    global max_month
    global filter_box

    # 時間の取得と設定
    dt_now = datetime.datetime.now(datetime.timezone.utc)
    year = dt_now.year
    month = dt_now.month
    day = dt_now.day
    hour = dt_now.hour
    minute = dt_now.minute
    second = dt_now.second

    # UTCに時間を加算
    if offset_which == "plus":
        hour = hour + offset
    if offset_which == "minus":
        hour = hour + offset

    # うるう年の判定
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                uruu = "y"
            else:
                uruu = "n"
        else:
            uruu = "y"
    else:
        uruu = "n"

    # 時間と日の処理
    if hour > 24:
        day = day + 1
        hour = hour - 24
    if hour < 0:
        day = day - 1
        hour = hour + 24

    # 日と月の処理
    if uruu == "y":
        max_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if uruu == "n":
        max_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day > max_month[month - 1]:
        month = month + 1
        day = 0
    if day < 0:
        month = month - 1
        if month == 0:
            day = max_month[month]
        else:
            day = max_month[month - 1]

    # 月と年の処理
    if month == 0:
        year = year - 1
        month = 12
    if month == 13:
        year = year + 1
        month = 1

    # 出力の処理
    if filter_set == "year":
        nowtime = year
    if filter_set == "month":
        nowtime = month
    if filter_set == "day":
        nowtime = day
    if filter_set == "hour":
        nowtime = hour
    if filter_set == "minute":
        nowtime = minute
    if filter_set == "second":
        nowtime = second

    # エラーの処理
    filter_box = ["year", "month", "day", "hour", "minute", "second"]
    if filter_set not in filter_box:
        nowtime = 9999


def get(timezone, filter):
    # Global
    global nowtime
    global dt_now
    global tz_set
    global filter_set
    global offset_which
    global offset
    global year
    global month
    global day
    global hour
    global minute
    global second
    global uruu
    global max_month
    global filter_box

    # 変数の処理
    tz_set = timezone.upper()
    filter_set = filter.lower()

    # timezone処理
    if tz_set == "JST":
        offset = 9
        offset_which = "plus"
    else: # ここどうにかする。
        offset = 0
        print("9999")

    change()
    return nowtime