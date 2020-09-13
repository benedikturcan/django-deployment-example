from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values!
    """
    return value.replace(arg, '')
