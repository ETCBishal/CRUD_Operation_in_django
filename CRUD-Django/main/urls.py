from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('addStudents/',AddStudents.as_view(),name='addStudents'),
    path('edit/<int:id>/',EditStudents.as_view(),name='edit'),
    path('delete/<int:id>/',DeleteStudents.as_view(),name='delete'),
]