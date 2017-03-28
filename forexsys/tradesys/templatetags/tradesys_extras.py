from django import template

register = template.Library()

@register.filter
def hash(h, key):
    if h.has_key(key):
        return h[key]
    else:
        return u'NoValue'

