from django import template

register = template.Library()

@register.filter
def import_js(obj, name):
    return obj.import_js(name)

@register.filter
def import_css(obj, name):
    return obj.import_css(name)
