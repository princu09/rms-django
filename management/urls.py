from django.views.decorators.csrf import csrf_exempt
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import RedirectView


urlpatterns = [

    # Basic Page For Everyone
    url(r'^admin', RedirectView.as_view(url='/home')),
    path('home', views.index, name="Main Page"),

    path('add_user', views.add_user, name="Add User Page"),
    path('user_list', views.user_list, name="User List Page"),

    path('delete_member/<int:id>', views.delete_member, name="User List Page"),

    path('add_maintenance', views.add_maintenance, name="Add Maintainance Page"),
    path('maintenance_list', views.maintenance_list, name="List Maintainance Page"),
    
    path('delete_maintenance/<int:id>', views.delete_maintenance, name="Delete Maintainance Page"),
    path('edit_maintenance/<int:id>', views.edit_maintenance, name="Edit Maintainance Page"),
    
    path('add_notice', views.add_notice, name="Add Notice"),
    path('notice_list', views.notice_list, name="List Notice"),
    
    path('gallery', views.gallery, name="Gallery"),
    
    path('handle_login', views.handle_login, name="Login Page"),
    path('handle_logout', views.handle_logout, name="Login Page"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
