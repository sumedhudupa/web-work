from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"todolist/index.html",{
        "tasks": request.session["tasks"]
    })
class CreateForm(forms.Form):
    task = forms.CharField(label="New task")
    #priority = forms.IntegerField(label="Priority", min_value=1,max_value = 5)
def add(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            task =form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("todolist:index"))

        else:
            return render(request, "todolist/add.html", {
                "form":form
            })
    return render(request,"todolist/add.html",{
        "form": CreateForm()
    })