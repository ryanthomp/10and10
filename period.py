from datetime import datetime


class Time:
    def __init__(self):
        pass

    def check(self):
        global time
        time = datetime.now().strftime('%H:%M.%S')
        print(time)
        if "08:20.24" <= time < "09:30.24":
            if "08:30.00" <= time <= "09:20.00":
                return True
            else:
                return False

        elif "09:30.24" <= time < "10:30.24":
            if "09:40.00" <= time <= "10:20.00":
                return True
            else:
                return False

        elif "10:30.24" <= time < "11:30.24":
            if "10:40.00" <= time <= "11:20.00":
                return True
            else:
                return False

        elif "11:30.24" <= time < "12:30.24":
            if "11:40.00" <= time <= "12:20.00":
                return True
            else:
                return False

        elif "12:30.24" <= time < "13:25.24":
            if "12:40.00" <= time <= "13:15.00":
                return True
            else:
                return False

        elif "13:25.24" <= time < "14:25.24":
            if "13:35.00" <= time <= "14:15.00":
                return True
            else:
                return False

        elif "14:25.24" <= time <= "15:25.24":
            if "14:35.00" <= time <= "15:15.00":
                return True
            else:
                return False
