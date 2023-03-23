from django.contrib import admin
from django.urls import path
from django.urls import url
from polls import views

urlpatterns = [
    url("user/",views.UserApiView.as_view)
]
 