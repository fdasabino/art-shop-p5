from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Daniela's Art Shop"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Portal"


urlpatterns = [
    path("", include("home.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("products/", include("products.urls")),
]
