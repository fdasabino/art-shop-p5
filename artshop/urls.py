from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Daniela's Art Shop"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Portal"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
