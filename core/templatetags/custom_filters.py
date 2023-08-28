from django import template

register = template.Library()


def format_number(value):
    value = float(value)
    if value >= 1000000000:
        return "{:.1f}B".format(value / 1000000000)
    elif value >= 1000000:
        return "{:.1f}M".format(value / 1000000)
    elif value >= 1000:
        return "{:.1f}K".format(value / 1000)
    return int(value)


register.filter("format_number", format_number)
