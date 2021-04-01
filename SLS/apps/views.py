from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import *
from .forms import *

def home(request):
    title = 'Dashboard'
    data = []
    data_save = Savings.objects.all().values('person_id').annotate(Sum('amount'))
    for d in data_save:
        da = {
            'id':d['person_id'],
            'person':Person.objects.get(id=d['person_id']),
            'amount':d['amount__sum']
        }
        data.append(da)
    context = {
        'title': title,
        'data': data,
    }
    return render(request, 'home.html',context)

def savings_list(request):
    title = 'Savings List'
    data = Savings.objects.all()
    context = {
        'title': title,
        'data': data,
    }
    return render(request, 'savings_list.html',context)

def savings_add(request):
    title = 'Add Savings'
    form = SavingsCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'title': title,
        #'data': data,
        'form': form,
    }
    return render(request, 'savings_add.html',context)

def savings_person(request,id):
    title = 'Add Savings'
    data = Savings.objects.filter(person_id=id).order_by('-date')
    context = {
        'title': title,
        'data':data,
        'person':Person.objects.get(id=id),
    }
    return render(request, 'savings_person.html',context)