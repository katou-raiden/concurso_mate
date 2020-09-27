from django import template
import datetime, pytz
import math

register = template.Library()

@register.filter(name="divide_by")
def number_over(number, arg=None):

    if arg == None:
        return number % 2
    else:
        try: 
            returning = number % arg
            return returning

        except ZeroDivisionError:
            return ''

@register.filter(name="minus")
def number_minus(number, arg):
    arg = int(arg)
    number = int(number)
    if not isinstance(number, int, float) or not isinstance(arg, int, float):
        return ''
    else:
        return number - arg
        
@register.filter(name='format_date')
def format_date_our_way(date):
    pass