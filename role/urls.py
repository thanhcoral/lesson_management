from django.urls import path
from role import views

urlpatterns = [
    path('', views.RoleList.as_view()),
    path('<int:pk>/', views.RoleDetail.as_view()),
]