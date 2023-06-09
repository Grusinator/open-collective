from django import template

register = template.Library()

@register.filter
def to_date(value):
    return value.date()