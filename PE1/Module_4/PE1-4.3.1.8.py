def is_year_leap(year):
    if year%4 != 0:
        year = False
    elif year%100 != 0:
        year = True 
    elif year%400 != 0:
        year = False   
    else:
        year = True
    return year
#
# Your code from LAB 4.3.6.
#
'''a = is_year_leap(1900)
print(a)''' #There were for checking intermediate result


def days_in_month(year, month):
    month_index = [1,2,3,4,5,6,7,8,9,10,11,12]
    month_31 = [1,3,5,7,8,10,12]
    month_30 = [4,6,9,11]
    
    if year <= 0 or month not in month_index:
        return None
    elif is_year_leap(year) and month == 2:
        days = 29
    elif not is_year_leap(year) and month == 2:
        days = 28
    elif month in month_31:
        days = 31
    else:
        days = 30
    return days
    

# Write your new code here.
#

#x = days_in_month(2016,1)
#print(x, "days in the current month")

def day_of_year(year, month, day):
    month_index = [1,2,3,4,5,6,7,8,9,10,11,12]
    sum_of_days_in_months = 0
    if year <= 0 or month not in month_index:
        return None
    if day <= 0 or day > days_in_month(year, month):
        return None
    for i in range(1, (month+1)):
        sum_of_days_in_months += days_in_month(year, i)
    return sum_of_days_in_months - days_in_month(year, month) + day
x = day_of_year(2024, 3, 3)
print(x, "it is a current day")
