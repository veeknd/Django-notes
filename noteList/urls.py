from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path("add",views.addRecord,name="addRecord"),
    path("record/<str:pk>",views.viewRecord, name='viewRecord'),
    path("delete/<str:pk>",views.deleteRecord,name='deleteRecord'),
]