# coding: utf-8
from render import render


def index(request):
    content = {'users': ['gustavohenrique', 'avelino', 'python']}
    return render(request, 'index.html', content)