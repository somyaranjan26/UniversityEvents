from django.contrib import admin
from django.urls import path

from app.admin import appAdmin

# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appAdmin.urls),
] 

# ? To use local storage
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

