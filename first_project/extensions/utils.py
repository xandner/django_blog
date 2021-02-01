from . import jalali
from django.utils import timezone


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
    return output
