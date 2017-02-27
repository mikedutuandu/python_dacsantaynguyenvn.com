
from django import template
from apps.products.models import Product,Category

register = template.Library()

@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_hot_products.html')
def hot_products():
    products = Product.objects.filter(hot=True,active=True)[:5]
    return {'products':products}
@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_left_nav.html')
def left_nav():
    categories = Category.objects.filter(active=True)
    return {'categories':categories}

@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_latest_post.html')
def latest_post():
    return {}
@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_head_card.html')
def head_card():
    return {}
@register.inclusion_tag('theme_lotus/pages/inclusion_tags/_head_search.html')
def head_search():
    categories = Category.objects.filter(active=True)
    return {'categories':categories}


