from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'pages/register/$', views.register,name='register'),
    url(r'pages/register_user/$', views.register_user,name='register_user'),
    url(r'pages/register_department/$', views.register_department,name='register_department'),
    url(r'pages/login/$',  auth_views.login,{'template_name': 'auth1/pages/login.html'}, name='login'),
    url(r'^(?P<employees_id>[0-9]+)/profile/$', views.profile, name='profile'),
    url(r'^(?P<department_id>[0-9]+)/department/$', views.department, name='department'),
    url(r'pages/employee_success/$', views.employee_success,name='employee_success'),
    url(r'pages/department_success/$', views.department_success,name='department_success'),
    url(r'pages/profile/', views.profile,name='profile'),
    url(r'pages/logout/$', views.logout,name='logout'),
]
