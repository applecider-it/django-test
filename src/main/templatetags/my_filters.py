from django import template

register = template.Library()

@register.filter
def asset(obj, name):
    return obj.asset(name)