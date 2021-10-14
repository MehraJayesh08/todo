from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import todoList
import datetime

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        data = todoList(title=title,date=datetime.datetime.now())
        data.save()
        todo_id = data.todo_id
        return JsonResponse({'title': title,'todo_id':todo_id},safe=False) 
    allobj = todoList.objects.all()   
    return render(request,'index.html',{'allobj':allobj})

def delete(request):
    if request.method == 'POST':
        t_id = request.POST.get('t_id')
        fdata = todoList.objects.filter(todo_id=t_id) 
        fdata.delete()
    return HttpResponse("delete")

def update(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        u_id = request.POST.get('u_id')
        fdata = todoList.objects.filter(todo_id=u_id).update(title=title)
        return JsonResponse({'title': title,'todo_id':u_id},safe=False)       
    return HttpResponse("delete")