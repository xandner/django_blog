from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگو"


@register.inclusion_tag('blog/partials/hategory_navbar.html')
def category_navbar():
    return {
        'category':Category.objects.filter(status=True)
    }