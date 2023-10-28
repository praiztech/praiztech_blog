from django import template

from wagtail.models import Page
from ..models import Logo
from home.models import HomePage

register = template.Library()

@register.inclusion_tag('tags/logo.html')
def logo():
    site_logo = Logo.objects.first()
    return {"site_logo": site_logo}

@register.inclusion_tag('tags/main_nav.html', takes_context=True)
def main_nav(context):
    main_nav_items = HomePage.objects.first().get_children().live().in_menu()
    return {
        'main_nav_items': main_nav_items,
        'request': context['request']
        }

@register.inclusion_tag('tags/breadcrumb_nav.html', takes_context=True)
def breadcrumb_nav(context):
    self = context.get("self")
    if self.depth <= 2:
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=1)
    return {
        "ancestors": ancestors,
        "request": context["request"],
    }