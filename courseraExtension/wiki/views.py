from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####
from wiki import bm25

import wikipedia

def index(request):
    return HttpResponse("Hello, world. You're at the wiki index.")


# https://pypi.org/project/wikipedia/#description
def get_wiki_summary(request):
    topic = request.GET.get('topic', None)

    print('topic:', topic)

    data = {
        'summary': wikipedia.summary(topic, sentences=1),
        'raw': 'Successful',
    }

    print('json-data to be sent: ', data)

    return JsonResponse(data)

def search_bm25(request):
    topic = request.GET.get('topic', None)

    print('topic:', topic)

    data = {
        'summary': bm25.do_bm25(topic),
        'raw': 'Successful',
    }

    print('json-data to be sent: ', data)

    return JsonResponse(data)
