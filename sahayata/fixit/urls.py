from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="fixit"),
    path('add_fix', views.add_fix, name="add_fix")
]
