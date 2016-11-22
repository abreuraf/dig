from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'dig.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^production/', include('production.urls', namespace='production')),
    url(r'^admin/', include(admin.site.urls)),   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)