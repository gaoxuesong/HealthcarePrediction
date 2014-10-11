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
import MySQLdb

host_mysql='192.168.1.70'
user_mysql='root'
passwd_mysql='root123'
port_mysql=3306
db_mysql='gecris'
con=MySQLdb.connect(host_mysql,user_mysql,passwd_mysql,db_mysql,port =port_mysql,charset='utf8',connect_timeout=30)
cursor=con.cursor()

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

def getdepartment(id):

   r = []
   order="SELECT PreExamDepartment,count(*) as num from ExamInfo WHERE PatientIntraID="+str(id)+" GROUP BY PreExamDepartment ORDER BY num desc"
   cursor.execute(order)
   result=cursor.fetchall()
   for i in result:
      r.append(( i[0],i[1]))
   return r


def getusername(id):
   order="SELECT PatientNameChinese FROM PatientInfo WHERE PatientIntraID="+str(id)
   cursor.execute(order)
   result=cursor.fetchall()
   if result:
      return result[0][0]
   else:
      return ''


def getpredictiondata(request):
    """get prediction resualt data"""
    userid = request.GET.get('userid','')
    data = {}
    try:
        data['userid']=userid
        data['username']=getusername(userid)
        data['dep']=getdepartment(userid)
    except:
        return HttpResponse('not exist')
    return HttpResponse( json.dumps(data, encoding='UTF-8', ensure_ascii=False) )


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
