from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, render
from django.contrib.auth.models import User
from event.models import Product, Event
from django.db.models import Sum
from decimal import *

def index(request):
    return render(request, 'index.html')

def track(request, user_id, brand):
    return HttpResponse("tracking!")

def deposit(request):
    data = list()
    for p in Product.objects.all():
        sumobject = Event.objects.filter(product=p).aggregate(Sum('amount'))
        if not sumobject['amount__sum']:
            sumobject['amount__sum'] = 0
        data.append({'name': p.name, 'amount': sumobject['amount__sum']})
    return render(request, 'deposit.html', {'products': data})

def stats(request):
    return HttpResponse("stats page")

def user(request, user_id):
    u = User.objects.get(username=user_id)
    data = {'name': u.username, 'sum': Decimal(0)}
    for a in Event.ACTIONS:
        obj = Event.objects.filter(user=u, action=a[0]).aggregate(Sum('value'))
        value = obj['value__sum']
        if not value:
            value = Decimal(0)
        data[a[0]] = value
        if a[0] == 'C':
            data['sum'] -= value
        else:
            data['sum'] += value
    return render(request, 'user.html', {'data': data})

def userlist(request):
    users = User.objects.all()
    return render(request, 'userlist.html', {'users': users})
