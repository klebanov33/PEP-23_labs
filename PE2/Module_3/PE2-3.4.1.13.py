class WeekDayError(Exception):
    pass
	
class Weeker:
    Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        
        if day not in Weeker.Days:
            raise WeekDayError
        
        self.__cur_day_str = day
        
        if day == 'Mon':
            self.__cur_day_num = 1
        if day == 'Tue':
            self.__cur_day_num = 2
        if day == 'Wed':
            self.__cur_day_num = 3
        if day == 'Thu':
            self.__cur_day_num = 4
        if day == 'Fri':
            self.__cur_day_num = 5
        if day == 'Sat':
            self.__cur_day_num = 6
        if day == 'Sun':
            self.__cur_day_num = 7
        
           
    def __str__(self):
        return self.__cur_day_str

    def add_days(self, n):
        if n > 7:
            self.__dwww = n - (n//7)*7 #dwww - days without whole week(s)
        else:
            self.__dwww = n    
        self.__cur_day_num = self.__cur_day_num + self.__dwww
        self.__cur_day_num = self.__cur_day_num - (self.__cur_day_num//7)*7
        if self.__cur_day_num == 1:
            self.__cur_day_str = 'Mon'
        if self.__cur_day_num == 2:
            self.__cur_day_str = 'Tue'
        if self.__cur_day_num == 3:
            self.__cur_day_str = 'Wed'
        if self.__cur_day_num == 4:
            self.__cur_day_str = 'Thu'
        if self.__cur_day_num == 5:
            self.__cur_day_str = 'Fri'
        if self.__cur_day_num == 6:
            self.__cur_day_str = 'Sat'
        if self.__cur_day_num == 7:
            self.__cur_day_str = 'Sun' 
        return  self.__cur_day_str      

    def subtract_days(self, n):
        if n > 7:
            self.__dwww = n - (n//7)*7 #dwww - days without whole week(s)
        else:
            self.__dwww = n    
        self.__cur_day_num = self.__cur_day_num + (7 - self.__dwww)
        self.__cur_day_num = self.__cur_day_num - (self.__cur_day_num//7)*7
        if self.__cur_day_num == 1:
            self.__cur_day_str = 'Mon'
        if self.__cur_day_num == 2:
            self.__cur_day_str = 'Tue'
        if self.__cur_day_num == 3:
            self.__cur_day_str = 'Wed'
        if self.__cur_day_num == 4:
            self.__cur_day_str = 'Thu'
        if self.__cur_day_num == 5:
            self.__cur_day_str = 'Fri'
        if self.__cur_day_num == 6:
            self.__cur_day_str = 'Sat'
        if self.__cur_day_num == 7:
            self.__cur_day_str = 'Sun'
        if self.__cur_day_num == 0:
            self.__cur_day_str = 'Sun' 
        return  self.__cur_day_str

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('test')
except WeekDayError:
    print("Sorry, I can't serve your request.")