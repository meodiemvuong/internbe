from django.urls import path
from user import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('logout/', views.UserLogout.as_view()),
    path('me/', views.GetMe.as_view()),
    path('update/com', views.UpdateCompany.as_view()),
    path('update/lev', views.UpdateLevel.as_view()),
    path('update/emp', views.UpdateEmployee.as_view()),
]