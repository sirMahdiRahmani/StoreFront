from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Store Front Admin'
admin.site.site_index = 'Admin'

urlpatterns = [
    path('my-admin-panel/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('store/', include('store.urls')),
]
