from django.urls import path
from . import views

urlpatterns = [
    path('' , views.Home , name="Home Sheet"),
    path('AddUser/' , views.AddUser , name="AddUser Sheet"),
    path('UserAll/' , views.UserAll , name="UserAll Sheet"),
]