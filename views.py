import helloworld
from django.shortcuts import render_to_response

def hello(request, lang="en"):
#    cad = helloworld.hello(lang)
    cad = helloworld.hello()
    return render_to_response('hello.html', locals())
