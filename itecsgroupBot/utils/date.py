import datetime


class DateTime:
    @staticmethod
    def get_current_time():
        now = datetime.datetime.now()
        print("Current date and time is : ", now.date())
        print("Current date and time is : ", now.time())
        return now.strftime("%Y-%m-%d %H:%M:%S")
