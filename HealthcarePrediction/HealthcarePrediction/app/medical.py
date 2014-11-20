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
import pymongo

conn = None
servers = "mongodb://192.168.1.152:27017"

def connect(servers):
    conn = pymongo.Connection(servers)
    return conn

def close(conn):
    conn.disconnect()



def getMedical(request):
    """get prediction resualt data"""
    global conn
    conn = connect(servers)
    tname = request.GET.get('userid','')
    data = {}
    try:
        db = conn.medical
        res = db.tname.find()
    except:
        return HttpResponse('not exist')
    close(conn)
    return HttpResponse( json.dumps(res, encoding='UTF-8', ensure_ascii=False) )

