# coding: utf-8
from django.conf import settings
from django.http import HttpResponse
from quik import FileLoader


def render(request, template_file, content={}):
    content.update({'request': request})
    loader = FileLoader(settings.QUIK_TEMPLATE_DIR, settings.DEBUG)
    template = loader.load_template(template_file)
    r = template.render(content, loader=loader).encode('utf-8')
    return HttpResponse(r)
