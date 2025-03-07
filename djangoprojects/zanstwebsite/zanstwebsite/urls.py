from django.contrib import admin
from django.urls import path
from zanstapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.calculator, name="calculator"),
]