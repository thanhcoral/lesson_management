from django.urls import path
from lesson import views

urlpatterns = [
    path('', views.LessonList.as_view()),
    path('<int:pk>/', views.LessonDetail.as_view()),
]