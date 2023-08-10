from django import template
import base64

register = template.Library()


@register.filter(name='base64encode')
def base64_encode(value):
    return base64.b64encode(value).decode('utf-8')


@register.filter(name='base64decode')
def base64_decode(value):
    return base64.b64decode(value).decode('utf-8')
