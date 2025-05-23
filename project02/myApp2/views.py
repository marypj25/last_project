from django.shortcuts import render

import datetime,math
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from .models import StudentModel
from .forms import StudentModelForm

def index(request):
    return render(request, "index.html")

def table_original(request):
    objects = StudentModel.objects.all()
    return render(request, 'table_original.html', {'objects':objects})


def student_model_form(request):
    print("request.method: ", request.method)
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect("myApp2:my_result")
    else:
        form = StudentModelForm()
        print("\nform_else:\n", form)
    context = {"form": form}
    print("\ncontext:\n", context)
    return render(request, "student_model_form.html", context)

def solution(c):
    if c == 'двадцатый':
        result = 'Да, скоро выпускной'
    else:
        result = 'Нет'
    return result


def my_result(request):
    object_list = StudentModel.objects.all().order_by("-id")
    print("\n\nobject_list: ", object_list)

    last_object = object_list.values("task", "a", "b", "c")[0]
    print("\n\nlast_object: ", last_object)
    task_formulation = object_list.values("task")[0]
    task_id = object_list.values("id")[0]["id"]
    print("task_id task_formulation: ", task_id, task_formulation)

    result = solution(last_object["c"])
    print("\nresult: ", result)

    update_obj = StudentModel.objects.filter(id=task_id)
    update_result = result
    update_obj.update(result = update_result)

    values_list = object_list.values_list()[0]
    print("\nvalues_list: ", values_list)
    task_formulation = values_list[1]
    print("\ntask_formulation: ", task_formulation)
    last_values = [values_list[1], values_list[2], values_list[3], values_list[4]]
    print("\nlast_values:", last_values)

    context = {
        "last_object": last_object,
        "task_formulation": task_formulation,
        "last_values": last_values,
        "result": result,
    }
    return render(request, "my_result.html", context)


def table(request):
    # all = AbcModel.objects.all()
    # all.delete()
    # objects_list
    objects_values =StudentModel.objects.values()
    print("\nobjects_values:", objects_values)
    # values_list
    objects_values_list = (
        StudentModel.objects.values_list().filter(id__gte=2).order_by("-id")
    )  # [0:3]
    print("\nobjects_values_list:", objects_values_list)
    cur_objects = objects_values_list
    statics_val = [
        cur_objects.aggregate(Count("a")),
        #cur_objects.aggregate(Avg("b")),
        #cur_objects.aggregate(Min("b")),
        cur_objects.aggregate(Max("c")),
        #cur_objects.aggregate(Sum("b")),
    ]
    print("\nstatics_val:", statics_val)
    statics = {"statics_val": statics_val}
    # fields_name
    fields = StudentModel._meta.get_fields()
    print("\nfields", fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)
    print("\nverbose_name_list:", verbose_name_list)
    print("\nname_list", name_list)
    field_names = verbose_name_list
    context = {
        "objects_values": objects_values,
        "name_list": name_list,
        "objects_values_list": objects_values_list,
        "verbose_name_list": verbose_name_list,
        "statics": statics,
        "field_names": field_names,
    }
    return render(request, "table.html", context)














