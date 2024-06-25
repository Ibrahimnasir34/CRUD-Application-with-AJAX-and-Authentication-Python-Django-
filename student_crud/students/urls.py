# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('student/', views.student_list, name='student_list'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
    path('student/update/<int:id>/', views.student_update, name='student_update'),
    path('student/delete/<int:id>/', views.student_delete, name='student_delete'),
]
