from django import template

register = template.Library()


@register.filter(name="str")
def string(value):
    return str(value)