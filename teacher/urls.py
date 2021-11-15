from django.urls import path
from teacher import views

urlpatterns = [
    path('', views.TeacherList.as_view()),
    path('<int:pk>/', views.TeacherDetail.as_view()),
]