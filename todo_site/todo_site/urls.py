from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    #####################home_page###########################################
    path("", views.index, name="todo"),
    ####################give id no. item_id name or item_id=i.id ############
    # pass item_id as primary key to remove that the todo with given id
    path("del/<str:item_id>", views.remove, name="del"),
    path("makeComplete/<str:item_id>", views.makeComplete, name="makeComplete"),
    path("undo/<str:item_id>", views.undo, name="undo"),
    path("editTag/<str:item_id>", views.editTag, name="editTag"),
    path("deleteTag/<str:item_id>", views.deleteTag, name="deleteTag"),
    ########################################################################
    path("admin/", admin.site.urls),
    path("tags/", views.tags, name="tags"),
]
