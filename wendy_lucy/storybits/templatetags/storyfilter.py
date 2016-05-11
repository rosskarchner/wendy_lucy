import re

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

POI_FINDER = re.compile(r'\[(.+?)\]')


def repl_function(match):
    groups = match.groups()
    return "<a class='poi' data-poi='{0}' href='{0}'>{0}</a>".format(*groups)


@register.filter
@stringfilter
def render_poi_links(value):
    return POI_FINDER.sub(repl_function, value)
