from django import template

register = template.Library()

@register.simple_tag
def multiply(qty, unit_price, *args, **kwargs):
    return float(qty * unit_price)
