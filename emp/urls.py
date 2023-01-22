
from django.contrib import admin
from django.urls import path,include
from .views import *



urlpatterns = [
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path("delete-emp/<int:empid>",delete_emp),
    path("update-emp/<int:empid>",update_emp),
    path("do-update-emp/<int:empid>",do_update_emp),
    path("testimonials/",Testimonials),
    path("feedback/",Feedback),
]