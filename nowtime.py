import datetime

class now:

    def get(self, tz_set_nt, filter_nt):

        # 変数の定義
            # 時刻に関する変数
        self.dt_now = None
        self.year = None
        self.month = None
        self.day = None
        self.hour = None
        self.minute = None
        self.second = None
            # 処理に使う変数
        self.tz_set_nt = str(tz_set_nt.upper()) # タイムゾーン設定
        self.filter_nt = str(filter_nt.lower()) # フィルター設定
        self.offset_hour = None # オフセット値格納(時)
        self.offset_min = None # オフセット値格納(分)
        self.offset_which = None # オフセットの方向(plus or minus)
        self.month_size = None # 毎月の最大日数
        self.uruu = None # うるう年判定値の格納(y or n)
        self.output = None# 出力の格納

        def change(self):

            # 変数の設定
            dt_now = datetime.datetime.now(datetime.timezone.utc)
            self.year = dt_now.year
            self.month = dt_now.month
            self.day = dt_now.day
            self.hour = dt_now.hour
            self.minute = dt_now.minute
            self.second = dt_now.second

            # UTCにオフセットの加減算
            if self.offset_which == "plus":
                self.hour = self.hour + self.offset_hour
                self.minute = self.minute + self.offset_min
            elif self.offset_which == "minus":
                self.hour = self.hour - self.offset_hour
                self.minute = self.minute - self.offset_min
            else:
                self.output = 9999
                print("Error: :offset_which: value typo.")
                return(self.output)

            # うるう年の判定と設定
            if self.year % 4 == "0":
                if self.year % 100 == "0":
                    if self.year % 400 == "0":
                        self.uruu = "y"
                    else:
                        self.uruu = "n"
                else:
                    self.uruu = "y"
            else:
                self.uruu = "n"
            
            if self.uruu == "y":
                self.month_size = [None, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            elif self.uruu == "n":
                self.month_size = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                self.output = 9999
                print(":urur: value typo.")
                return(self.output)                

            # 分の処理と時の加減算
            if self.minute > 59:
                self.hour = self.hour + 1
                self.minute = self.minute - 59
            elif self.minute < 0:
                self.hour = self.hour - 1
                self.minute = self.minute + 59

            # 時の処理と日の加減算
            if self.hour > 23:
                self.day = self.day + 1
                self.hour = self.hour - 24
            elif self.hour < 0:
                self.day = self.day - 1
                self.hour = self.hour + 24

            # 日の処理と月の加減算
            if self.day > self.month_size[self.month]:
                self.month = self.month + 1
                self.day = 1
            elif self.day < 1:
                self.month = self.month - 1
                if self.month == 0:
                    self.day = self.month_size[12]
                elif self.month == 13:
                    self.day = self.month_size[1]

            if self.month > 13:
                self.output = 9999
                print("Error: Incorrect month value.")
                return(self.output)
            elif self.month < 0:
                self.output = 9999
                print("Error: Incorrect month value.")
                return(self.output)

            # 月の処理と年の加減算
            if self.month == 13:
                self.year = self.year + 1
                self.month = 1
            elif self.month == 0:
                self.year = self.year - 1
                self.month = 12

            # 出力の処理
            if self.filter_nt == "year":
                self.output = self.year
            elif self.filter_nt == "month":
                self.output = self.month
            elif self.filter_nt == "day":
                self.output = self.day
            elif self.filter_nt == "hour":
                self.output = self.hour
            elif self.filter_nt == "minute":
                self.output = self.minute
            elif self.filter_nt == "second":
                self.output = self.second
            else:
                self.output = 9999
                print("Error: Incorrect filter value.")
                return(self.output)


        # フィルター値の正誤判定
        if self.filter_nt not in ["year", "month", "day", "hour", "minute", "second"]:
            self.output = 9999
            print("Error: Incorrect filter value.")
            return(self.output)

        # タイムゾーン(ネーム)処理
        # 未実装

        # タイムゾーン(コード)処理
        if self.tz_set_nt == "GMT":
            self.offset_hour = 0
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "UTC":
            self.offset_hour = 0
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "ECT":
            self.offset_hour = 1
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "EET":
            self.offset_hour = 2
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "ART":
            self.offset_hour = 2
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "EAT":
            self.offset_hour = 3
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "MET":
            self.offset_hour = 3
            self.offset_min = 30
            self.offset_which = "plus"
        elif self.tz_set_nt == "NET":
            self.offset_hour = 4
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "PLT":
            self.offset_hour = 5
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "IST":
            self.offset_hour = 5
            self.offset_min = 30
            self.offset_which = "plus"
        elif self.tz_set_nt == "BST":
            self.offset_hour = 6
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "VST":
            self.offset_hour = 7
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "CTT":
            self.offset_hour = 8
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "JST":
            self.offset_hour = 9
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "ACT":
            self.offset_hour = 9
            self.offset_min = 30
            self.offset_which = "plus"
        elif self.tz_set_nt == "AET":
            self.offset_hour = 10
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "SST":
            self.offset_hour = 11
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "NST":
            self.offset_hour = 12
            self.offset_min = 0
            self.offset_which = "plus"
        elif self.tz_set_nt == "MIT":
            self.offset_hour = 11
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "HST":
            self.offset_hour = 10
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "AST":
            self.offset_hour = 9
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "PST":
            self.offset_hour = 8
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "PNT":
            self.offset_hour = 7
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "MST":
            self.offset_hour = 7
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "CST":
            self.offset_hour = 6
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "EST":
            self.offset_hour = 5
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "IET":
            self.offset_hour = 5
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "PRT":
            self.offset_hour = 4
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "CNT":
            self.offset_hour = 3
            self.offset_min = 30
            self.offset_which = "minus"
        elif self.tz_set_nt == "AGT":
            self.offset_hour = 3
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "BET":
            self.offset_hour = 3
            self.offset_min = 0
            self.offset_which = "minus"
        elif self.tz_set_nt == "CAT":
            self.offset_hour = 1
            self.offset_min = 0
            self.offset_which = "minus"
        else:
            self.output = 9999
            print("Error: Not timezone.")
            return(self.output)

        change(self)
        return(self.output)
        
        
