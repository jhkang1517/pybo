# ----- edit -----
from django import template

register = template.Library()


# register.filter 라는 어노테이션을 적용하면 템플릿에서 해당 함수를 핑
@register.filter
def sub(value, arg):
    return value - arg
# -