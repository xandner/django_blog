from . import jalali
from django.utils import timezone

def persian_numer_converter(mystr):
    numbers={
        "0":"۰",
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹",
        
    }
    for e,p in numbers.items():
        # .items ==> e is key , p is value
        mystr=mystr.replace(e,p)
    return mystr



def jalali_converter(time):
    j_month=['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
    time=timezone.localtime(time)
    time_str=f'{time.year},{time.month},{time.day}'
    time_tuple=jalali.Gregorian(time_str).persian_tuple()

    time_list=list(time_tuple)
    for index , month in enumerate(j_month):
        if time_list[1]==index+1:
            time_list[1]=month
            break
    output = f'{time_list[0]}/{time_list[1]}/{time_list[2]}. ساعت{time.hour}:{time.minute}'
    return persian_numer_converter(output)
