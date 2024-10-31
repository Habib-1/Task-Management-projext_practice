from django.shortcuts import render,redirect
from task.models import TaskModel
from . import forms
# Create your views here.
def showTask(request):
    allTask=TaskModel.objects.all()
    return render(request, 'task.html',{'task':allTask})

def add_task(request):
    if request.method=='POST':
        taskForm=forms.task_form(request.POST)
        if taskForm.is_valid():
            taskForm.save()
            return redirect('all_task')
        
    else:
        taskForm=forms.task_form()
    return render(request,"add_task.html",{'form':taskForm})

def edit_task(request,pk):
    post=TaskModel.objects.get(pk=pk)
    taskForm=forms.task_form(instance=post)
    if request.method=='POST':
        taskForm=forms.task_form(request.POST,instance=post)
        if taskForm.is_valid():
            taskForm.save()
            return redirect('all_task')
    
    return render(request,"add_task.html",{'form':taskForm})

def delete_task(request,pk):
    deletePost= TaskModel.objects.get(pk=pk)
    deletePost.delete()
    return redirect('all_task')