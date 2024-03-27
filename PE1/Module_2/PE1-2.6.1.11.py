hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here

Start_hours_into_minutes = hour*60
Total_min_with_start = Start_hours_into_minutes + mins + dura
Exctract_days = Total_min_with_start%1440
Exact_hours = Exctract_days//60
Exact_minutes = Exctract_days%60
print(str(Exact_hours) + ":" + str(Exact_minutes))