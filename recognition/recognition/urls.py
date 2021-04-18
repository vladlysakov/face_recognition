from django.contrib import admin
from django.urls import path, include

from face import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urls))
]
