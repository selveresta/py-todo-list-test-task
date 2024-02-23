from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import TodoForm, TagForm, UpdateTagForm
from .models import Todo, Tag
import datetime

###############################################


def index(request):

    item_list = Todo.objects.order_by("-created_datetime")

    if request.method == "POST":
        # dat = datetime.datetime(request.POST["deadline_datetime"])
        # print(dat)
        # print(request.POST["deadline_datetime"])
        form1 = TodoForm(request.POST)
        form2 = TagForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect("todo")

        if form2.is_valid():
            form2.save()
            return redirect("todo")

    res_list = []
    for todo in item_list:
        res_tags = []
        tags = todo.tags.all()

        for tag in tags:
            res_tags.append(str(tag))

        res = {
            "id": todo.id,
            "content": todo.content,
            "created_datetime": todo.created_datetime,
            "deadline_datetime": todo.deadline_datetime,
            "is_done": todo.is_done,
            "tags": "No Tags" if len(res_tags) == 0 else ", ".join(res_tags),
        }

        res_list.append(res)

    formtodo = TodoForm()
    formtag = TagForm()

    page = {
        "forms": {"todoForm": formtodo, "tagForm": formtag},
        "list": res_list,
        "title": "TODO LIST",
    }
    return render(request, "todo/index.html", page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect("todo")


def tags(request):
    tags = Tag.objects.all()
    return render(request, "todo/tags.html", {"tags": tags})


def makeComplete(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.is_done = True
    item.save()
    return redirect("todo")


def undo(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.is_done = False
    item.save()
    return redirect("todo")


def deleteTag(request, item_id):
    tag = Tag.objects.get(id=item_id)
    tag.delete()
    return redirect("tags")


def editTag(request, item_id):
    tag = Tag.objects.get(id=item_id)
    form = UpdateTagForm(tag.name)

    if request.method == "POST":
        print(request.POST)
        if request.POST.get("name"):
            tag.name = request.POST["name"]
            tag.save()
            return redirect("tags")

    return render(request, "todo/updateTag.html", {"tag": tag, "form": form})
