from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from lyceum import settings


urlpatterns = [
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('catalog/', include('catalog.urls')),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
