from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('TestApp/', include('TestApp.urls')),
    path('admin/', admin.site.urls),
    path('', include('TestApp.urls'))
]
