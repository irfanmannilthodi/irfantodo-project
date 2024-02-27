from django.shortcuts import render, redirect
from. models import Ttask
from. form import todoform

# Create your views here.
def add(request):
    task2 = Ttask.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Ttask(name=name,priority=priority,date=date)

        task.save()
    return render(request,'home.html',{'task1':task2})
# def detail(request):
#
#     return render(request,'detail.html',)
def delete(request,taskid):
    task=Ttask.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Ttask.objects.get(id=id)
    f=todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html',{'f':f,'task':task})

