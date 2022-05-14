from django.urls import path
from company import views

urlpatterns = [
    # Company Url
    path('company/', views.CompanyViews.as_view()),
    path('company/<int:pk>', views.CompanyDetail.as_view()),
    path('company/admin', views.CompanyCreate.as_view()),
    path('company/admin/<int:pk>', views.CompanyDetailAdmin.as_view()),
    
    path('company/user/<int:pk>', views.GetUserCompany.as_view()),

    # Level Url
    path('level/', views.LevelViews.as_view()),
    path('level/<int:pk>', views.LevelDetail.as_view()),
    path('level/admin', views.LevelCreate.as_view()),
    path('level/admin/<int:pk>', views.LevelDetailAdmin.as_view()),

    path('level/user/<int:pk>', views.GetUserLevel.as_view()),

    # Employee Url
    path('emp/', views.EmployeeViews.as_view()),
    path('emp/<int:pk>', views.EmployeeDetail.as_view()),
    path('emp/admin', views.EmployeeCreate.as_view()),
    path('emp/admin/<int:pk>', views.EmployeeDetailAdmin.as_view()),

    path('emp/user/<int:pk>', views.GetUserEmployee.as_view())
]