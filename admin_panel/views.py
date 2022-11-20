from django.shortcuts import render , redirect
from.models import *


def home(request):
    status_obj = TaskStatus.objects.all()
    task_obj = Task.objects.select_related("task_status")
    if request.method == "POST":
        if request.POST.get("form_type") == "status_filter":
            search_filter       = request.POST.get("search_filter")

            if search_filter == "All":
                task_obj = task_obj
                
            else:

                filter_status = TaskStatus.objects.get(id = search_filter)
                task_obj = Task.objects.select_related("task_status").filter(task_status = filter_status)

            context = {
                "task_obj":task_obj,
                "status_obj":status_obj,
                "search_filter":search_filter
            }

        else:
            task   = request.POST.get("task")
            Task.objects.create(task_name = task , task_status = TaskStatus.objects.get(status = "In-Progress"))
            return redirect("/")
    
    context = {
        "task_obj":task_obj,
        "status_obj":status_obj
    }
    return render(request,'home.html',context)


def update_task(request):
     if request.method == "POST":
        task   = request.POST.get("task")
        task_id = request.POST.get("task_id")
        status  = request.POST.get("status_id")

        Task.objects.filter(id = task_id).update(
            task_name       = task,
            task_status          = TaskStatus.objects.get(id = status)
        )
        
        
        return redirect("/")

def delete_task(request,id):
    Task.objects.get(id = id).delete()
    return redirect("/")