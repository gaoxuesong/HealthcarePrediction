# -*- coding: utf-8 -*-
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import json
from django.http import HttpResponse

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    userId = request.GET.get('userid','')
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'userid':userId,
            'year':datetime.now().year,
        })
    )

def prediction(request):
    """Renders the prediction page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/prediction.html',
        context_instance = RequestContext(request,
        {
            'title':'Prediction',
            'message':'suggested medical department is orthopedics.',
            'year':datetime.now().year,
        })
    )

def getpredictiondata(request):
    """get prediction resualt data"""
    userId = request.GET.get('userid','')
    ret = {'userid':userId, 'department':['orthopedics','儿科']}
    return HttpResponse( json.dumps (ret))

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
