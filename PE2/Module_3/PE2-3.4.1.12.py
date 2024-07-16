class Timer:
    def __init__(self, hh = 0, mm = 0, ss = 0):
        self.HH = hh
        self.MM = mm
        self.SS = ss

    def __str__(self):
        if self.HH < 10:
            self.HH_str = "0" + str(self.HH)
        else:
            self.HH_str = str(self.HH)

        if self.MM < 10:
            self.MM_str = "0" + str(self.MM)
        else:
            self.MM_str = str(self.MM)

        if self.SS < 10:
            self.SS_str = "0" + str(self.SS)
        else:
            self.SS_str = str(self.SS)
            
        self.str = self.HH_str + ':' + self.MM_str + ':' + self.SS_str
        return self.str

    def next_second(self):
        self.full_time = ((self.HH*3600) + (self.MM*60) + (self.SS + 1))
        if self.full_time == 86400:
            self.full_time = 0
        self.HH = self.full_time//3600
        self.MM = (self.full_time - (self.HH * 3600))//60
        self.SS = self.full_time - (self.HH * 3600) - (self.MM * 60)
        self.__str__()

    def prev_second(self):
        self.full_time = ((self.HH*3600) + (self.MM*60) + (self.SS - 1))
        if self.full_time == -1:
            self.full_time = 86399
        self.HH = self.full_time//3600
        self.MM = (self.full_time - (self.HH * 3600))//60
        self.SS = self.full_time - (self.HH * 3600) - (self.MM * 60)
        self.__str__()

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)