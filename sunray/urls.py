from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    
    path('', views.index, name='index'),
    path('large_project/<int:pk>/', views.large_project_detail, name='large_project_detail'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('upload/project/', views.upload_project, name='upload_project'),
    path('upload/large_project/', views.upload_large_project, name='upload_large_project'),
    path('dashboard/', views.dashboard, name='dashboard'),
 

    path('edit/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete/<int:pk>/', views.delete_project, name='delete_project'),

    path('edit_large_project/<int:pk>/', views.edit_large_project, name='edit_large_project'),
    path('delete_large_project/<int:pk>/', views.delete_large_project, name='delete_large_project'),
 

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)