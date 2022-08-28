from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from.models import Task
# Create your views here.
from .forms import Taskform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
def todo(request):

    if request.method=='POST':
        task=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(name=task,priority=priority,date=date)
        task.save()
    task1 = Task.objects.all()

    return render(request,'index.html',{"task1":task1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=Taskform(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task} )
class Tasklistview(ListView):
    model=Task
    template_name = 'index.html'
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kewargs={'pk':self.object.id})
class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')
