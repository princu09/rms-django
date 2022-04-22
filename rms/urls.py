from django.contrib import admin
from django.urls import path, include
from management import urls

admin.site.site_header = "rms"
admin.site.index_title = "Welcome to rms"

urlpatterns = [
    path('siteAdminApproveByNFG/', admin.site.urls),
    path('', include('management.urls')),
]