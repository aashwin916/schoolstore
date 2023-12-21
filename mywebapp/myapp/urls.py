from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.school, name='school.html'),
    path('reg/',views.reg,name='reg'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('reg_form/', views.reg_form, name='reg_form'),
    # path('reg_result/', views.reg_result, name='reg_result'),
    path('process_reg/', views.process_reg, name='process_reg'),

]