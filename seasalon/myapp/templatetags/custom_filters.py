from django import template

register = template.Library()

@register.filter
def get_rating_color(value):
    if value == 1 or value == 2:
        return 'red'
    elif value == 3:
        return 'orange'
    elif value == 4 or value == 5:
        return 'green'
    else:
        return ''