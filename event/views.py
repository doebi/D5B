from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, render
from django.contrib.auth.models import User
from event.models import Product, Event
from django.db.models import Sum
from decimal import *
from datetime import datetime
import simplejson as json

def index(request):
    return render(request, 'index.html')

def track(request, user_id, barcode):
    b = get_object_or_404(Product, barcode=barcode)
    u = get_object_or_404(User, username=user_id)
    e = Event.objects.create(user=u, amount=1, value=1, product=b, action='C')
    return HttpResponse()

def deposit(request):
    data = list()
    for p in Product.objects.all():
        sumobject = Event.objects.filter(product=p).aggregate(Sum('amount'))
        if not sumobject['amount__sum']:
            sumobject['amount__sum'] = 0
        data.append({'name': p.name, 'amount': sumobject['amount__sum']})
    return render(request, 'deposit.html', {'products': data})

def sync(request):
    drinks = []
    for p in Product.objects.all():
        drinks.append({'name': p.name, 'barcode': p.barcode})
    dump = "[{'name': 'Ratsherrn', 'barcode': '90104015'}]"
    return HttpResponse(json.dumps(drinks))

def user(request, user_id):
    u = get_object_or_404(User, username=user_id)
    data = {'name': u.username, 'balance': Decimal(0)}
    for a in Event.ACTIONS:
        allEvents = Event.objects.filter(user=u, action=a[0])
        obj = allEvents.aggregate(Sum('value'), Sum('amount'))
        value = obj['value__sum']
        amount = obj['amount__sum']
        if not value:
            value = Decimal(0)
        if not amount:
            amount = 0
        data[a[0]] = amount
        if a[0] == 'C':
            data['balance'] -= value
        else:
            data['balance'] += value
    allEvents = Event.objects.filter(user=u, action='C')
    last = allEvents.latest(field_name='timestamp')
    delta = datetime.utcnow() - last.timestamp.replace(tzinfo=None)
    if delta.seconds < 1:
        text = "right now"
    elif delta.seconds < 60:
        text = "%d seconds ago" %delta.seconds
    elif delta.seconds < 3600:
        text = "%d seconds ago" %(delta.seconds / 60)
    elif delta.seconds < 86400:
        text = "%d hours ago" %(delta.seconds/60**2)
    else:
        text = "%d days ago" %delta.days
    data['last'] = last.product.name + ", " + text
    return render(request, 'user.html', {'data': data})

def userlist(request):
    users = User.objects.all()
    return render(request, 'userlist.html', {'users': users})
